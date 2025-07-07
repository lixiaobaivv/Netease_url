# 网易云无损音乐解析

> **声明**  
> 本项目为开源软件，遵循 MIT 许可证。任何个人或组织均可自由使用、修改和分发本项目的源代码。但本项目及其任何衍生作品**禁止用于任何商业或付费项目**。如有违反，将视为对本项目许可证的侵犯。欢迎大家在遵守开源精神和许可证的前提下积极贡献和分享代码。

---

## 功能简介

本项目可解析网易云音乐无损音质下载链接，支持多种音质选择，支持 API 与命令行（GUI）两种模式。

---

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 Cookie

请在 `cookie.txt` 文件中填入黑胶会员账号的 Cookie，格式如下：

```
MUSIC_U=你的MUSIC_U值;os=pc;appver=8.9.70;
```

> 具体值请参考 `cookie.txt` 示例，替换为你自己的即可。

### 3. 运行

#### GUI 模式

```bash
python main.py --mode gui --url <网易云音乐地址> --level <音质参数>
```

#### API 模式

```bash
python main.py --mode api
```

- 访问接口：http://ip:port/类型解析
- 支持 GET 和 POST 请求

---

## 参数说明

### GUI 模式参数

| 参数         | 说明                         |
| ------------ | ---------------------------- |
| --mode       | 启动模式：api 或 gui         |
| --url        | 需要解析的网易云音乐地址     |
| --level      | 音质参数（见下方音质说明）   |

### API 模式参数

| 参数         | 说明                                         |
| ------------ | -------------------------------------------- |
| url / ids    | 网易云音乐地址或歌曲ID（二选一）             |
| level        | 音质参数（见下方音质说明）                   |
| type         | 解析类型：json / down / text（三选一）       |

| 类型参数         | 说明                                         |
| ------------ | -------------------------------------------- |
| Song_v1    | 单曲解析             |
| search        | 搜索解析                   |
| playlist         | 歌单解析       |
| album         | 专辑解析       |

---

## 音质参数说明（仅限单曲解析）

- `standard`：标准音质
- `exhigh`：极高音质
- `lossless`：无损音质
- `hires`：Hi-Res音质
- `jyeffect`：高清环绕声
- `sky`：沉浸环绕声
- `jymaster`：超清母带

> 黑胶VIP音质：standard, exhigh, lossless, hires, jyeffect  
> 黑胶SVIP音质：sky, jymaster

---

## Docker 一键部署

1. **修改参数**

   - 如需修改端口，请编辑 `.env` 或 `docker-compose.yml` 文件中的 `ports` 配置，例如：

     ```yaml
     ports:
       - "8080:5000"
     ```

2. **启动服务**

   ```bash
   docker-compose up -d
   ```

---

## 在线演示

[在线解析](https://api.toubiec.cn/wyapi.html)

---

## 注意事项

- 必须使用黑胶会员账号的 Cookie 才能解析高音质资源。
- Cookie 格式请严格按照 `cookie.txt` 示例填写。

---

## 致谢

- [Ravizhan](https://github.com/ravizhan)

---

## 反馈与交流

- 在 Github [Issues](https://github.com/Suxiaoqinx/Netease_url/issues) 提交反馈
- 或访问 [我的博客](https://www.toubiec.cn)

---

欢迎 Star、Fork 和 PR！

## 🐳 Docker 部署指南

### 方式一：使用环境变量（推荐）

1. **创建环境配置文件**：
```bash
# 复制示例配置文件
cp .env.example .env

# 编辑配置文件，填入您的网易云Cookie
nano .env
```

2. **获取网易云Cookie**：
   - 登录 [网易云音乐网页版](https://music.163.com)
   - 按F12打开开发者工具
   - 切换到Network（网络）选项卡
   - 刷新页面或进行任意操作
   - 找到任意请求，复制完整的Cookie值

3. **启动服务**：
```bash
# 使用docker-compose启动
docker-compose up -d

# 或使用docker run直接启动
docker run -d \
  --name netease-music \
  -p 5000:5000 \
  -e NETEASE_COOKIE="你的完整cookie字符串" \
  -e LEVEL=lossless \
  -e MODE=api \
  netease-url
```

### 方式二：使用cookie.txt文件

```bash
# 将cookie写入文件
echo "你的cookie字符串" > cookie.txt

# 启动容器并挂载文件
docker run -d \
  --name netease-music \
  -p 5000:5000 \
  -v $(pwd)/cookie.txt:/app/cookie.txt:ro \
  netease-url
```

### 环境变量说明

| 环境变量 | 必需 | 默认值 | 说明 |
|---------|-----|--------|------|
| `NETEASE_COOKIE` | 是 | - | 网易云音乐Cookie |
| `LEVEL` | 否 | lossless | 音质设置 |
| `MODE` | 否 | api | 运行模式 |
| `URL` | 否 | - | 启动时处理的URL |
| `TZ` | 否 | Asia/Shanghai | 时区设置 |

### 音质选项

- `standard`: 标准音质
- `exhigh`: 极高音质  
- `lossless`: 无损音质（推荐）
- `hires`: Hires音质
- `sky`: 沉浸环绕声
- `jyeffect`: 高清环绕声
- `jymaster`: 超清母带

### 验证部署

访问 `http://localhost:5000` 查看Web界面，或测试API接口：

```bash
# 测试API
curl "http://localhost:5000/Song_V1?ids=音乐ID&level=lossless&type=json"
```

### 安全建议

1. **生产环境**：使用Docker Secrets或专用的密钥管理服务
2. **网络安全**：仅在内网环境部署，或配置反向代理
3. **定期更新**：及时更新Cookie以确保服务正常运行