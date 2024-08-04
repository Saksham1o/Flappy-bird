# Importing the libraries
import pygame
import sys
import time
import random

# Initializing the pygame
pygame.init()

# Frames per second
clock = pygame.time.Clock()


# Function to draw
def draw_floor():
    screen.blit(floor_img, (floor_x, 520))
    screen.blit(floor_img, (floor_x + 448, 520))


# Function to create pipes
def create_pipes():
    pipe_y = random.choice(pipe_height)
    top_pipe = pipe_img.get_rect(midbottom=(467, pipe_y - 300))
    bottom_pipe = pipe_img.get_rect(midtop=(467, pipe_y))
    return top_pipe, bottom_pipe


# Function for animation
def pipe_animation():
    global game_over, score_time
    for pipe in pipes:
        if pipe.top < 0:
            flipped_pipe = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flipped_pipe, pipe)
        else:
            screen.blit(pipe_img, pipe)

        pipe.centerx -= 3
        if pipe.right < 0:
            pipes.remove(pipe)

        if bird_rect.colliderect(pipe):
            game_over = True


# Function to draw score
def draw_score(game_state):
    if game_state == "game_on":
        score_text = score_font.render(str(score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(width // 2, 66))
        screen.blit(score_text, score_rect)
    elif game_state == "game_over":
        score_text = score_font.render(f" Score: {score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(width // 2, 66))
        screen.blit(score_text, score_rect)

        high_score_text = score_font.render(f"High Score: {high_score}", True, (255, 255, 255))
        high_score_rect = high_score_text.get_rect(center=(width // 2, 506))
        screen.blit(high_score_text, high_score_rect)


# Function to update the score
def score_update():
    global score, score_time, high_score
    if pipes:
        for pipe in pipes:
            if 65 < pipe.centerx < 69 and score_time:
                score += 1
                score_time = False
            if pipe.left <= 0:
                score_time = True

    if score > high_score:
        high_score = score


# Game window
width, height = 350, 622
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# setting background and base image
back_img = pygame.image.load("img_46.png")
floor_img = pygame.image.load("img_50.png")
floor_x = 0

# different stages of bird
bird_up = pygame.image.load("img_47.png")
bird_down = pygame.image.load("img_48.png")
bird_mid = pygame.image.load("img_49.png")
birds = [bird_up, bird_mid, bird_down]
bird_index = 0
bird_flap = pygame.USEREVENT
pygame.time.set_timer(bird_flap, 200)