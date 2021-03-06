import pygame
from random import randint

class Question_08():

    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bgcolor = (255, 255, 255)
        self.text_color = (255, 255, 0)
        self.rect_color = (255, 255, 0)
        self.button_color = (0, 0, 0)
        self.finish = False
        self.rect_width, self.rect_height = 50, 50
        self.collided_rects = []
        self.circle_pos, self.circle_width = 300, 50
        self.circle_height = 50
        self.font = pygame.font.Font(None, 24)
        self.circle_caption = self.font.render("Clique", True, self.text_color)
        self.display_name = pygame.display.set_caption('Question 07')

    def draw_button(self):
        return pygame.draw.circle(self.screen, self.button_color, (self.circle_pos, self.circle_width), self.circle_height)

    def draw_random_squares(self, screen, rect_color, area):
        return pygame.draw.rect(screen, rect_color, area)

    def event(self):
        self.screen.fill(self.bgcolor)
        button = self.draw_button()
        self.screen.blit(self.circle_caption, (272, 40))

        while not self.finish:
            x, y = randint(0, self.width), randint(0, self.height)
            area = pygame.Rect(x, y, self.rect_width, self.rect_height)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if button.collidepoint(pos):
                        square = self.draw_random_squares(self.screen, self.rect_color, area)
                        # self.collided_rects.append(square)
                        self.collided_rects.append(area)
                        print(self.collided_rects)
                    
                        for r in self.collided_rects:
                            if r is not area and r.colliderect(area):
                                self.collided_rects.remove(r)
                                #pygame.draw.rect(self.screen, (255, 0, 0), r)

                                # self.rect_color = (255, 255, 0)

                                if area in self.collided_rects:
                                    self.collided_rects.remove(area)
                                print("colidiu")

                                # if area in self.collided_rects:
                                #     self.collided_rects.remove(area)
                                #     print("colidiu")
                        self.screen.fill(self.bgcolor)
                        for r in self.collided_rects:
                            self.draw_random_squares(self.screen, self.rect_color, r)

                        self.draw_button()
                        self.screen.blit(self.circle_caption, (272, 40))
                        # for r in self.collided_rects:
                        #     if r is not square and r.colliderect(square):
                        #         self.collided_rects.remove(r)
                        #         print("colidiu")
                                
                        #         if square in self.collided_rects:
                        #             self.collided_rects.remove(square)
                        #             print("colidiu")
                                
                        #         for r in self.collided_rects:
                        #             self.screen.fill(self.bgcolor)
                        #             self.draw_random_squares(self.screen, self.rect_color, area)
                        #             self.draw_button()
                        #             self.screen.blit(self.circle_caption, (272, 40))
                            
                            
                pygame.display.update()

        pygame.display.quit()
        pygame.quit()

Question_08().event()