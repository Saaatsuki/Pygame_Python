# file:///C:/Users/YJU/Documents/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%86%A1%20%EB%B0%9B%EC%9D%80%20%ED%8C%8C%EC%9D%BC/chp_1_pygame%20(1).pdf

# Pygameライブラリをインポート
import pygame

# Pygameを初期化する（必要なすべてのモジュールを初期化）
pygame.init()

# 640x480ピクセルの画面を作成し、変数'screen'に保存
screen = pygame.display.set_mode((640, 480))

# ウィンドウのタイトルを設定
pygame.display.set_caption("Event Listener and Handler Example")

# メインループのフラグを設定（ゲームループを実行するかどうかを制御）
running = True

# メインゲームループの開始
while running:
    # Pygameのイベントキューからイベントを取得して処理する
    for event in pygame.event.get():
        # 取得したイベントをコンソールに出力（すべてのイベントが表示される）
        print(event)

# メインループを抜けたらPygameを終了
pygame.quit()