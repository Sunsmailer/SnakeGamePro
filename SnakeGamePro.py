import pygame
import time
import random

pygame.init()

width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

font = pygame.font.SysFont("None", 35)

# поле
color_display = (255, 253, 208)
# цвет змеи
color_snake = (119, 221, 119)
# цвет проигрыша красный
color_lose = (213, 50, 80)
# тело змеи
segment_size = 20
# скорость змейки
snake_speed = 10
# голова змеи
head_x = width // 2 // segment_size * segment_size
head_y = height // 2 // segment_size * segment_size


# еда
color_food = (255, 128, 0)


def get_random_point():
    x = random.randint(0, width - segment_size) // segment_size * segment_size
    y = random.randint(0, height - segment_size) // segment_size * segment_size
    return x, y


def show_snake(snake):
    for x in snake:
        pygame.draw.rect(display, color_snake, [x[0], x[1], segment_size, segment_size])


def show_score(score):
    value = font.render("Очки: " + str(score), True, color_snake)
    display.blit(value, [0, 0])


food_x, food_y = get_random_point()

# съесть фрукт
snake = []
snake_length = 1
# скорость по иксам
vx = 0
# скорость по игрекам
vy = 0


clock = pygame.time.Clock()


while True:
    if head_x < 0 or head_x > width - segment_size or head_y < 0 or head_y > height - segment_size:

        message = font.render("Вы проиграли", True, color_lose)
        display.blit(message, [width / 2.4, height / 2.3])
        pygame.display.flip()

        time.sleep(2)

        pygame.quit()
        quit()

    events = pygame.event.get()

    for event in events:
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vy = segment_size
                vx = 0
            elif event.key == pygame.K_UP:
                vy = -segment_size
                vx = 0
            elif event.key == pygame.K_LEFT:
                vy = 0
                vx = -segment_size
            elif event.key == pygame.K_RIGHT:
                vy = 0
                vx = segment_size
    head_x += vx
    head_y += vy

# фон
    display.fill(color_display)
# фрукт
    pygame.draw.rect(display, color_food, [food_x, food_y, segment_size, segment_size])

# начало левый верхний угол (увеличить сверху вниз) отображение змейки
    pygame.draw.rect(display, color_snake, [head_x, head_y, segment_size, segment_size])

    snake.append((head_x, head_y))
    if len(snake) > snake_length:
        del snake[0]

    show_snake(snake)
    show_score(snake_length - 1)

    if head_x == food_x and head_y == food_y:
        food_x, food_y = get_random_point()
        snake_length += 1

    pygame.display.flip()
    clock.tick(snake_speed)
