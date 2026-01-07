# We-MP-RSS（二开 + 同步官方 + Ubuntu 22.04 源码部署）工作流

目标：本地（Mac）让 AI 读/改代码 → `git push` 到你的 fork → SSH 到服务器 `git pull/reset` 并重启服务。  
你的仓库（origin）：`zhsh2980/we-mp-rss-linux`（private）  
官方仓库（upstream）：`rachelos/we-mp-rss`

> 约定：所有“你自己新增的流程/脚本/密钥/笔记”都放在 `bro_private/`；`bro_private/key/` 永远不提交。

## 1) 分支与远端约定（推荐）

- `origin`：你的 fork（用于开发与部署）
- `upstream`：官方仓库（用于同步更新）
- 分支：
  - `main`：只做“跟官方保持一致”的基线（尽量只 fast-forward）
  - `dev`：你的二开开发分支
  - `deploy`：线上部署分支（从 dev 挑选/合并后发布）

## 2) 本地初始化（只做一次）

```bash
git remote add upstream https://github.com/rachelos/we-mp-rss.git
git fetch --all --prune

# 从 main 拉出 dev / deploy
git switch -c dev
git switch -c deploy main
git switch dev
```

### GitHub SSH 22 端口被拦时（可选）
如果你所在网络无法访问 `github.com:22`，用 443：

```bash
git remote set-url origin ssh://git@ssh.github.com:443/zhsh2980/we-mp-rss-linux.git
```

## 3) 跟官方同步（每次官方更新后）

推荐用 rebase，保证你的二开提交清晰：

```bash
git fetch upstream --prune

# 1) 更新 main（只快进）
git switch main
git merge --ff-only upstream/main

# 2) 把 dev 变基到最新 main
git switch dev
git rebase main

# 3) 更新 deploy（发布前再做）
git switch deploy
git merge --ff-only dev

# 4) 推送到你的 fork
git push origin main dev deploy
```

冲突处理要点：
- rebase 冲突：按提示解决后 `git rebase --continue`
- 不确定时：先 `git status` 看冲突文件，再用你的 AI 协助分析/解决

## 4) 服务器拉代码（private 必做）：GitHub Deploy Key

目的：让服务器能 `git clone/pull` 你的私有仓库，但权限最小（只读）。

在服务器上生成 deploy key（不要加密码）：
```bash
ssh ubuntu@154.8.205.159
mkdir -p ~/.ssh && chmod 700 ~/.ssh
ssh-keygen -t ed25519 -C "we-mp-rss-linux deploy@154.8.205.159" -f ~/.ssh/we_mp_rss_deploy -N ""
cat ~/.ssh/we_mp_rss_deploy.pub
```

在 GitHub：你的仓库 → `Settings` → `Deploy keys` → `Add deploy key`
- 粘贴上面的 `.pub`
- 只给 **read access**（不要勾写权限）

服务器侧可用 host alias（避免影响其它仓库）：
```bash
cat >> ~/.ssh/config <<'EOF'
Host github.com-we-mp-rss-linux
  HostName ssh.github.com
  Port 443
  User git
  IdentityFile ~/.ssh/we_mp_rss_deploy
  IdentitiesOnly yes
EOF
chmod 600 ~/.ssh/config
```

测试：
```bash
ssh -T github.com-we-mp-rss-linux
```

## 5) 服务器目录与运行方式（建议）

- 只开 `8001` 端口（安全组放行 TCP 8001）
- 使用 SQLite（默认 `data/db.db`），所以要持久化 `data/`
- 生产推荐 `systemd`：开机自启、崩溃自动拉起、统一日志（比 nohup/tmux 稳定）

推荐目录：
- 代码：`/srv/we-mp-rss/app`
- 数据：`/srv/we-mp-rss/data`（持久化）
- 配置：`/srv/we-mp-rss/config.yaml`（持久化）
- venv：`/srv/we-mp-rss/venv`

初始化管理员（WeRSS Web 登录，不是 Ubuntu 用户）：
- `USERNAME=admin`
- `PASSWORD=123654zz`

注意：`main.py` 会把环境变量打印到日志；所以生产不要长期把敏感信息放到环境变量里。管理员密码建议只在首次初始化时临时设置一次。

## 6) “出网下载依赖”是什么意思（以及国内镜像）

源码部署会从外网下载：
- `apt`：系统依赖包
- `pip`：Python 依赖（`requirements.txt`）
- Playwright：浏览器与依赖（项目依赖里包含 `playwright`）

通常腾讯云默认允许**出站**，无需额外设置；如果你发现下载很慢/失败，再换镜像：
- pip 镜像（清华）示例：写 `~/.pip/pip.conf` 设置 `index-url`
- Node/yarn 镜像：改 registry 为 `https://registry.npmmirror.com`

## 7) 手动发布（本地 push + SSH pull）

推荐使用脚本：`bro_private/scripts/deploy_prod.sh`  
发布前：确保 `deploy` 分支是你想上线的内容（从 `dev` fast-forward 过来）。

```bash
cp bro_private/.env.example bro_private/.env
./bro_private/scripts/deploy_prod.sh
```

