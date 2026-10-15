# Verlora Bags — 箱包独立站（Custom Bag & Luggage Manufacturer Site）

> ⚠️ **先认清你在改哪个站：本目录 = Verlora Bags，改动只会发到 https://www.verlorabags.com。**
> 如果你手上是 **EliteBox Packaging** 的工单（目标站点 `https://www.eliteboxpacking.com`），**不要在这里动手**——它的部署源是
> `C:\Users\Administrator\AccioWork\2026-09-03-08-22-04-529-aa57469b\elitebox-content\deploy\sitebundle`，由 **Accio 直传**上线，
> 与本仓库、GitHub、Cloudflare 自动构建全都无关。反之，本目录的 `git push` 也永远不会影响 eliteboxpacking.com。详细对照见下方「目录归属」。

纯静态、无框架、无外部依赖的 **箱包 OEM/ODM 工厂独立站**（英文，面向欧美 B2B 买家）。
结构参考相邻项目 `独立站项目`（目前结构最完善的制造型独立站），配色/文案/图形均为全新设计。

## 目录归属（2026-10-13 拆分 / 剥离；物理外移已于 2026-10-15 完成）

本目录**只包含 Verlora Bags 项目**。EliteBox Packaging（包装盒站）已在 2026-10-13 从本仓库的部署链、凭证与文档里彻底剥离；**物理外移**已于 2026-10-15 核实完成：本目录下不再有 `EliteBox-Packaging\`，它现在是同级独立文件夹 `C:\Users\Administrator\Documents\ChatGPT\EliteBox-Packaging`（自带独立 git 仓库）。此后文件、脚本、凭证、git 仓库全部分开，互不扫描、互不部署，不会再出现一边的构建/部署脚本动到另一边站点的交叉感染。（`.gitignore` 里仍保留 `EliteBox-Packaging/` 排除项，防止它被重新放回本仓库。）

| | 本项目 | 另一个项目 |
| --- | --- | --- |
| 项目 | Verlora Bags（箱包 OEM/ODM） | EliteBox Packaging（包装盒） |
| 目录 | `C:\Users\Administrator\Documents\ChatGPT\箱包独立站项目`（本目录，即仓库根） | `C:\Users\Administrator\Documents\ChatGPT\EliteBox-Packaging`（同级独立目录，外移已完成） |
| 线上站点 | https://www.verlorabags.com | https://www.eliteboxpacking.com |
| Cloudflare Pages 项目 | `velorabags-site`（Git 自动构建） | `eliteboxpacking`（直传，无 Git 连接） |
| 部署方式 | 推送到 GitHub 后由 Cloudflare Pages 自动构建 | **Accio** 从 `C:\Users\Administrator\AccioWork\2026-09-03-08-22-04-529-aa57469b\elitebox-content\deploy\` 执行 wrangler 直传 |
| 说明文档 | 本文件 | `...\EliteBox-Packaging\README.md` |

> ⚠️ 本目录是 git 仓库根目录，同时也是 GitHub 自动部署的站点根目录。**不要**把站点文件挪进子目录，否则线上构建会直接失效。
> ⚠️ 本项目**只管 verlorabags.com**。任何与 eliteboxpacking 有关的部署动作，都不允许在本目录执行。

## 快速开始
1. 直接双击打开 `index.html`，或
2. 本地预览（推荐）：
```powershell
python -m http.server 8000
# 浏览器打开 http://127.0.0.1:8000/
```
3. 上线：把整个文件夹上传到任意静态托管（nginx / 对象存储 / GitHub Pages）。

## 页面结构
线上由 Cloudflare Pages 托管，内部链接、canonical 与 sitemap 统一使用无后缀地址（clean URL）；括号内为对应的源文件。
- 首页 `/`（源文件 `index.html`，含环保袋品类区块 Sustainable Totes & Packaging）；产品总览 `/products`（源文件 `products.html`，20 款产品卡 + 前端筛选）
- 产品详情 `products/`：共 42 个详情页（18 个品类页 + 24 个单品页），线上地址 `/products/<slug>`，全部互链、无孤岛
- 公司页：`/about`、`/factory-tour`、`/certifications`、`/industries`（源文件为同名 `.html`）
- 转化页：`/quote`（询盘表单）、`/contact`；法务页 `/privacy`、`/terms`（页脚全站可点）；错误页 `/404.html`（源文件 `404.html`）
- 错误页链接约定：`404.html` 会被 Cloudflare Pages 用于**任意**不存在的路径，因此页内链接一律写根绝对路径（`/`、`/products`）。若写成相对路径，访问 `/products/xxx` 时浏览器会按 `/products/` 目录解析，样式表与导航会全部失效。
- 博客：`/blog` + `blog/` 七篇文章（how-to-choose-bag-fabrics / bag-factory-qc-checklist / eco-reusable-bag-trends-2026 / eco-bag-material-guide / eco-bag-printing-qc / qc-checklist / backpack-materials-guide），七篇均已挂在博客列表页
- 内部资料：`research/`（环保袋/编织袋竞品调研，本地参考用；已由 `.gitignore` 排除，不进公开仓库）
- 资产：`assets/css/style.css`（设计系统）、`assets/js/main.js`（导航/筛选/FAQ/表单）、`assets/svg/`（全部自绘矢量插画）
- 后端函数：`functions/api/quote.js`（Cloudflare Pages Function，接收询盘表单 POST）
- 边缘防护：`functions/_middleware.js`（Cloudflare Pages 中间件，过滤「中文界面 + 海外 IP」访客，默认只观察不拦，见下文「访问防护」）

## 上线配置（2026-09-11 已更新）
- 目标域名：`verlorabags.com`（GitHub → Cloudflare Pages 自动部署）
- 规范域名：全站 canonical / og:url / 结构化数据 / sitemap / robots 统一为 `https://www.verlorabags.com`
  （此前误写为 `velorabags.com`，该域名的 www 主机不存在，会把收录指向无效地址）
