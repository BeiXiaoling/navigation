# Navigation · 个人导航页

一个简洁、美观、实用的个人导航页，支持图标展示、自定义分类、响应式布局，适合自部署和私人站点跳转入口使用。

> 预览图：
>
> ![img](https://r2.wuxie.de/other/20250714_90e98988.jpg)

---

## ✨ 功能特点

- 🧭 分类清晰：支持“网站服务”、“穿透服务”、“内网服务”等多级分类；
- 🖼 图标美观：使用 FontAwesome 免费图标；
- 📱 响应式设计：在手机、平板和桌面端均显示良好；
- 🧩 数据配置：导航内容由 `navigation.json` 控制，便于维护和更新；
- 🌌 可自定义背景：支持根据设备分辨率使用不同的随机背景 API。

---

## 📁 项目结构说明

```

navigation/
├── xiny/                       # 存放静态资源
│   ├── favicon.ico             # 页面图标
│   └── fontawesome/            # FontAwesome 图标（CDN 加速镜像）
├── index.html                  # 主页面，导航展示逻辑和前端代码
└── navigation.json             # 配置文件，定义所有导航链接和图标

```

---

## 🧾 `navigation.json` 格式说明

`navigation.json` 是一个结构化的 JSON 文件，用于管理所有导航链接。大致结构如下：

```json
{
  "分类名": [
    {
      "name": "显示名称",
      "url": "https://example.com/",
      "icon": "fa-solid fa-icon-name"
    }
  ]
}
````

* `name`：链接的名称；
* `url`：点击后跳转的地址；
* `icon`：FontAwesome 图标的类名，例如 `fa-solid fa-film`；

  * 需要什么图标可以问 AI，或者在 [FontAwesome 图标库](https://fontawesome.com/icons) 中搜索查看。

---

## 🚀 快速开始

### 方式一：本地浏览器打开

1. 克隆仓库：

   ```bash
   git clone https://github.com/xinycai/navigation.git
   cd navigation
   ```

2. 用浏览器打开 `index.html` 即可访问导航页。

---

### 方式二：部署到服务器

1. 上传整个项目到你的服务器，例如 `/www/navigation`；
2. 配置 Nginx/Caddy/apache 等 Web 服务指向该目录；
3. 打开浏览器访问对应地址即可。

---

## ⚙️ 自定义配置

### 修改导航数据

编辑 `navigation.json` 文件，自定义你自己的分类和跳转链接，格式详见上文。

### 修改背景图片 API

`index.html` 第 490 行附近存在背景 API 的调用逻辑：

```js
const baseUrl = window.innerWidth <= 768
    ? 'https://img-api.wuxie.de/acg/13/sp'
    : 'https://img-api.wuxie.de/acg/13/sp';
```

你可以将 `baseUrl` 替换为你自己的随机图片 API 地址，例如：

```js
const baseUrl = 'https://api.example.com/random-wallpaper';
```

---

## 📌 依赖说明

* 无需构建、无需依赖环境；
* 页面中使用了 FontAwesome 图标；
* 可直接在本地或任意支持 HTML 的环境中运行。

---

## 📷 示例用途

本导航页适合：

* 私人站点总入口
* 内网服务汇总
* 自建服务门户
* 家庭网络管理面板

---

感谢使用！欢迎 Star ⭐ 支持这个项目！


##🤖fork后AI修改了

-让codex写了个小后端，点点点修改

-后台密码设置说明
部署后设置后台密码的方式是：在服务器上自己生成 .admin_htpasswd。
例如后台用户名用 admin，密码用 ovos1024：
cd /opt/1panel/apps/openresty/openresty/www/sites/www.ovo-s.com/index

hash=$(openssl passwd -apr1 'ovos1024')
echo "admin:$hash" > .admin_htpasswd
chmod 644 .admin_htpasswd
如果想换用户名，比如 root：
hash=$(openssl passwd -apr1 '你的密码')
echo "root:$hash" > .admin_htpasswd
chmod 644 .admin_htpasswd
