import pyautogui
import time
import random
import sys
from datetime import datetime

# === 配置区域 ===
INTERVAL = 60  # 每多少秒动一次
# ================

print(f"=== 鼠标防休眠助手已启动 ===")
print(f"正在运行中... 每 {INTERVAL} 秒微动一次")
print("【如何停止】：请直接关闭本窗口，或按 Ctrl+C")
print("【安全机制】：鼠标在屏幕角落可触发 PyAutoGUI 自动终止")

# 开启安全屏障（鼠标移到角落会报错停止）
pyautogui.FAILSAFE = True

try:
    while True:
        # 倒计时等待
        time.sleep(INTERVAL)
        
        # 获取当前时间
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # 获取当前位置
        x, y = pyautogui.position()
        
        # 随机微动 (-2 到 2 像素，肉眼几乎看不见，但系统能检测到)
        x_move = random.randint(-2, 2)
        y_move = random.randint(-2, 2)
        
        # 相对移动
        pyautogui.moveRel(x_move, y_move)
        
        print(f"[{current_time}] 鼠标已活动: ({x_move}, {y_move})")

except KeyboardInterrupt:
    print("\n程序已手动停止。")
    sys.exit()
except pyautogui.FailSafeException:
    print("\n触发安全机制（鼠标位于角落），程序停止。")
    sys.exit()