- 询盘邮箱：`evan.funkytek@gmail.com`（全站 mailto 兜底地址）
- WhatsApp：`+86 137 9827 5895`（`wa.me/8613798275895`）
- 地址：No. 8 Huasheng Rd, Shiling, Huadu District, Guangzhou, China
- 联系方式：主询盘 `evan.funkytek@gmail.com`（页脚/表单/全站 mailto）；售后支持 `support@verlorabags.com`（contact.html 展示卡）
- 产品图：主类目使用 `assets/img/*.webp`（AI 生成风格化产品示意，统一暖奶油底、无品牌标识）；拿到自家产品实拍图后可直接同路径替换
- SEO：`sitemap.xml`（68 URL，www 为规范域，只收录本仓库实际存在的页面）+ `robots.txt` 已随仓库部署；认证编号、报价、MOQ（300 pcs/款/配色）、交期仍为可编辑示例数据

## 询盘表单后端（新增）
表单提交后先 POST 到 `/api/quote`（`functions/api/quote.js`）。**接口未配置或调用失败时，自动回退为原来的 `mailto:` 方案，线索不会丢。**

在 Cloudflare Pages → Settings → Environment variables 里配置**任意一项**即可开始收信：

- `RESEND_API_KEY` + `LEAD_TO`：通过 Resend 发邮件（可选 `LEAD_FROM` 指定已验证发件人）
- `LEAD_WEBHOOK_URL`：把线索 JSON 转发到 Zapier / Make / n8n / 飞书等 webhook

未配置时接口返回 503，前端自动改走邮件客户端。表单还带蜜罐字段 `_gotcha` 防垃圾提交，并在页面上给出成功/失败提示。

### 生产环境当前配置（2026-10-13 已接上 Resend）
线上**已经配好**收信渠道：访客提交表单后，由 Resend 以本站域名把线索发到下面这个邮箱，访客本人不需要做任何事。

| Cloudflare 环境变量（Production） | 值 | 类型 |
| --- | --- | --- |
| `RESEND_API_KEY` | Resend 的 Sending access key（只存在 Cloudflare 里，不进仓库） | Secret |
| `LEAD_TO` | `evan.funkytek@gmail.com` | Text |
| `LEAD_FROM` | `Verlora Bags Website <quotes@verlorabags.com>` | Text |

