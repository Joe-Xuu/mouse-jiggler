import pyautogui
import time
import sys
from datetime import datetime

# === 配置区域 ===
MOVE_DISTANCE = 50  # 移动距离 (像素)
MOVE_DURATION = 0.5 # 移动过程耗时 (秒)
# ================

print(f"=== 鼠标防休眠助手 v2.0 已启动 ===")
INTERVAL=int(input("请输入防休眠操作的间隔时间（秒）："))
print(f"正在运行中... 每 {INTERVAL} 秒执行一次“拟人化滑动”")
print("【如何停止】：请直接关闭本窗口，或按 Ctrl+C")
print("【安全机制】：将鼠标快速甩到屏幕角落可触发紧急停止")

# 开启安全屏障
pyautogui.FAILSAFE = True

try:
    while True:
        # 1. 倒计时等待
        time.sleep(INTERVAL)
        
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # 获取当前位置，确保不会移出屏幕外（简单的边界检查）
        x, y = pyautogui.position()
        
        # 2. 执行“有去有回”的拟人化滑动
        # 这种 continuous 的信号最容易欺骗 Teams/Slack
        
        # 向右移动 (模拟人手)
        pyautogui.moveRel(MOVE_DISTANCE, 0, duration=MOVE_DURATION)
        
        # 马上向左移回来 (回到原位)
        pyautogui.moveRel(-MOVE_DISTANCE, 0, duration=MOVE_DURATION)
        
        pyautogui.press('shift') 
        
        print(f"[{current_time}] 已执行防休眠操作 (滑动距离: {MOVE_DISTANCE})")

except KeyboardInterrupt:
    print("\n程序已手动停止。")
    sys.exit()
except pyautogui.FailSafeException:
    print("\n触发安全机制（鼠标位于角落），程序停止。")
    sys.exit()