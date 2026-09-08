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
- 首页 `index.html`；产品总览 `products.html`（12 款分类 + 前端筛选）
- 产品详情 `products/`：backpack / handbag-tote / crossbody-sling / travel-trolley / laptop-briefcase / duffel-weekender
- 公司页：`about.html`、`factory-tour.html`、`certifications.html`、`industries.html`
- 转化页：`quote.html`（询盘表单）、`contact.html`；博客 `blog.html` + `blog/` 两篇文章；`404.html`
- 资产：`assets/css/style.css`（设计系统）、`assets/js/main.js`（导航/筛选/FAQ/表单）、`assets/svg/`（全部自绘矢量插画）

## 待替换占位信息
- 邮箱/域名：`sales@velorabags.com`（可在各页页脚与表单 `data-mailto` 中替换）
- WhatsApp：`+86 138 0000 0000`（`wa.me/8613800000000`）
- 地址：广州花都区狮岭镇华胜路 8 号（占位）
- 认证编号、报价、MOQ（300/500/1000 pcs）、交期等均为可编辑示例
- 产品图为自绘 SVG 占位：将 `assets/svg/*.svg` 同路径替换为实拍图即可，尺寸比例参考 `480x440`

## 定制说明
- 配色与字体：`assets/css/style.css` 顶部 `:root` 变量（咖啡棕/驼色/奶油色）
- 表单为 `mailto:` 方案：点击提交会打开本机邮件客户端并预填内容；接后端后把 `data-mailto` 表单改为表单接口即可
- 全站无外链字体/CDN，离线可完整运行
