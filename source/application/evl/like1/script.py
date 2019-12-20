#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 0:11
# @Author  : Lewic
# @File    : her1.py
# @Software: PyCharm
# @context :

import sys
import random
import pygame
from pygame.locals import *

WIDTH, HEIGHT = 640, 480
BACKGROUND = (100, 191, 255)


def button(text, x, y, w, h, color, screen):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.Font('C:/Windows/Fonts/simkai.ttf', 20)
    textRender = font.render(text, True, (0, 0, 0))
    textRect = textRender.get_rect()
    textRect.center = ((x + w / 2), (y + h / 2))
    screen.blit(textRender, textRect)


def title(text, screen, scale, color=(255, 0, 255)):
    font = pygame.font.Font('C:/Windows/Fonts/simkai.ttf', WIDTH // (len(text) * 2))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH / scale[0], HEIGHT / scale[1])
    screen.blit(textRender, textRect)


def get_random_pos():
    x, y = random.randint(20, 620), random.randint(20, 460)
    return x, y


def show_like_interface(text, screen, color=(255, 0, 255)):
    screen.fill(BACKGROUND)
    font = pygame.font.Font('C:/Windows/Fonts/simkai.ttf', WIDTH // (len(text)))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH / 2, HEIGHT / 2)
    screen.blit(textRender, textRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('帅气的LEWIC')
    clock = pygame.time.Clock()
    pygame.mixer.music.load('大美妞.mp3')
    pygame.mixer.music.play(-1, 30.0)
    pygame.mixer.music.set_volume(0.25)
    unlike_pos_x = 330
    unlike_pos_y = 300
    unlike_pos_width = 100
    unlike_pos_height = 50
    like_pos_x = 180
    like_pos_y = 300
    like_pos_width = 100
    like_pos_height = 50
    running = True
    like_color = (255, 192, 203)

    while running:
        screen.fill(BACKGROUND)
        img = pygame.image.load("heart.png")
        imgRect = img.get_rect()
        imgRect.midtop = WIDTH // 2, HEIGHT // 4
        screen.blit(img, imgRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] < like_pos_x + like_pos_width + 5 and mouse_pos[0] > like_pos_x - 5 and \
                        mouse_pos[1] < like_pos_y + like_pos_height + 5 and mouse_pos[1] > like_pos_y - 5:
                    like_color = BACKGROUND
                    running = False
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < unlike_pos_x + unlike_pos_width + 5 and mouse_pos[0] > unlike_pos_x - 5 and \
                mouse_pos[1] < unlike_pos_y + unlike_pos_height + 5 and mouse_pos[1] > unlike_pos_y - 5:
            while True:
                unlike_pos_x, unlike_pos_y = get_random_pos()
                if mouse_pos[0] < unlike_pos_x + unlike_pos_width + 5 and mouse_pos[0] > unlike_pos_x - 5 and \
                        mouse_pos[1] < unlike_pos_y + unlike_pos_height + 5 and mouse_pos[1] > unlike_pos_y - 5:
                    continue
                break
        title('小姐姐，我暗恋你很久了', screen, scale=[2, 10])
        title('做我女朋友好不好呀', screen, scale=[2, 6])
        button('好呀', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen)
        button('滚蛋', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, (255, 215, 0), screen)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
    show_like_interface('^V^我就知道小姐姐你也喜欢我^@^', screen, color=(255, 0, 255))


if __name__ == '__main__':
    main()
