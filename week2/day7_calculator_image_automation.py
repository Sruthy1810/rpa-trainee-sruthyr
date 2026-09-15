import pyautogui
import time
from pathlib import Path


def click_image(image_path):

    print("\nLooking for:", image_path)

    try:
        location = pyautogui.locateCenterOnScreen(
            str(image_path),
            confidence=0.8
        )

        if location:
            print("Location:", location)

            pyautogui.moveTo(location, duration=0.5)

            print("Moving mouse to:", location)

            time.sleep(1)

            pyautogui.click()

            print("CLICKED:", image_path)

            time.sleep(1)

        else:
            print("Not found:", image_path)

    except pyautogui.ImageNotFoundException:
        print("Not found:", image_path)


def main():

    pyautogui.hotkey("win", "r")
    time.sleep(1)

    pyautogui.write("calc")
    pyautogui.press("enter")
    time.sleep(3)

    BASE_DIR = Path(__file__).resolve().parent
    ASSETS_DIR = BASE_DIR / "assets"

    print("Assets folder:", ASSETS_DIR)
    print("Assets exists:", ASSETS_DIR.exists())

    click_image(ASSETS_DIR / "2.png")
    click_image(ASSETS_DIR / "5.png")
    click_image(ASSETS_DIR / "plus2.png")
    click_image(ASSETS_DIR / "1.png")
    click_image(ASSETS_DIR / "0.png")
    click_image(ASSETS_DIR / "equals.png")


if __name__ == "__main__":
    main()