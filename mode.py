import pygame

from flashcards import Flashcards
from quiz import GiaiDo
from tomau import ToMau

class Mode:
    def __init__(self, lobby):
        self.lobby = lobby
        self.rect_list = [0, 0, 0, 0, 'right']

    def init_mode(self):
        self.background = pygame.image.load('./assets/mode/mode.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft = (0, 0))

        self.flashcards = pygame.image.load('./assets/mode/flashcards.png')
        self.flashcards = pygame.transform.scale(self.flashcards, (206, 206))
        self.flashcards_rect = self.flashcards.get_rect(center = (248, 375))

        self.giaido = pygame.image.load('./assets/mode/giaido.png')
        self.giaido = pygame.transform.scale(self.giaido, (206, 206))
        self.giaido_rect = self.giaido.get_rect(center = (500, 375))

        self.tomau = pygame.image.load('./assets/mode/tomau.png')
        self.tomau = pygame.transform.scale(self.tomau, (206, 206))
        self.tomau_rect = self.tomau.get_rect(center = (751, 375))

        self.right_arrow = pygame.image.load('./assets/mode/right_arrow.png')
        self.right_arrow = pygame.transform.scale(self.right_arrow, (83, 107))
        self.right_arrow_rect = self.right_arrow.get_rect(center = (930, 375))

        self.exit_button = pygame.image.load('./assets/flashcards/exit.png').convert_alpha()
        self.exit_button = pygame.transform.scale(self.exit_button, (146, 50))
        self.exit_button_rect = self.exit_button.get_rect(topleft = (50, 30))

        self.rect_list = [self.flashcards_rect, self.giaido_rect, self.tomau_rect, self.right_arrow_rect, 'right']

    def draw_mode(self):
        self.lobby.screen.blit(self.background, self.background_rect)
        self.lobby.screen.blit(self.flashcards, self.flashcards_rect)
        self.lobby.screen.blit(self.giaido, self.giaido_rect)
        self.lobby.screen.blit(self.tomau, self.tomau_rect)
        self.lobby.screen.blit(self.right_arrow, self.right_arrow_rect)
        self.lobby.screen.blit(self.exit_button, self.exit_button_rect)


    def change_mode(self, direction):
        if direction == 'right':

            self.background = pygame.image.load('./assets/mode/mode.png').convert()
            self.background = pygame.transform.scale(self.background, (1000, 707))
            self.background_rect = self.background.get_rect(topleft = (0, 0))

            self.left_arrow = pygame.image.load('./assets/mode/left_arrow.png')
            self.left_arrow = pygame.transform.scale(self.left_arrow, (83, 107))
            self.left_arrow_rect = self.left_arrow.get_rect(center = (70, 375))

            self.divenha = pygame.image.load('./assets/mode/divenha.png')
            self.divenha = pygame.transform.scale(self.divenha, (206, 206))
            self.divenha_rect = self.divenha.get_rect(center = (248, 375))

            self.dieukhienxe = pygame.image.load('./assets/mode/dieukhienxe.png')
            self.dieukhienxe = pygame.transform.scale(self.dieukhienxe, (206, 206))
            self.dieukhienxe_rect = self.dieukhienxe.get_rect(center = (500, 375))

            self.giaimamecung = pygame.image.load('./assets/mode/giaimamecung.png')
            self.giaimamecung = pygame.transform.scale(self.giaimamecung, (206, 206))
            self.giaimamecung_rect = self.giaimamecung.get_rect(center = (751, 375))

            self.lobby.screen.blit(self.background, self.background_rect)
            self.lobby.screen.blit(self.divenha, self.divenha_rect)
            self.lobby.screen.blit(self.dieukhienxe, self.dieukhienxe_rect)
            self.lobby.screen.blit(self.giaimamecung, self.giaimamecung_rect)
            self.lobby.screen.blit(self.left_arrow, self.left_arrow_rect)

            self.rect_list = [self.divenha_rect, self.dieukhienxe_rect, self.giaimamecung_rect, self.left_arrow_rect, 'left']


        elif direction == 'left':
            del self.divenha
            del self.divenha_rect
            del self.dieukhienxe
            del self.dieukhienxe_rect
            del self.giaimamecung
            del self.giaimamecung_rect
            del self.left_arrow
            del self.left_arrow_rect

            self.init_mode()
            self.draw_mode()

    def handle_event(self, event):
        if(self.exit_button_rect.collidepoint(event.pos)):
            print('lobby')
            self.lobby.state = 'lobby'
        if(self.rect_list[0].collidepoint(event.pos) and self.rect_list[4] == 'right'):
            print('flashcards')
            Flashcards(self.lobby.screen, self.lobby.clock).run()
        elif(self.rect_list[1].collidepoint(event.pos) and self.rect_list[4] == 'right'):
            print('giaido')
            GiaiDo(self.lobby.screen, self.lobby.clock).run()
        elif(self.rect_list[2].collidepoint(event.pos) and self.rect_list[4] == 'right'):
            print('tomau')
            ToMau(self.lobby.screen, self.lobby.clock).run()
        elif(self.rect_list[4] == 'right' and self.rect_list[3].collidepoint(event.pos)):
            print('change right')
            self.change_mode('right')
        elif(self.rect_list[4] == 'left' and self.rect_list[3].collidepoint(event.pos)):
            print('change left')
            self.change_mode('left')
        elif(self.rect_list[0].collidepoint(event.pos) and self.rect_list[4] == 'left'):
            print('divenha')
        elif(self.rect_list[1].collidepoint(event.pos) and self.rect_list[4] == 'left'):
            print('dieukhienxe')
        elif(self.rect_list[2].collidepoint(event.pos) and self.rect_list[4] == 'left'):
            print('giaimamecung')