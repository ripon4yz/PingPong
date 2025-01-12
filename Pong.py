import pygame
import random

pygame.init()

# Screen dimensions
dis_width = 800
dis_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Paddle and ball properties
paddle_width = 20
paddle_height = 100
ball_size = 20

# Speeds
paddle_speed = 15
ball_speed_x = 2
ball_speed_y = 2

# Initialize display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Dynamic Pong")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("bahnschrift", 35)


def message(msg, color, y_offset=0):
    """Displays a message on the screen."""
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2 - mesg.get_width() / 2, dis_height / 2 + y_offset])


def game_loop():
    # Paddle positions
    left_paddle_y = dis_height / 2 - paddle_height / 2
    right_paddle_y = dis_height / 2 - paddle_height / 2

    # Ball position and direction
    ball_x = dis_width / 2
    ball_y = dis_height / 2
    ball_dx = random.choice([-ball_speed_x, ball_speed_x])
    ball_dy = random.choice([-ball_speed_y, ball_speed_y])

    # Scores
    left_score = 0
    right_score = 0

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get pressed keys
        keys = pygame.key.get_pressed()

        # Move paddles
        if keys[pygame.K_w] and left_paddle_y > 0:
            left_paddle_y -= paddle_speed
        if keys[pygame.K_s] and left_paddle_y < dis_height - paddle_height:
            left_paddle_y += paddle_speed
        if keys[pygame.K_UP] and right_paddle_y > 0:
            right_paddle_y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle_y < dis_height - paddle_height:
            right_paddle_y += paddle_speed

        # Move the ball
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with top and bottom walls
        if ball_y <= 0 or ball_y >= dis_height - ball_size:
            ball_dy *= -1

        # Ball collision with paddles
        if (
            ball_x <= paddle_width
            and left_paddle_y < ball_y < left_paddle_y + paddle_height
        ) or (
            ball_x >= dis_width - paddle_width - ball_size
            and right_paddle_y < ball_y < right_paddle_y + paddle_height
        ):
            ball_dx *= -1
            # Increase ball speed dynamically
            ball_dx += 1 if ball_dx > 0 else -1
            ball_dy += 1 if ball_dy > 0 else -1

        # Ball out of bounds
        if ball_x < 0:
            right_score += 1
            ball_x, ball_y = dis_width / 2, dis_height / 2
            ball_dx = random.choice([-ball_speed_x, ball_speed_x])
            ball_dy = random.choice([-ball_speed_y, ball_speed_y])

        if ball_x > dis_width:
            left_score += 1
            ball_x, ball_y = dis_width / 2, dis_height / 2
            ball_dx = random.choice([-ball_speed_x, ball_speed_x])
            ball_dy = random.choice([-ball_speed_y, ball_speed_y])

        # Clear the screen
        dis.fill(black)

        # Draw paddles and ball
        pygame.draw.rect(dis, blue, (0, left_paddle_y, paddle_width, paddle_height))
        pygame.draw.rect(
            dis, red, (dis_width - paddle_width, right_paddle_y, paddle_width, paddle_height)
        )
        pygame.draw.ellipse(dis, white, (ball_x, ball_y, ball_size, ball_size))

        # Draw scores
        score_text = font.render(f"{left_score} : {right_score}", True, white)
        dis.blit(score_text, (dis_width / 2 - score_text.get_width() / 2, 10))

        # Update display
        pygame.display.update()

        # Control frame rate
        clock.tick(60)

    pygame.quit()
    quit()


# Run the game
game_loop()
