import pygame
import random

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Circle")

# 색상 정의
colors = [(255, 0, 0), (0, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]
current_color = random.choice(colors)

# 동그라미 초기 위치와 크기
circle_radius = 20
circle_x = screen_width // 2
circle_y = screen_height // 2

# 프레임 레이트 설정
clock = pygame.time.Clock()
fps = 1000

# 속도 설정
speed = 5

# 키 상태 저장 변수
keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}

# 색깔 변경 함수
def change_color(current_color):
    new_color = current_color
    while new_color == current_color:
        new_color = random.choice(colors)
    return new_color

running = True
while running:
    dt = clock.tick(fps) / 1000  # 델타 타임 (초 단위로 변환)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 왼쪽 버튼 클릭
                current_color = change_color(current_color)
    
    # 동그라미 이동 처리
    if keys[pygame.K_LEFT]:
        circle_x -= speed
    if keys[pygame.K_RIGHT]:
        circle_x += speed
    if keys[pygame.K_UP]:
        circle_y -= speed
    if keys[pygame.K_DOWN]:
        circle_y += speed
    
    # 경계 체크
    if circle_x - circle_radius < 0:
        circle_x = circle_radius
    if circle_x + circle_radius > screen_width:
        circle_x = screen_width - circle_radius
    if circle_y - circle_radius < 0:
        circle_y = circle_radius
    if circle_y + circle_radius > screen_height:
        circle_y = screen_height - circle_radius

    # 화면 업데이트
    screen.fill((255, 255, 255))  # 흰색 배경
    pygame.draw.circle(screen, current_color, (circle_x, circle_y), circle_radius)
    pygame.display.flip()

pygame.quit()
