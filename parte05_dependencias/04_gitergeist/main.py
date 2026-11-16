import pyautogui as auto

from datetime import date


def main():
    hoje = date.today().strftime("%d/%m/%Y")

    auto.PAUSE = 0.75

    auto.hotkey("win","r")
    auto.write("cmd")
    auto.press("enter")
    auto.sleep(1)
    auto.write("cd C:/Users/Gustavo/Documents/desenvolvedor_python_qua.544.005")
    auto.press("enter")
    auto.write("git add *")
    auto.press("enter")
    auto.write(f'git commit -m "Tudo que vi e aprendi no curso até o dia de {hoje}"')
    auto.press("enter")
    auto.write("git branch -M main")
    auto.press("enter")
    auto.write("git remote add origin https://github.com/gustavohcsantos/desenvolvedor_python_qua.544.005.git")
    auto.press("enter")
    auto.write("git push -u origin main")
    auto.press("enter")
    auto.write("exit")
    auto.press("enter")


if __name__ == "__main__":
    main()