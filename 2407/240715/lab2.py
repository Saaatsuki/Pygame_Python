import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

screen.fill((255,255,255))
pygame.display.flip()

count = random.randint(5,20)
for _ in range(count):
    color_1 = random.randint(0,255)
    color_2 = random.randint(0,255)
    color_3 = random.randint(0,255)
    COLOR = (color_1,color_2,color_3)

    # center_x = int(screen.get_width() / 2)
    # center_y = int(screen.get_height() / 2)
    random_x = random.randint(0,screen.get_width())
    random_y = random.randint(0,screen.get_height())

    size = random.randint(50,200)
    pygame.draw.circle(screen,COLOR,(random_x,random_y),size)

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