- 发件域名 `verlorabags.com` 已在 Resend 验证：DKIM 的 TXT `resend._domainkey`，加上 SPF 的两条 CNAME `send` / `rsend`，都加在 Cloudflare DNS 里，代理状态必须保持 **DNS only（灰云）**。
- 接口已把 `reply_to` 设为访客填写的邮箱，所以收到线索后在 Gmail 直接点「回复」就是回客户本人，不用手动复制地址。
- `quotes@verlorabags.com` 不需要真实存在，Resend 是以本站域名代发。

自检（期望返回 `{"ok":true,"delivered":"email"}`）：

```powershell
'{"fields":{"Company":"readme self-test","Email":"you@example.com"}}' | Set-Content -Path "$env:TEMP\lead.json" -Encoding ascii
curl.exe -sS -X POST -H "Content-Type: application/json" --data-binary "@$env:TEMP\lead.json" https://www.verlorabags.com/api/quote
```

也可以直接在 https://www.verlorabags.com/quote 真填一次表单做端到端确认（用另一个邮箱最好，能顺便验证回复地址）。

返回码含义：`200` 已投递；`400 Missing contact details` 是 `Company` 与 `Email` 都没填；`502` 多半是 Resend 侧拒收（发件域名没验证好，或 `LEAD_FROM` 用了非本站域名）；`503` 是变量没生效——**环境变量只对保存之后新建的部署生效，改完必须去 Deployments 重新部署一次**。

## 访问防护：屏蔽「中文界面 + 海外 IP」访客（2026-09-12 新增）
**结论：Wordfence 用不上，也不需要。** Wordfence 是 WordPress 插件，本站是纯静态站 + Cloudflare Pages，没有 PHP/数据库，装不了；而且静态站的"扒站"防护本来就不该在应用层做。用 Cloudflare 免费版能力就能实现同样的效果，有两条路：

### 方式 A：Cloudflare 面板零代码（免费版可用）
进入 `Security → WAF → Custom rules → Create rule`，自定义表达式填：

```
(ip.geoip.country ne "CN" and http.request.headers["accept-language"] contains "zh" and http.request.headers["sec-fetch-dest"] eq "document")
```

- 动作优先选 **Managed Challenge**（弹一次校验，真人能过、脚本过不去）；确认真要硬拦再改成 **Block**。
- `sec-fetch-dest eq "document"` 是为了只筛"打开网页"的请求，图片/CSS/JS 和 `/api/quote` 询盘接口不受影响。
- 免费版自定义规则条数有限（约 5 条），这个场景 1 条就够。
- 注意：面板规则只对**已接入 Cloudflare 的自定义域名**（`www.verlorabags.com`）生效，对 `*.pages.dev` 预览域名不生效。

### 方式 B：仓库内中间件（已实现，推荐先用它观察）
`functions/_middleware.js` 已随仓库就位，Cloudflare Pages 会自动加载它（和 `functions/api/quote.js` 同一套机制，无需额外配置），预览域名也生效，改规则就是改代码、可版本管理。

当前默认 `MODE = "observe"`：**不拦任何人**，只做两件事——给命中请求加一个 `X-Ver-Filter: observe:zh-language-overseas` 响应头，并往 Pages 实时日志打一行 JSON（国家 / 语言 / 路径 / IP / UA）。先跑一两周看真实数据，再决定要不要打击。

```powershell
# 看实时日志（需要 wrangler，npx wrangler pages deployment tail）
```

确认数据后把文件顶部 `const MODE = "observe"` 改成 `"block"` 即开始返回 403。

自测一眼（命中时返回头里会出现 `x-ver-filter`，普通英文访客没有这个头）：

```powershell
curl.exe -sI -H "Accept-Language: zh-CN,zh;q=0.9" https://www.verlorabags.com/
curl.exe -sI -H "Accept-Language: en-US,en;q=0.9" https://www.verlorabags.com/
```

可调参数（都在 `functions/_middleware.js` 顶部）：

