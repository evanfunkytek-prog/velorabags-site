# Verlora Bags — 箱包独立站（Custom Bag & Luggage Manufacturer Site）

纯静态、无框架、无外部依赖的 **箱包 OEM/ODM 工厂独立站**（英文，面向欧美 B2B 买家）。
结构参考相邻项目 `独立站项目`（目前结构最完善的制造型独立站），配色/文案/图形均为全新设计。

## 快速开始
1. 直接双击打开 `index.html`，或
2. 本地预览（推荐）：
```powershell
python -m http.server 8000
# 浏览器打开 http://127.0.0.1:8000/
```
3. 上线：把整个文件夹上传到任意静态托管（nginx / 对象存储 / GitHub Pages）。

## 页面结构
- 首页 `index.html`（含环保袋品类区块 Sustainable Totes & Packaging）；产品总览 `products.html`（20 款产品卡 + 前端筛选）
- 产品详情 `products/`：共 42 个详情页（18 个品类页 + 24 个单品页），全部互链、无孤岛
- 公司页：`about.html`、`factory-tour.html`、`certifications.html`、`industries.html`
- 转化页：`quote.html`（询盘表单）、`contact.html`；法务页 `privacy.html`、`terms.html`（页脚全站可点）；`404.html`
- 博客：`blog.html` + `blog/` 七篇文章（how-to-choose-bag-fabrics / bag-factory-qc-checklist / eco-reusable-bag-trends-2026 / eco-bag-material-guide / eco-bag-printing-qc / qc-checklist / backpack-materials-guide），七篇均已挂在博客列表页
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
- SEO：`sitemap.xml`（60 URL，www 为规范域）+ `robots.txt` 已随仓库部署；认证编号、报价、MOQ（300 pcs/款/配色）、交期仍为可编辑示例数据

## 询盘表单后端（新增）
表单提交后先 POST 到 `/api/quote`（`functions/api/quote.js`）。**接口未配置或调用失败时，自动回退为原来的 `mailto:` 方案，线索不会丢。**

在 Cloudflare Pages → Settings → Environment variables 里配置**任意一项**即可开始收信：

- `RESEND_API_KEY` + `LEAD_TO`：通过 Resend 发邮件（可选 `LEAD_FROM` 指定已验证发件人）
- `LEAD_WEBHOOK_URL`：把线索 JSON 转发到 Zapier / Make / n8n / 飞书等 webhook

未配置时接口返回 503，前端自动改走邮件客户端。表单还带蜜罐字段 `_gotcha` 防垃圾提交，并在页面上给出成功/失败提示。

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
- 博客文章的 `datePublished` 取自 `tools/content.py` 的 `BLOG_DATES`，可直接改成真实发布日
- 重新生成页面外壳与 SEO 文件：`python tools/build.py chrome`（重写 head/页头/页脚）、`python tools/build.py seo`（sitemap + robots）
- 全站无外链字体/CDN，离线可完整运行
