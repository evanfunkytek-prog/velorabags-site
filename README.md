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
