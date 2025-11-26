# Mouse Jiggler (鼠标防休眠助手) - portable version

这是一个基于 Python 开发的轻量级工具，通过模拟微小的鼠标移动来防止计算机进入休眠、锁屏状态或保持在线状态（如 Teams/Slack/企业微信）。
此分支为[Mouse Jiggler](https://github.com/Joe-Xuu/mouse-jiggler)的便携版本 - 使用embedded python

适合长时间挂机下载、运行脚本或保持工作软件在线状态的场景。

**特点：**
* **无需安装 Python**：自带独立运行环境。
* **无需管理员权限**：公司电脑也能直接运行。
* **即插即用**：解压即用，不修改系统注册表。

---

## 给使用者的操作指南

如果你收到了这个压缩包，请按照以下步骤操作：

### 1. 解压文件 (重要！)
**请务必将压缩包解压出来**。不要直接在压缩软件里双击打开，否则程序会找不到运行环境。

### 2. 启动程序
进入解压后的文件夹，双击运行 **`run.bat`**。

* 你会看到一个黑色的命令窗口出现，这说明程序正在运行。
* 程序会每隔一段时间微动鼠标（包含拟人化滑动），防止电脑锁屏。

### 3. 停止程序
* **方法一**：直接关闭那个黑色的命令窗口。
* **方法二**：在黑色窗口中按 `Ctrl+C`。

---

## 构建指南 (给开发者)

本部分记录了如何从零生成这个 `dist_portable` 便携包。由于嵌入式环境体积较大且包含二进制文件，通常不建议完整上传至 Git，请按照以下步骤复原环境。

### 1. 准备嵌入式 Python
1. 从 Python 官网下载 **Windows embeddable package (64-bit)** (推荐 Python 3.10+)。
2. 解压并重命名文件夹为 `python_env`。

### 2. 解锁环境配置
1. 打开 `python_env` 文件夹内的 `python3xx._pth` 文件。
2. **取消注释最后一行** (`import site`)，以便允许加载第三方库。

### 3. 安装 pip 和依赖
在 `dist_portable` 目录下打开终端，依次运行：

```bash
# 1. 下载 pip 安装脚本
curl [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) -o get-pip.py

# 2. 给嵌入式 Python 安装 pip
.\python_env\python.exe get-pip.py

# 3. 安装项目依赖 (PyAutoGUI)
.\python_env\python.exe -m pip install pyautogui
**本工具仅供学习和个人辅助使用。请勿用于规避公司考勤制度或进行恶意操作。开发者不对因使用本工具造成的任何后果负责**

MIT Lisense

2025 Developed by Kouzen Jo. All Rights Reserved.