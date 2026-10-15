# Verlora Bags — 工作约定

给在本仓库里动手的人（和 AI）的硬性规则。目标是：站点轻、引用不断、不浪费上下文预算。

## 仓库与上线

- 仓库根目录 = 站点根目录。**任何文件都不能再嵌套一层**（那是过去出过的事故）。
- 上线方式：`git push origin main` → Cloudflare Pages 项目 `verlorabags-site` 自动拉取部署（约 1–2 分钟）。
- 本地普通提交不会上线，只有 push 才会。

## 硬性规则

1. **图片**
   - 只用 WebP；单张 ≤300 KB；`assets/img/` 整体 ≤12 MB。
   - 新增图片前先 `rg` 搜一遍，确认没有同用途的现成图，别重复上传。
   - 替换或停用图片后，**在同一次提交里删掉旧文件**，不要留在目录里当死重。
   - 不要重新压缩已经压好的 WebP：实测只省约 5%，画质反而受损。
2. **推送前必须跑** `python tools/build.py verify`
   - ERROR = 页面引用了不存在的文件，必须修掉再推。
   - WARN = 没人引用的死图 / 超过 300 KB 的大文件，推之前先看一眼。
3. **不要整文件读大文件**（几十 KB 以上的 HTML、日志、JSON）。先用 `rg` 定位到行号，再只读需要的片段。全站文本合计约 2.3 MB，整读会瞬间吃掉上下文预算。
4. **目视校对图片和 PDF 一律用拼版小图，禁止逐页导出大图。**
   - PDF：`python .wrangler\_工单PDF\_sheet.py <pdf> <out.png> [缩略图宽=240] [列数=5]`，一次输出**一张**约 1200×700 的小图，看这一张就够。
   - 旧的逐页模式（10 页 = 10 张 1012×1432 大图 ≈ 3.5 MB）是上下文爆掉的主因，`_render.py` 已改成转发到 `_sheet.py`。
   - 单张图片也先缩到 ≤256 px 再看。
   - 这两个脚本在 `.wrangler/`，是本地工具，不随仓库分发。
5. **生成工单 PDF**：`python .wrangler\_工单PDF\md2pdf.py <输入.md> <输出.pdf> [--doc-id ...] [--doc-type ...]`，排版校验按第 4 条。
6. **整站重建**（`python tools/build.py all`）会重写全部页面。只在确实需要时跑，否则会产生巨量 diff。

## 目录约定

| 路径 | 用途 |
| --- | --- |
| `assets/img/` | 站点图片（根目录放首屏/分类图，`p/` 放产品图） |
| `assets/css/`、`assets/js/` | 由 `tools/build.py` 生成，改样式请改 `tools/templates.py` 或 `tools/base-design-system.css` |
| `products/`、`markets/`、`blog/` | 页面 |
| `tools/` | 构建与校验脚本（不是站点内容，不会上线） |
| `.wrangler/` | 本地临时脚本、备份、工单。**已 gitignore，不要提交。** |

## 提交信息

用约定式前缀：`fix(seo):`、`feat(products):`、`perf(img):`、`docs(readme):` —— 参考 `git log --oneline` 里的既有风格。
