import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

try:
    pyautogui.screenshot("beforenotepad.png")
    pyautogui.hotkey("win","r")
    pyautogui.write("notepad")
    pyautogui.press("enter")

    time.sleep(5)
    paragraph = (
    "PyAutoGUI is a Python library used for desktop automation. "
    "It allows us to control the mouse and keyboard using Python. "
    "In this task, I learned how to open an application, type text, "
    "use keyboard shortcuts, work with screen coordinates, "
    "and save a file through GUI automation."
)

    pyautogui.write(paragraph, interval=0.01)
    time.sleep(2)
    print("Saving file")
    pyautogui.hotkey("Ctrl","S")
    time.sleep(5)
    pyautogui.write("day6_pyautogui.txt")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(3)
    print("File saved successfully")
    pyautogui.screenshot("after_notepad.png")

except pyautogui.FailSafeException:
    print("Automation stopped by user!")