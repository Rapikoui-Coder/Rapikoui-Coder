#coding:utf-8
# 
main.py


"Cookie Clicker"

# importations
import pygame
from sys import exit
from time import sleep
from cookie import Cookie
pygame.init() # initialisation

# classe principale du jeu
class Game:
    def __init__(self):

        # dimensions de la fenêtre
        self.SCREEN_WIDTH = 1080
        self.SCREEN_HEIGHT = 720
        # titre de la fenêtre
        pygame.display.set_caption(" - Cookie Clicker - ")
        # création de la fenêtre
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.running = True
        # charger l'arrière plan du jeu
        self.background = pygame.image.load('assets/background.jpg')
        # redimmensionner l'arière plan du jeu
        self.background = pygame.transform.scale(self.background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        # charger le cookie
        self.cookie = Cookie(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        # définir les points
        self.score = -1
        # définir les polices
        self.score_font = pygame.font.Font("assets/my_custom_font.ttf", 50)
        self.main_font = pygame.font.Font("assets/my_custom_font.ttf", 50)
        self.end_font = pygame.font.Font("assets/my_custom_font.ttf", 70)
        # charger l'icône du jeu
        self.icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(self.icon)
        # charger le bouton pour lancer le jeu
        self.play_button = pygame.image.load('assets/button.png')
        self.is_playing = False
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = (self.SCREEN_WIDTH // 2) - (self.play_button_rect.width // 2)
        self.play_button_rect.y = (self.SCREEN_HEIGHT // 2) - (self.play_button_rect.height // 2)
        self.max_score = 1000
        self.end = False

    # boucle principale
    def run(self):
        while self.running:
            self.draw()
            self.update()

    def draw(self):
        # empaqueter les éléments
        self.screen.blit(self.background, (0, 0))
        if self.is_playing and self.score <= self.max_score and not self.end:
            self.cookie.draw(self.screen)
            score_text = self.score_font.render("Score : " + str(self.score), True, (0, 0, 0))
            self.screen.blit(score_text, (0, 125))
            main_text = self.main_font.render("COOKIE CLICKER !!!", True, (0, 0, 0))
            self.screen.blit(main_text, (275, 0))

        elif not self.is_playing and self.score <= self.max_score and not self.end:
            self.screen.blit(self.play_button, self.play_button_rect)

        elif self.end:
            end_text = self.end_font.render("Bravo ! Tu as gagné !", True, (0, 0, 0))
            self.screen.blit(end_text, (150, 0))
            self.is_playing = False
            self.score = -1
            self.screen.blit(self.play_button, self.play_button_rect)

        pygame.display.flip()

    def update(self):
        # mettre à jour les éléments
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
                pygame.quit()

            if self.is_playing and self.score < self.max_score:

                # vérifier si le joueur clique sur le cookie
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.cookie.rect.collidepoint(event.pos):
                        self.score += 1
                        if not self.is_playing and self.score > self.max_score:
                            self.end = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.score += 1
                if self.score == 1000:
                    self.end = True

            elif not self.is_playing:
                
                # vérifier si le joueur clique sur le bouton pour lancer le jeu
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.is_playing = True
                        self.end = False

if __name__ == '__main__':
    game = Game()
    
game.run() 
