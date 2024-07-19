import pygame

# Pygameライブラリを初期化
pygame.init()

# 800x600ピクセルのウィンドウを作成
screen = pygame.display.set_mode((800,600))

# 色の定義 (RGB形式)
WHITE = (255,255,255)  # 白色
RED = (255,0,0)        # 赤色

# ウィンドウ全体を白色で塗りつぶし
screen.fill(WHITE)

# 赤い円を描画（左上隅）
pygame.draw.circle(screen, RED, (0, 0), 5)
# 赤い円を描画（右上隅）
pygame.draw.circle(screen, RED, (799, 0), 5)
# 赤い円を描画（左下隅、座標のyが間違っているため修正が必要：599）
pygame.draw.circle(screen, RED, (0, 599), 5)
# 赤い円を描画（右下隅）
pygame.draw.circle(screen, RED, (799, 599), 5)

# 左上隅から右下隅への赤い線を描画
pygame.draw.line(screen, RED, (0, 0), (799, 599))
# 右上隅から左下隅への赤い線を描画
pygame.draw.line(screen, RED, (799, 0), (0, 599))

# 画面更新を反映
pygame.display.flip()

# メインループ（ウィンドウが閉じられるまで実行）
running = True
while running:
    for event in pygame.event.get():
        # ウィンドウの閉じるボタンが押された時の処理
        if event.type == pygame.QUIT:
            running = False

# Pygameを終了（実際には省略されるが、良い習慣として）
pygame.quit()
