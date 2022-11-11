import webbrowser
import time
import pyperclip
import pyautogui as pg
from PIL import ImageGrab


interval = 2
url = "https://www.google.co.jp/"
webbrowser.open(url, new=0, autoraise=True)
time.sleep(interval)
# x, y = pg.locateCenterOnScreen("google_search.png平泉町 観光
# ", grayscale=True, confidence=0.1) ほんとはこんな感じで書きたい
pyperclip.copy("平泉町 観光")  # クリップボードに日本語のせる
# pg.click(650, 300)  # ダサいというかデフォルトで検索窓なのでいらなかった
pg.hotkey("ctrl", "v")  # pyperclip.paste() なぜか貼ってくれない
pg.press("enter")  # ダサくないらしい
time.sleep(interval)
screenshot = ImageGrab.grab()
screenshot.save("screenshot.jpg")
pg.click(1345, 22)  # ダサい


# Selenium用 ボツ
# xpass
# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
# ソース平泉町 観光

# <input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="検索" value="" aria-label="検索" data-ved="0ahUKEwjr-JK96Zj7AhVcmFYBHWwlCBkQ39UDCAY">

# 座標確認
# print("Press Ctrl-C to quit.")
# try:
#     while True:
#         x, y = pg.position()
#         positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
#         print(positionStr, end="")
#         print("\b" * len(positionStr), end="", flush=True)
# except KeyboardInterrupt:
#     print("\n")