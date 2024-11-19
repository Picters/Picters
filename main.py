import pygame
import random

# Инициализация pygame
pygame.init()

# Получаем размер экрана
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Создаем экран в полноэкранном режиме
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Отскакивающий текст")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Настройки текста
font = pygame.font.SysFont("Arial", 80)  # Шрифт и размер текста
text = font.render("Picters", True, WHITE)  # Создаем текстовое изображение

text_width, text_height = text.get_size()  # Получаем размер текста для корректного отскакивания
text_x = random.randint(0, screen_width - text_width)
text_y = random.randint(0, screen_height - text_height)

# Скорость движения текста
speed_x = random.choice([3, -3])
speed_y = random.choice([3, -3])

# Настройки FPS
clock = pygame.time.Clock()

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление позиции текста
    text_x += speed_x
    text_y += speed_y

    # Отскакивание от стен
    if text_x <= 0 or text_x + text_width >= screen_width:
        speed_x = -speed_x
    if text_y <= 0 or text_y + text_height >= screen_height:
        speed_y = -speed_y

    # Отображаем фон
    screen.fill(BLACK)

    # Рисуем текст
    screen.blit(text, (text_x, text_y))

    # Обновляем экран
    pygame.display.flip()

    # Устанавливаем FPS
    clock.tick(60)

# Закрытие игры
pygame.quit()
