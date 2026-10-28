# 徐安察的个人主页

站点基于 [Hugo](https://gohugo.io/) 与 [hugo-coder](https://github.com/luizdepra/hugo-coder) 主题，默认中文，英文在 `/en/`。在线地址：[www.xu-ancha.com](https://www.xu-ancha.com/)。

## 编辑内容

| 页面 | 中文 | 英文 |
| --- | --- | --- |
| 首页信息（姓名、头衔、社交链接） | `hugo.toml` 中 `[languages.zh-cn]` | `hugo.toml` 中 `[languages.en]` |
| 简介 | [`content/zh/about.md`](content/zh/about.md) | [`content/en/about.md`](content/en/about.md) |
| 论文 | [`content/zh/publications.md`](content/zh/publications.md) | [`content/en/publications.md`](content/en/publications.md) |
| 团队 | [`content/zh/team.md`](content/zh/team.md) | [`content/en/team.md`](content/en/team.md) |
| 教学 | [`content/zh/teaching.md`](content/zh/teaching.md) | [`content/en/teaching.md`](content/en/teaching.md) |
| 数据集 | [`content/zh/datasets.md`](content/zh/datasets.md) | [`content/en/datasets.md`](content/en/datasets.md) |
| 新闻 | [`content/zh/news.md`](content/zh/news.md) | [`content/en/news.md`](content/en/news.md) |

图片放在 `static/images/`，课件、数据集等文件放在 `static/files/`。Markdown 中可写成：

```markdown
[Slides](/files/slides/xxx.pdf)
```

头像文件为 `static/images/yixing.jpg`，在 `hugo.toml` 的 `avatarURL` 中引用。

## 本地预览

需要 [Hugo extended](https://gohugo.io/installation/) 0.124 或更高版本：

```bash
hugo server
```

浏览器打开 <http://localhost:1313/>。导航栏右侧的 **English / 中文** 可切换语言。

## 部署

站点由 GitHub Actions（[`.github/workflows/hugo.yml`](.github/workflows/hugo.yml)）构建并发布到 GitHub Pages。首次切换到本仓库后，请在仓库 **Settings → Pages → Build and deployment → Source** 中选择 **GitHub Actions**。自定义域名 `www.xu-ancha.com` 写在 `static/CNAME`。
