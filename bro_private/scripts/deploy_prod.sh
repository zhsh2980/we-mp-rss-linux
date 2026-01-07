#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/../.." && pwd)"

env_file="${repo_root}/bro_private/.env"
if [[ -f "${env_file}" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "${env_file}"
  set +a
fi

PROD_SSH_HOST="${PROD_SSH_HOST:-ubuntu@154.8.205.159}"
PROD_SSH_PORT="${PROD_SSH_PORT:-22}"
PROD_APP_DIR="${PROD_APP_DIR:-/srv/we-mp-rss/app}"
PROD_SERVICE="${PROD_SERVICE:-we-mp-rss}"
DEPLOY_BRANCH="${DEPLOY_BRANCH:-deploy}"
VENV_PY="${VENV_PY:-/srv/we-mp-rss/venv/bin/python}"
RUN_PIP_INSTALL="${RUN_PIP_INSTALL:-1}"

cd "${repo_root}"

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "ERROR: working tree not clean. Please commit/stash before deploy." >&2
  exit 1
fi

current_branch="$(git rev-parse --abbrev-ref HEAD)"
if [[ "${current_branch}" != "${DEPLOY_BRANCH}" ]]; then
  echo "ERROR: current branch is '${current_branch}', expected '${DEPLOY_BRANCH}'." >&2
  echo "Hint: git switch ${DEPLOY_BRANCH} && git merge --ff-only dev" >&2
  exit 1
fi

echo "==> Pushing origin/${DEPLOY_BRANCH} ..."
git push origin "${DEPLOY_BRANCH}"

echo "==> Deploying to ${PROD_SSH_HOST} ..."

ssh_args=()
if [[ -n "${PROD_SSH_PORT}" ]]; then
  ssh_args+=(-p "${PROD_SSH_PORT}")
fi

ssh "${ssh_args[@]}" "${PROD_SSH_HOST}" bash -s <<EOF
set -euo pipefail

cd "${PROD_APP_DIR}"

echo "==> Updating code ..."
git fetch origin --prune
git reset --hard "origin/${DEPLOY_BRANCH}"

if [[ "${RUN_PIP_INSTALL}" == "1" ]]; then
  if [[ -x "${VENV_PY}" ]]; then
    echo "==> Installing Python deps ..."
    "${VENV_PY}" -m pip install -r requirements.txt
  else
    echo "WARN: ${VENV_PY} not found; skipping pip install." >&2
  fi
fi

echo "==> Restarting systemd service (${PROD_SERVICE}) ..."
sudo systemctl restart "${PROD_SERVICE}"
sudo systemctl status "${PROD_SERVICE}" --no-pager
EOF

echo "==> Done."
