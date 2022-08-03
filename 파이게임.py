import pygame
import os

# 초기화
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Pygame")
icon = pygame.image.load("C:\\Users\\eyulj\\Documents\\Python\\PythonWorkspace\\CheatSheet\\pygame_images\\icon.jpg")
pygame.display.set_icon(icon)

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# current path
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "pygame_images")

##################################################

# background
background = pygame.image.load(os.path.join(images_path, "background.png"))

# spuare
square = pygame.image.load(os.path.join(images_path, "square.png"))
square_size = square.get_rect().size
square_width = square_size[0]
square_height = square_size[1]
square_posX = (screen_width / 2) - (square_width / 2)
square_posY = screen_height - square_height

square_toX = 0
square_toY = 0
square_speed = 0.1

# enemy
enemy = pygame.image.load(os.path.join(images_path, "enemy.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_posX = (screen_width / 2) - (enemy_width / 2)
enemy_posY = (screen_height / 2) - (enemy_height / 2)

# 타이머
total_time = 10
start_ticks = pygame.time.get_ticks()

# 게임 오버 메시지
gameover_msg = "Game Over"

##################################################

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # fps

    for event in pygame.event.get():
        # 종료
        if event.type == pygame.QUIT:
            running = False

        # 키보드 입력
        if event.type == pygame.KEYDOWN: # 누름
            if event.key == pygame.K_RIGHT:
                square_toX += square_speed
            elif event.key == pygame.K_LEFT:
                square_toX -= square_speed
            elif event.key == pygame.K_UP:
                square_toY -= square_speed
            elif event.key == pygame.K_DOWN:
                square_toY += square_speed
            
        if event.type == pygame.KEYUP: # 뗌
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                square_toX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                square_toY = 0

    # 위치 정의
    square_posX += square_toX * dt # fps 와 무관하게 일정한 속도
    square_posY += square_toY * dt 

    # 경계값
    if square_posX < 0:
        square_posX = 0
    elif square_posX > screen_width - square_width:
        square_posX = screen_width - square_width

    if square_posY < 0:
        square_posY = 0
    elif square_posY > screen_height - square_height:
        square_posY = screen_height - square_height

    # 충돌 처리
        # rect 정보 업데이트
    square_rect = square.get_rect()
    square_rect.left = square_posX
    square_rect.top = square_posY

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_posX
    enemy_rect.top = enemy_posY
        # 충돌 체크
    if square_rect.colliderect(enemy_rect):
        gameover_msg = "CRASH!!"
        running = False

##################################################

    # 화면
    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    screen.blit(square, (square_posX, square_posY))
    screen.blit(enemy, (enemy_posX, enemy_posY))
    
    # 타이머
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 출력문, True, 색상
    screen.blit(timer, (10, 10))

    if elapsed_time > total_time:
        gameover_msg = "Time Over"
        running = False

    pygame.display.update() # 화면 다시 그리기

##################################################

# 게임 오버 메시지
msg = game_font.render(gameover_msg, True, (255, 255, 0))
msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
    
pygame.display.update() # 화면 다시 그리기

# 종료
pygame.time.delay(2000) # 대기
pygame.quit()