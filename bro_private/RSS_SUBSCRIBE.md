# WeRSS RSS 订阅使用指南

> 创建时间：2026-01-08
> 用途：详细说明如何使用 RSS 订阅 WeRSS 爬取的微信公众号文章

---

## 📋 目录

- [什么是 RSS](#什么是-rss)
- [WeRSS 的 RSS 特性](#werss-的-rss-特性)
- [RSS 订阅地址格式](#rss-订阅地址格式)
- [在各种 RSS 阅读器中订阅](#在各种-rss-阅读器中订阅)
- [订阅示例](#订阅示例)
- [高级用法](#高级用法)
- [常见问题](#常见问题)

---

## 什么是 RSS

### RSS 简介

**RSS**（Really Simple Syndication，简易信息聚合）是一种用于发布和订阅网站内容的标准格式。

### RSS 的优势

- ✅ **聚合阅读**：在一个应用中订阅多个内容源
- ✅ **无需登录**：不需要账号即可订阅
- ✅ **自动更新**：RSS 阅读器会自动检查更新
- ✅ **无广告干扰**：只展示纯净的文章内容
- ✅ **离线阅读**：大部分 RSS 阅读器支持离线缓存
- ✅ **隐私保护**：不需要关注、点赞等社交行为

### 为什么用 RSS 订阅微信公众号？

微信公众号的文章只能在微信内查看，不方便批量管理和阅读。使用 WeRSS 的 RSS 订阅功能，你可以：

- 在 RSS 阅读器中统一管理所有公众号
- 跨平台阅读（PC、Mac、手机、平板）
- 按时间线聚合所有订阅内容
- 搜索、标记、分类文章
- 导出文章存档

---

## WeRSS 的 RSS 特性

### 支持的 RSS 格式

WeRSS 提供多种 RSS 格式，满足不同阅读器的需求：

| 格式 | 扩展名 | 适用场景 | 示例 |
|------|--------|---------|------|
| **RSS 2.0** | `.rss` `.xml` | 标准 RSS 格式，兼容性最好 | `/feed/{feed_id}.xml` |
| **Atom** | `.atom` | 新一代 RSS 格式，功能更丰富 | `/feed/{feed_id}.atom` |
| **JSON Feed** | `.json` `.jmd` | JSON 格式，便于程序化处理 | `/feed/{feed_id}.json` |
| **Markdown** | `.md` `.txt` | Markdown 格式，适合文本编辑器 | `/feed/{feed_id}.md` |

### RSS 订阅的特点

- ✅ **无需认证**：RSS 订阅接口不需要登录即可访问
- ✅ **全文输出**：可配置是否输出文章完整内容
- ✅ **封面图片**：支持展示公众号和文章封面
- ✅ **自动缓存**：RSS Feed 会自动缓存，提升访问速度
- ✅ **按需更新**：可以强制刷新最新内容
- ✅ **灵活筛选**：支持按公众号、标签、关键词筛选

---

## RSS 订阅地址格式

### 服务器地址

| 环境 | Base URL |
|------|----------|
| 云服务器 | `http://154.8.205.159:8001` |
| 本地访问 | `http://localhost:8001` |

---

### 1. 订阅所有公众号

获取你订阅的所有公众号的聚合 RSS。

```
格式：GET /rss
示例：http://154.8.205.159:8001/rss
```

**查询参数**：

| 参数 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| `limit` | integer | 每页文章数量（1-30） | `10` |
| `offset` | integer | 偏移量 | `0` |

**示例**：

```
# 获取所有公众号的 RSS（最新 20 篇文章）
http://154.8.205.159:8001/rss?limit=20

# 强制更新缓存
http://154.8.205.159:8001/rss/fresh
```

---

### 2. 订阅单个公众号

订阅指定公众号的文章。

```
格式：GET /rss/{feed_id}
示例：http://154.8.205.159:8001/rss/MP_WXS_MzI1MDY3MTkyMw==
```

**路径参数**：

| 参数 | 说明 | 示例 |
|------|------|------|
| `feed_id` | 公众号 ID | `MP_WXS_MzI1MDY3MTkyMw==` |

**查询参数**：

| 参数 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| `limit` | integer | 每页文章数量（1-100） | `10` |
| `offset` | integer | 偏移量 | `0` |

**示例**：

```
# 订阅单个公众号（最新 50 篇）
http://154.8.205.159:8001/rss/MP_WXS_MzI1MDY3MTkyMw==?limit=50

# 强制更新
http://154.8.205.159:8001/rss/MP_WXS_MzI1MDY3MTkyMw==/fresh
```

---

### 3. 订阅指定格式的 RSS

使用不同的格式订阅公众号。

```
格式：GET /feed/{feed_id}.{ext}
示例：http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.xml
```

**支持的格式**：

| 格式 | URL 示例 |
|------|----------|
| RSS 2.0 (XML) | `/feed/{feed_id}.xml` |
| RSS 2.0 (RSS) | `/feed/{feed_id}.rss` |
| Atom | `/feed/{feed_id}.atom` |
| JSON Feed | `/feed/{feed_id}.json` |
| JSON (Markdown) | `/feed/{feed_id}.jmd` |
| Markdown | `/feed/{feed_id}.md` |
| 纯文本 | `/feed/{feed_id}.txt` |

**完整示例**：

```bash
# XML 格式（标准 RSS）
http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.xml

# Atom 格式
http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.atom

# JSON 格式
http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.json

# Markdown 格式
http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.md
```

---

### 4. 订阅标签分组

按标签订阅多个公众号的聚合内容。

```
格式：GET /feed/tag/{tag_id}.{ext}
示例：http://154.8.205.159:8001/feed/tag/tech_news.xml
```

**路径参数**：

| 参数 | 说明 | 示例 |
|------|------|------|
| `tag_id` | 标签 ID | `tech_news` |
| `ext` | 格式扩展名 | `xml`, `atom`, `json` 等 |

**示例**：

```bash
# 订阅"技术类"标签的所有公众号（XML）
http://154.8.205.159:8001/feed/tag/tech_news.xml

# 订阅"技术类"标签的所有公众号（JSON）
http://154.8.205.159:8001/feed/tag/tech_news.json
```

---

### 5. 搜索并订阅

按关键词搜索文章并订阅。

```
格式：GET /feed/search/{keyword}/{feed_id}.{ext}
示例：http://154.8.205.159:8001/feed/search/Python/MP_WXS_xxx.xml
```

**路径参数**：

| 参数 | 说明 | 示例 |
|------|------|------|
| `keyword` | 搜索关键词 | `Python` |
| `feed_id` | 公众号 ID（可选，使用 `all` 表示全部） | `MP_WXS_xxx` 或 `all` |
| `ext` | 格式扩展名 | `xml`, `atom`, `json` 等 |

**示例**：

```bash
# 搜索包含"Python"的文章（所有公众号）
http://154.8.205.159:8001/feed/search/Python/all.xml

# 搜索指定公众号中包含"Python"的文章
http://154.8.205.159:8001/feed/search/Python/MP_WXS_MzI1MDY3MTkyMw==.xml
```

---

### 6. 获取文章内容（HTML 页面）

查看缓存的文章完整内容（HTML 格式）。

```
格式：GET /rss/content/{content_id}
示例：http://154.8.205.159:8001/rss/content/MP_WXS_xxx-2651087878
```

**说明**：
- 文章内容会自动缓存在服务器
- 返回 HTML 页面，可在浏览器中直接查看
- 包含文章标题、来源、发布时间、完整内容

---

## 在各种 RSS 阅读器中订阅

### 推荐的 RSS 阅读器

| 平台 | 阅读器名称 | 特点 | 价格 |
|------|-----------|------|------|
| **跨平台** | [Inoreader](https://www.inoreader.com/) | 功能强大，云同步 | 免费/付费 |
| **跨平台** | [Feedly](https://feedly.com/) | 界面美观，AI 推荐 | 免费/付费 |
| **跨平台** | [The Old Reader](https://theoldreader.com/) | 类似 Google Reader | 免费 |
| **iOS/macOS** | [Reeder](https://reederapp.com/) | 界面简洁，体验极佳 | 付费 |
| **iOS/macOS** | [NetNewsWire](https://netnewswire.com/) | 开源免费 | 免费 |
| **iOS** | [Fiery Feeds](https://cocoacake.net/apps/fiery/) | 功能全面 | 付费 |
| **Android** | [FeedMe](https://play.google.com/store/apps/details?id=com.seazon.feedme) | Material Design | 免费 |
| **Android** | [FocusReader](https://play.google.com/store/apps/details?id=allen.town.focus.reader) | 开源 | 免费 |
| **Windows** | [Fluent Reader](https://hyliu.me/fluent-reader/) | Fluent Design，开源 | 免费 |
| **Linux** | [FreshRSS](https://freshrss.org/) | 自托管 Web 阅读器 | 免费 |
| **浏览器** | [RSS Reader 扩展](https://chrome.google.com/webstore/search/rss%20reader) | Chrome/Firefox | 免费 |

---

### 在 Inoreader 中订阅

**Inoreader** 是功能最强大的 RSS 阅读器之一，支持云同步、全文搜索、过滤规则等。

#### 步骤 1：注册账号

访问 [Inoreader](https://www.inoreader.com/) 并注册账号（可免费使用）。

#### 步骤 2：添加订阅

1. 点击左侧菜单的 **"添加新订阅"** 按钮
2. 在弹出的输入框中粘贴 RSS 订阅地址：
   ```
   http://154.8.205.159:8001/rss/MP_WXS_MzI1MDY3MTkyMw==
   ```
3. 点击 **"订阅"**
4. 选择分类文件夹（可选）

#### 步骤 3：查看文章

- 在左侧订阅列表中找到刚添加的公众号
- 点击即可查看最新文章
- 支持全文阅读、标记已读、加星标等操作

---

### 在 Feedly 中订阅

**Feedly** 是界面最美观的 RSS 阅读器之一，支持 AI 内容推荐。

#### 步骤 1：注册账号

访问 [Feedly](https://feedly.com/) 并注册账号（可免费使用）。

#### 步骤 2：添加订阅

1. 点击左侧的 **"+ Add Content"** 按钮
2. 在搜索框中粘贴 RSS 订阅地址：
   ```
   http://154.8.205.159:8001/rss/MP_WXS_MzI1MDY3MTkyMw==
   ```
3. 点击 **"Follow"**
4. 选择分类（Personal、Work 等）

#### 步骤 3：阅读文章

- 在左侧订阅列表中查看文章
- 支持卡片视图、列表视图、杂志视图

---

### 在 Reeder (iOS/macOS) 中订阅

**Reeder** 是 iOS/macOS 上体验最好的 RSS 阅读器（需付费购买）。

#### 步骤 1：打开 Reeder

启动 Reeder 应用。

#### 步骤 2：添加订阅

1. 点击右上角的 **"+"** 按钮
2. 选择 **"Add Feed"**
3. 粘贴 RSS 订阅地址：
   ```
   http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.xml
   ```
4. 点击 **"Subscribe"**

#### 步骤 3：同步设置（可选）

Reeder 支持与多种云服务同步：
- Feedly
- Inoreader
- FeedBin
- iCloud

---

### 在 NetNewsWire (iOS/macOS) 中订阅

**NetNewsWire** 是免费开源的 RSS 阅读器。

#### 步骤 1：下载安装

- macOS：从 [Mac App Store](https://apps.apple.com/us/app/netnewswire/id1480640210) 下载
- iOS：从 App Store 下载

#### 步骤 2：添加订阅

1. 点击菜单栏 **File → New Web Feed** (或按 `⌘N`)
2. 粘贴 RSS 订阅地址：
   ```
   http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.xml
   ```
3. 选择分类文件夹
4. 点击 **"Add"**

---

### 在 Fluent Reader (Windows) 中订阅

**Fluent Reader** 是 Windows 上界面美观的开源 RSS 阅读器。

#### 步骤 1：下载安装

从 [GitHub Releases](https://github.com/yang991178/fluent-reader/releases) 下载最新版本。

#### 步骤 2：添加订阅

1. 点击左上角的 **"+"** 按钮
2. 选择 **"Add Source"**
3. 粘贴 RSS 订阅地址：
   ```
   http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3GTkyMw==.xml
   ```
4. 点击 **"Fetch"** → **"Confirm"**

---

### 在浏览器中订阅（RSS Reader 扩展）

如果你不想安装独立的 RSS 阅读器，可以使用浏览器扩展。

#### Chrome/Edge 推荐扩展

- [Feedbro](https://chrome.google.com/webstore/detail/feedbro/mefgmmbdailogpfhfblcnnjfmnpnmdfa)
- [RSS Feed Reader](https://chrome.google.com/webstore/detail/rss-feed-reader/pnjaodmkngahhkoihejjehlcdlnohgmp)

#### Firefox 推荐扩展

- [Feedbro](https://addons.mozilla.org/en-US/firefox/addon/feedbroreader/)

#### 使用步骤

1. 安装扩展后，点击浏览器工具栏的 RSS 图标
2. 点击 **"Add Feed"** 或类似按钮
3. 粘贴 RSS 订阅地址并确认

---

## 订阅示例

### 示例 1：订阅"Python之禅"公众号

假设你已经在 WeRSS 中添加了"Python之禅"公众号，其 ID 为 `MP_WXS_MzI1MDY3MTkyMw==`。

#### 获取订阅地址

```bash
# 方式 1：默认 RSS 格式
http://154.8.205.159:8001/rss/MP_WXS_MzI1MDY3MTkyMw==

# 方式 2：指定 XML 格式
http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.xml

# 方式 3：指定 Atom 格式
http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.atom

# 方式 4：指定 JSON 格式
http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.json
```

#### 在 Inoreader 中添加

1. 登录 Inoreader
2. 点击左侧菜单的 **"添加新订阅"**
3. 粘贴订阅地址：
   ```
   http://154.8.205.159:8001/feed/MP_WXS_MzI1MDY3MTkyMw==.xml
   ```
4. 点击 **"订阅"**
5. 完成！现在你可以在 Inoreader 中阅读"Python之禅"的最新文章了

---

### 示例 2：订阅所有公众号

如果你想在一个 RSS Feed 中查看所有订阅的公众号文章：

```bash
# 所有公众号的聚合 RSS
http://154.8.205.159:8001/rss
```

在 RSS 阅读器中添加这个地址，就可以看到所有公众号的最新文章，按时间线排序。

---

### 示例 3：按标签订阅

假设你创建了一个名为"技术类"的标签，ID 为 `tech_news`，并将多个技术公众号添加到这个标签中。

```bash
# 订阅"技术类"标签下的所有公众号
http://154.8.205.159:8001/feed/tag/tech_news.xml
```

这样可以只订阅特定分类的公众号，避免信息过载。

---

### 示例 4：搜索订阅

假设你只想订阅包含"Python"关键词的文章：

```bash
# 搜索所有公众号中包含"Python"的文章
http://154.8.205.159:8001/feed/search/Python/all.xml

# 搜索"Python之禅"中包含"装饰器"的文章
http://154.8.205.159:8001/feed/search/装饰器/MP_WXS_MzI1MDY3MTkyMw==.xml
```

---

## 高级用法

### 1. 配置 RSS 输出选项

WeRSS 支持通过配置文件调整 RSS 输出行为。编辑 `/srv/we-mp-rss/config.yaml`：

```yaml
rss:
  # RSS 域名地址（用于生成链接）
  base_url: http://154.8.205.159:8001/

  # 是否为本地 RSS 链接（true=指向本地缓存，false=直接链接到微信）
  local: false

  # RSS 标题
  title: 我的微信公众号订阅

  # RSS 描述
  description: 使用 WeRSS 订阅微信公众号

  # RSS 封面
  cover: http://154.8.205.159:8001/static/logo.svg

  # 是否显示全文（true=完整文章内容，false=仅摘要）
  full_context: true

  # 是否添加封面图片
  add_cover: true

  # RSS 正文是否启用 CDATA
  cdata: false

  # RSS 分页大小（默认每次返回多少篇文章）
  page_size: 30
```

**配置说明**：

| 配置项 | 说明 | 推荐值 |
|--------|------|--------|
| `full_context` | 是否输出完整文章内容 | `true`（全文阅读） |
| `add_cover` | 是否包含封面图片 | `true`（更美观） |
| `local` | 文章链接指向本地还是微信 | `false`（直接跳转微信） |
| `page_size` | 每次返回的文章数量 | `30`（平衡性能和内容） |

修改配置后需要重启 WeRSS 服务：

```bash
sudo systemctl restart we-mp-rss
```

---

### 2. 使用 OPML 批量导入订阅

如果你有多个公众号要订阅，可以生成 OPML 文件批量导入到 RSS 阅读器。

#### 步骤 1：获取所有公众号列表

```bash
# 登录获取 Token
TOKEN=$(curl -X POST "http://154.8.205.159:8001/api/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin@123" | jq -r '.access_token')

# 获取公众号列表
curl -X GET "http://154.8.205.159:8001/api/mps?limit=100" \
  -H "Authorization: Bearer $TOKEN" | jq '.data.list'
```

#### 步骤 2：生成 OPML 文件

创建一个 Python 脚本 `generate_opml.py`：

```python
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# 登录获取 Token
login_url = "http://154.8.205.159:8001/api/auth/token"
data = {"username": "admin", "password": "admin@123"}
response = requests.post(login_url, data=data)
token = response.json()["access_token"]

# 获取公众号列表
mps_url = "http://154.8.205.159:8001/api/mps?limit=100"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(mps_url, headers=headers)
feeds = response.json()["data"]["list"]

# 创建 OPML
opml = ET.Element("opml", version="1.0")
head = ET.SubElement(opml, "head")
ET.SubElement(head, "title").text = "WeRSS 订阅列表"
ET.SubElement(head, "dateCreated").text = datetime.now().isoformat()

body = ET.SubElement(opml, "body")

# 添加每个公众号
for feed in feeds:
    feed_url = f"http://154.8.205.159:8001/feed/{feed['id']}.xml"
    ET.SubElement(body, "outline", {
        "type": "rss",
        "text": feed["mp_name"],
        "title": feed["mp_name"],
        "xmlUrl": feed_url,
        "htmlUrl": feed_url
    })

# 保存 OPML 文件
tree = ET.ElementTree(opml)
tree.write("werss_subscriptions.opml", encoding="utf-8", xml_declaration=True)
print("✅ OPML 文件已生成：werss_subscriptions.opml")
```

运行脚本：

```bash
python generate_opml.py
```

#### 步骤 3：导入到 RSS 阅读器

大部分 RSS 阅读器都支持导入 OPML 文件：

- **Inoreader**: Settings → Import/Export → Import from OPML file
- **Feedly**: Settings → Import/Export → Import OPML
- **NetNewsWire**: File → Import Subscriptions
- **Fluent Reader**: Settings → Import/Export → Import OPML

---

### 3. 定期刷新 RSS Feed

RSS Feed 默认会缓存一段时间。如果你想立即获取最新文章，可以使用 `/fresh` 路径：

```bash
# 刷新所有公众号的 RSS
http://154.8.205.159:8001/rss/fresh

# 刷新单个公众号的 RSS
http://154.8.205.159:8001/rss/MP_WXS_MzI1MDY3MTkyMw==/fresh
```

---

### 4. 自建 RSS 聚合服务（可选）

如果你希望在公网访问 RSS，但不想直接暴露 WeRSS 服务器，可以使用 FreshRSS、Tiny Tiny RSS 等自托管 RSS 聚合服务作为中间层。

#### 使用 FreshRSS

1. 在你的服务器上安装 FreshRSS：
   ```bash
   docker run -d --name freshrss \
     -p 8080:80 \
     -v freshrss_data:/var/www/FreshRSS/data \
     freshrss/freshrss
   ```

2. 访问 `http://your-server:8080` 完成初始化

3. 在 FreshRSS 中添加 WeRSS 的 RSS 订阅地址（内网）：
   ```
   http://154.8.205.159:8001/rss
   ```

4. 通过 FreshRSS 的公网地址订阅

---

### 5. 使用 RSS to Email

如果你更喜欢通过邮件阅读文章，可以使用 RSS to Email 服务：

- [Blogtrottr](https://blogtrottr.com/)
- [FeedRabbit](https://feedrabbit.com/)
- [Kill the Newsletter](https://kill-the-newsletter.com/)

将 WeRSS 的 RSS 订阅地址添加到这些服务，它们会定期将新文章发送到你的邮箱。

---

## 常见问题

### Q1: RSS 订阅需要登录吗？

**不需要**。WeRSS 的 RSS 订阅接口（`/rss` 和 `/feed`）不需要认证，可以直接访问。这与 API 接口不同，API 接口需要 Bearer Token 认证。

---

### Q2: RSS Feed 多久更新一次？

WeRSS 的定时任务会定期抓取公众号的最新文章（默认间隔可在 `config.yaml` 中配置）。RSS Feed 会自动缓存，缓存时间默认为 1 小时。

如果你想立即获取最新内容，可以使用 `/fresh` 路径强制刷新：

```
http://154.8.205.159:8001/rss/MP_WXS_xxx/fresh
```

---

### Q3: RSS Feed 中的文章是全文还是摘要?

这取决于 `config.yaml` 中的 `rss.full_context` 配置：

- `full_context: true`：输出完整文章内容（推荐）
- `full_context: false`：仅输出摘要

修改配置后需要重启服务。

---

### Q4: 如何在公网访问 RSS 订阅？

目前 WeRSS 部署在云服务器 `154.8.205.159:8001`，已经可以在公网访问。

如果你担心安全问题，可以：

1. **配置防火墙**：仅允许特定 IP 访问
2. **使用反向代理**：通过 Nginx 添加基础认证
3. **使用 VPN**：通过 VPN 连接到服务器内网
4. **使用 FreshRSS**：在中间层添加认证

---

### Q5: 如何知道公众号的 `feed_id`？

有几种方式获取公众号的 `feed_id`：

#### 方式 1：通过 API 查询

```bash
# 登录获取 Token
TOKEN=$(curl -X POST "http://154.8.205.159:8001/api/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin@123" | jq -r '.access_token')

# 获取公众号列表
curl -X GET "http://154.8.205.159:8001/api/mps?limit=100" \
  -H "Authorization: Bearer $TOKEN" | jq '.data.list[] | {mp_name, id}'
```

输出示例：

```json
{
  "mp_name": "Python之禅",
  "id": "MP_WXS_MzI1MDY3MTkyMw=="
}
```

#### 方式 2：登录 Web 界面查看

1. 访问 `http://154.8.205.159:8001`
2. 登录后进入"公众号管理"
3. 在公众号列表中可以看到每个公众号的 ID

#### 方式 3：直接访问聚合 RSS

如果你不需要订阅单个公众号，可以直接使用：

```
http://154.8.205.159:8001/rss
```

这个地址会聚合所有订阅的公众号。

---

### Q6: RSS 阅读器显示图片加载失败怎么办？

WeRSS 默认会将微信的图片链接转换为本地代理链接（通过 `/static/res/logo/` 前缀）。

如果图片加载失败，可能是：

1. **网络问题**：微信的图片服务器可能被你的网络屏蔽
2. **缓存问题**：清除 RSS 阅读器的缓存重试

**解决方案**：

编辑 `config.yaml`，将图片链接改为直接访问微信服务器：

```yaml
rss:
  local: false  # 不使用本地代理
```

重启服务后，图片链接会直接指向微信 CDN。

---

### Q7: 如何在 RSS 中只显示特定日期的文章？

目前 RSS 接口不直接支持按日期筛选，但你可以：

1. **使用 API 接口**：通过 API 按日期查询（见 `SQL_API.md` 文档）
2. **使用 RSS 阅读器的过滤功能**：大部分高级 RSS 阅读器（如 Inoreader）支持按日期过滤
3. **调整 `limit` 参数**：获取更多历史文章

示例：

```
# 获取最新 100 篇文章
http://154.8.205.159:8001/rss/MP_WXS_xxx?limit=100
```

---

### Q8: 支持播客（Podcast）格式的 RSS 吗？

目前 WeRSS 主要支持文章类 RSS，不支持播客格式（需要 `<enclosure>` 标签包含音频文件）。

如果公众号文章中包含音频，可能需要自定义模板来提取音频链接。

---

### Q9: RSS Feed 中的链接指向哪里？

这取决于 `config.yaml` 中的 `rss.local` 配置：

- `local: true`：链接指向本地缓存 (`/rss/content/{article_id}`)
- `local: false`：链接直接指向微信公众号原文

**推荐设置**：

```yaml
rss:
  local: false  # 直接跳转到微信原文，方便分享和查看完整排版
```

---

### Q10: 如何备份 RSS 订阅列表？

大部分 RSS 阅读器支持导出 OPML 格式的订阅列表：

- **Inoreader**: Settings → Import/Export → Export to OPML file
- **Feedly**: Settings → Import/Export → Export OPML
- **NetNewsWire**: File → Export Subscriptions

定期导出备份，以防数据丢失。

---

## 总结

### RSS 订阅的优势

使用 WeRSS 的 RSS 订阅功能，你可以：

- ✅ 在 RSS 阅读器中统一管理所有公众号
- ✅ 跨平台阅读（PC、Mac、手机、平板）
- ✅ 按时间线聚合所有订阅内容
- ✅ 离线缓存，随时阅读
- ✅ 搜索、标记、分类文章
- ✅ 无广告、无干扰
- ✅ 导出文章存档

### 快速开始

1. **获取公众号 ID**：
   ```bash
   # 登录 Web 界面查看，或通过 API 查询
   http://154.8.205.159:8001
   ```

2. **复制 RSS 订阅地址**：
   ```
   http://154.8.205.159:8001/feed/{feed_id}.xml
   ```

3. **添加到 RSS 阅读器**：
   - 推荐：Inoreader、Feedly、Reeder、NetNewsWire

4. **开始阅读**！

### 进一步了解

- **API 接口文档**：`SQL_API.md`（程序化访问数据）
- **部署文档**：`RUNBOOK.zh-CN.md`（运维和部署）
- **项目官网**：[https://github.com/rachelos/we-mp-rss](https://github.com/rachelos/we-mp-rss)

---

**文档版本**: 1.0
**最后更新**: 2026-01-08
