import pyautogui
import time
import sys
from datetime import datetime

# === 配置区域 ===
MOVE_DISTANCE = 50  # 移动距离 (像素)
MOVE_DURATION = 0.5 # 移动过程耗时 (秒)
# ================

print(f"=== mouse jiggler v2.0 CLI tool activated ===")
print( "Kouzen Jo 2025. Powered by pyautogui.")
INTERVAL=int(input("Please enter the interval time for anti-sleep operation (seconds): "))
print(f"Running... Performing 'human-like slide' every {INTERVAL} seconds")

# 开启安全屏障
pyautogui.FAILSAFE = True

try:
    while True:
        # 1. 倒计时等待
        time.sleep(INTERVAL)
        
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # 获取当前位置，确保不会移出屏幕外（简单的边界检查）
        x, y = pyautogui.position()
        
        # 向右移动 (模拟人手)
        pyautogui.moveRel(MOVE_DISTANCE, 0, duration=MOVE_DURATION)
        
        # 马上向左移回来 (回到原位)
        pyautogui.moveRel(-MOVE_DISTANCE, 0, duration=MOVE_DURATION)
        
        pyautogui.press('shift') 
        
        print(f"[{current_time}] Performed anti-sleep operation (slide distance: {MOVE_DISTANCE})")

except KeyboardInterrupt:
    print("\nProgram manually stopped.")
    sys.exit()
except pyautogui.FailSafeException:
    print("\nFail-safe triggered, program stopped.")
    sys.exit()