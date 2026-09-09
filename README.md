# Velora Bags — 箱包独立站（Custom Bag & Luggage Manufacturer Site）

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
- 首页 `index.html`（含环保袋品类区块 Sustainable Totes & Packaging）；产品总览 `products.html`（16 款产品卡 + 前端筛选）
- 产品详情 `products/`：主包袋 6 款（backpack / handbag-tote / crossbody-sling / travel-trolley / laptop-briefcase / duffel-weekender）+ 环保袋 4 款（jute-bags / canvas-bags / non-woven-bags / woven-pp-bags）
- 公司页：`about.html`、`factory-tour.html`、`certifications.html`、`industries.html`
- 转化页：`quote.html`（询盘表单）、`contact.html`；博客 `blog.html` + `blog/` 四篇文章（backpack-materials-guide / qc-checklist / eco-bag-material-guide / eco-bag-printing-qc）；`404.html`
- 内部资料：`research/`（环保袋/编织袋竞品调研，本地参考用；已由 `.gitignore` 排除，不进公开仓库）
- 资产：`assets/css/style.css`（设计系统）、`assets/js/main.js`（导航/筛选/FAQ/表单）、`assets/svg/`（全部自绘矢量插画）

## 上线配置（2026-09-09 已更新）
- 目标域名：`verlorabags.com`（GitHub → Cloudflare Pages 自动部署）
- 询盘邮箱：`evan.funkytek@gmail.com`（全站替换原占位 sales@velorabags.com，含表单 data-mailto）
- WhatsApp：`+86 137 9827 5895`（`wa.me/8613798275895`）
- 地址：No. 8 Huasheng Rd, Shiling, Huadu District, Guangzhou, China
- 联系方式：主询盘 `evan.funkytek@gmail.com`（页脚/表单/全站 mailto）；售后支持 `Support@velorabags.com`（contact.html 展示卡）
- 产品图：六大主类目已启用 `assets/img/*.jpg`（AI 生成风格化产品示意，统一暖奶油底、无品牌标识）；拿到自家产品实拍图后可直接同路径替换
- SEO：`sitemap.xml`（23 URL，www 为规范域）+ `robots.txt` 已随仓库部署；认证编号、报价、MOQ（300/500/1000 pcs）、交期仍为可编辑示例数据

## 定制说明
- 配色与字体：`assets/css/style.css` 顶部 `:root` 变量（咖啡棕/驼色/奶油色）
- 表单为 `mailto:` 方案：点击提交会打开本机邮件客户端并预填内容；接后端后把 `data-mailto` 表单改为表单接口即可
- 全站无外链字体/CDN，离线可完整运行
