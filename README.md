# Mouse Jiggler (鼠标防休眠助手)

这是一个基于 Python 开发的轻量级工具，通过模拟微小的鼠标移动来防止计算机进入休眠、锁屏状态或保持在线状态（如 Teams/Slack/企业微信）。

适合长时间挂机下载、运行脚本或保持工作软件在线状态的场景。

## ✨ features

* **防休眠**：每 60 秒随机微动鼠标（肉眼几乎不可见），有效防止系统锁屏。
* **轻量级**：打包后为独立的 `.exe` 可执行文件，无需安装 Python 环境。
* **安全机制**：
    * **Ctrl+C**：在控制台按 Ctrl+C 即可退出。
* **可视化**：控制台实时打印运行日志和当前时间。

## 🚀 Jump Start for Users

如果你只想使用本软件，无需配置开发环境：

1. 下载 [Releases](你的GitHub发布页链接/releases) 中的 `main.exe` 文件。
2. 双击运行 `main.exe`。
3. 若要停止，直接关闭黑色命令窗口，或按 `Ctrl+C`。

---

## 🛠️ 开发指南 (对于开发者)

如果你想修改代码或自己构建项目，请遵循以下步骤。本项目使用 **Python 3** 和 **Virtual Environment** 进行开发。

### 1. 环境准备

克隆项目到本地：
```bash
git clone [https://github.com/你的用户名/mouse-jiggler.git](https://github.com/你的用户名/mouse-jiggler.git)
cd mouse-jiggler
```

### 2.venv

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Dependencies
```bash
pip install -r requirements.txt
```

### 4. run the codes
```bash
python main.py
```

### 5. packaging
本项目使用 PyInstaller 将 Python 脚本打包为独立可执行文件。

在虚拟环境激活的状态下，运行以下命令：

```Bash
pyinstaller -F main.py
```
- 构建产物：生成的文件位于 dist/ 目录下。

- 清理：构建完成后，build/ 文件夹和 main.spec 文件可以删除。

### 6. project arch

mouse-jiggler/
├── dist/               # 打包后的exe
├── venv/               # venv
├── main.py             # 主程序源码
├── README.md           # readme
├── requirements.txt    
└── .gitignore          

### 7. Disclaimer

**本工具仅供学习和个人辅助使用。请勿用于规避公司考勤制度或进行恶意操作。开发者不对因使用本工具造成的任何后果负责**

MIT Lisense

2025 Developed by Kouzen Jo. All Rights Reserved.