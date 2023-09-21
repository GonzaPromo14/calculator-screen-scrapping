from utils import click_image
import pyautogui

class Calculator:

    def __init__(self) -> None:
        pyautogui.press("win")
        pyautogui.write("CALCULADORA")
        pyautogui.press("enter")

    def operate(self, number1, number2, operation="add"):
        click_image(number1)
        click_image(operation)
        click_image(number2)
        click_image("equals")