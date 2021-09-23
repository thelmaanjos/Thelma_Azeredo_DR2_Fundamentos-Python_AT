import pygame
from random import randint

class Question_07():

    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bgcolor = (255, 255, 255)
        self.rect_color = (255, 255, 0)
        self.finish = False
        self.rect_width, self.rect_height = 50, 50
        self.display_name = pygame.display.set_caption('Question 07')

    def draw_random_squares(self, screen, rect_color, area):
        pygame.draw.rect(screen, rect_color, area)

    def event(self):
        self.screen.fill(self.bgcolor)

        while not self.finish:   
            x, y = randint(0, self.width), randint(0, self.height)
            area = pygame.Rect(x, y, self.rect_width, self.rect_height)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                       self.draw_random_squares(self.screen, self.rect_color, area)
                       print(" oi")
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.draw_random_squares(self.screen, self.rect_color, area)
                        print(" olá")

                pygame.display.update()

        pygame.display.quit()
        pygame.quit()

Question_07().event()