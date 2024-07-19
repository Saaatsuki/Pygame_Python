import pygame

# Pygameの初期化
pygame.init()

# 画面の設定
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Event Listener and Handler Example")
running = True

# キーが押されたときの処理
def handle_keydown(event):
    if event.key == pygame.K_SPACE:
        print("Spacebar pressed - handled by function.")

# ゲームループ
while running:
    # イベントの取得と処理
    for event in pygame.event.get():
        # ウィンドウを閉じるボタンが押された場合
        if event.type == pygame.QUIT:
            running = False
        # キーが押された場合
        elif event.type == pygame.KEYDOWN:
            # エスケープキーが押された場合
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed - handled by algorithm")
            # それ以外のキーが押された場合
            else:
                handle_keydown(event)

# Pygameの終了処理
pygame.quit()