| 参数 | 默认 | 说明 |
| --- | --- | --- |
| `MODE` | `"observe"` | `observe` 只记录，`block` 返回 403 |
| `LANGUAGE_MATCH` | `"primary"` | `primary` 只认浏览器首选语言（误伤最少）；`any` 只要 Accept-Language 里出现 zh 就算，命中更多也更容易误伤 |
| `HOME_COUNTRIES` | `["CN"]` | 这些国家的访客永不打标；想连境内一起拦就清空成 `[]` |
| `EXEMPT_PATHS` | `/api/*`、`/.well-known/*` | 永不拦的路径 |
| `LANGUAGE_PREFIXES` | `["zh"]` | 覆盖 `zh-CN` / `zh-TW` / `zh-HK` / `zh-Hans` 等全部中文变体 |

已内置的兜底：搜索引擎爬虫（Googlebot / Bingbot / Yandex / Baidu / Applebot 等）一律放行；只筛 HTML 页面浏览，图片/JS/CSS 和询盘接口一律放行；解析异常时直接放行，不会把站点搞挂。

### 必须先知道的三个风险
1. **对真爬虫几乎无效。** `Accept-Language` 是客户端自己报的，curl / wget / HTTrack / Playwright 默认根本不带 `zh`。会命中这条规则的绝大部分是**真人**——扒站者只要把浏览器语言改回英文就绕过了。所以它的定位是"降低被顺手抄袭的概率"，不是安全边界。
2. **命中最多的很可能是你最想要的客户。** 海外华人开的贸易公司、采购代理、中间商，浏览器常年是中文界面但人在美国/加拿大/澳洲/欧洲——他们正是这个站最优质的询盘来源。这也是为什么建议用 **Managed Challenge 而不是 Block**，并在观察模式下先看清命中量。
3. **别把 SEO 一起拦掉。** 中间件已放行主流搜索引擎爬虫，但如果你走方式 A 自己写规则，务必保留爬虫放行，否则 Google 抓取会受影响。

### 想真正防扒站，更有效的是这几招（都免费）
- Cloudflare **Bot Fight Mode**（免费，自动挑战可疑自动化流量）+ 免费版 1 条 **Rate limiting** 规则限制同 IP 高频抓取。
- 屏蔽云厂商 ASN（AWS / Hetzner / DigitalOcean 等）——采集器大多跑在这些机器上，真人不会。
- 图片加水印/EXIF 归属、产品文案埋不可见指纹词，出现抄袭时可反查来源。
- `robots.txt` 声明禁止抓取（对恶意方无强制力，但对 GPTBot 等合规爬虫有效）+ 抄袭站点走 Google DMCA 下架。

## 资产体积
- 6 张曾被引用的大图已转 WebP：factory-hero / niche-pets / duffel / tote / backpack / trolley，**9.6 MB → 0.49 MB**
- 旧 `.jpg` 文件仍留在仓库中但已不再被任何页面引用；`python tools/build.py package` 打包时只复制被引用的资源，因此不会进部署包

## 定制说明
- 配色与字体：`assets/css/style.css` 顶部 `:root` 变量（咖啡棕/驼色/奶油色）
- 表单接口地址写在表单的 `data-endpoint` 上（默认 `/api/quote`）；删掉该属性即回到纯 `mailto:` 模式
- 订单/审核用邮箱、地址等站点级信息集中在 `tools/content.py` 顶部（`SITE` / `EMAIL` / `PHONE` / `WA` / `ADDRESS`）
- 站长验证与统计：`tools/content.py` 顶部的 `GSC_VERIFICATION`（Google Search Console）、`BING_VERIFICATION`（Bing 站长）、`GA4_ID`（Google Analytics）**默认留空**，避免把占位标签发布上线；拿到真值后填入，再运行 `python tools/build.py chrome` 重建全部页面头部。
- 博客文章的 `datePublished` 取自 `tools/content.py` 的 `BLOG_DATES`，可直接改成真实发布日
- 重新生成页面外壳与 SEO 文件：`python tools/build.py chrome`（重写 head/页头/页脚）、`python tools/build.py seo`（sitemap + robots）
- 全站无外链字体/CDN，离线可完整运行
