import pyautogui
import time

def click_image(name_image, condifence=0.95, timeout=30, image_wait=2, action=pyautogui.click):
    x = -1
    time_break = time.time() + timeout
    while x < 0 and time.time() < time_break:
        try:
            x, y = pyautogui.locateCenterOnScreen("./images/{0}.png".format(name_image), confidence=condifence)
            action(x, y)
        except Exception as ex:
            print(str(ex))
            print(f"The image: {name_image} not found yet")
            time.sleep(image_wait)