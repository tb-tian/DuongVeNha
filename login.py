import pygame
from utils import check_credentials, register_user
import time

class Login:
    def __init__(self, lobby):
        self.lobby = lobby

    def init_login(self):
        self.lobby.init = True

        self.background = pygame.image.load('./assets/login/background.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft=(0, 0))

        self.name = pygame.image.load('./assets/login/game_name.png')
        self.name = pygame.transform.scale(self.name, (424, 91))
        self.name_rect = self.name.get_rect(center=(500, 83))

        self.bulletin_board = pygame.image.load('./assets/login/bulletin_board.png').convert_alpha()
        self.bulletin_board = pygame.transform.scale(self.bulletin_board, (573, 488))
        self.bulletin_board_rect = self.bulletin_board.get_rect(center=(500, 373))

        self.exit = pygame.image.load('./assets/login/exit.png')
        self.exit = pygame.transform.scale(self.exit, (146, 50))
        self.exit_rect = self.exit.get_rect(center=(350, 587))

        self.register = pygame.image.load('./assets/login/register.png')
        self.register = pygame.transform.scale(self.register, (146, 50))
        self.register_rect = self.register.get_rect(center=(650, 587))

        self.login = pygame.image.load('./assets/login/login.png')
        self.login = pygame.transform.scale(self.login, (146, 50))
        self.login_rect = self.login.get_rect(center=(650, 527))

        self.username = pygame.image.load('./assets/login/username.png')
        self.username = pygame.transform.scale(self.username, (510, 56))
        self.username_rect = self.username.get_rect(center=(500, 325))

        self.password = pygame.image.load('./assets/login/password.png')
        self.password = pygame.transform.scale(self.password, (510, 56))
        self.password_rect = self.password.get_rect(center=(500, 400))

        self.color_active = pygame.Color(74, 232, 128)
        self.color_passive = pygame.Color(232, 128, 74)
        self.color = pygame.Color('black')
        self.username_input = pygame.Rect(400, 300, 325, 50)
        self.password_input = pygame.Rect(400, 375, 325, 50)
        self.username_active = False
        self.password_active = False
        self.error = ''

    def draw_login(self):
        self.lobby.screen.blit(self.background, self.background_rect)
        self.lobby.screen.blit(self.name, self.name_rect)
        self.lobby.screen.blit(self.bulletin_board, self.bulletin_board_rect)
        self.lobby.screen.blit(self.exit, self.exit_rect)
        self.lobby.screen.blit(self.login, self.login_rect)
        self.lobby.screen.blit(self.register, self.register_rect)
        self.lobby.screen.blit(self.username, self.username_rect)
        self.lobby.screen.blit(self.password, self.password_rect)
        if self.username_active:
            # pygame.draw.rect(self.lobby.screen, self.color_active, self.username_input, 5)
            # draw cursor
            cursor = pygame.Rect(self.username_input.x + self.lobby.font.size(self.lobby.username_text)[0], self.username_input.y + 10, 2, self.lobby.font.get_height())
            if time.time() % 1 > 0.5:
                pygame.draw.rect(self.lobby.screen, 'black', cursor)
        else:
            pygame.draw.rect(self.lobby.screen, self.color_passive, self.username_input, 5)
        if self.password_active:
            # pygame.draw.rect(self.lobby.screen, self.color_active, self.password_input, 5)
            # draw cursor
            cursor = pygame.Rect(self.password_input.x + self.lobby.font.size(self.lobby.password_text)[0], self.password_input.y + 10, 2, self.lobby.font.get_height())
            if time.time() % 1 > 0.5:
                pygame.draw.rect(self.lobby.screen, 'black', cursor)
        else:
            pygame.draw.rect(self.lobby.screen, self.color_passive, self.password_input, 5)
        self.username_surface = self.lobby.font.render(self.lobby.username_text, True, self.color)
        self.lobby.screen.blit(self.username_surface, (self.username_input.x, self.username_input.y + 10))
        self.password_surface = self.lobby.font.render(self.lobby.password_text, True, self.color)
        self.lobby.screen.blit(self.password_surface, (self.password_input.x, self.password_input.y + 10))
        if self.error != '':
            self.error_surface = self.lobby.font.render(self.error, True, "Red")
            self.lobby.screen.blit(self.error_surface, (255, 445))

    def handle_event(self, event):
        if self.lobby.state == 'login':
            if self.exit_rect.collidepoint(event.pos):
                pygame.quit()
                exit()
            if self.login_rect.collidepoint(event.pos):
                if check_credentials(self.lobby.username_text, self.lobby.password_text):
                    self.lobby.state = 'lobby'
                else:
                    self.error = "Invalid credentials"
            if self.register_rect.collidepoint(event.pos):
                if self.lobby.username_text and self.lobby.password_text:
                    register_user(self.lobby.username_text, self.lobby.password_text)
                    self.error = "Registration successful"
                else:
                    self.error = "Please fill in all fields"

            if self.username_input.collidepoint(event.pos):
                self.username_active = True
                self.password_active = False
            elif self.password_input.collidepoint(event.pos):
                self.username_active = False
                self.password_active = True
            else:
                self.username_active = False
                self.password_active = False

    def handle_keydown(self, event):
        if self.username_active:
            if event.type == pygame.KEYDOWN:
                self.error = ''
                if event.key == pygame.K_BACKSPACE:
                    self.lobby.username_text = self.lobby.username_text[:-1]
                else:
                    self.lobby.username_text += event.unicode
        if self.password_active:
            if event.type == pygame.KEYDOWN:
                self.error = ''
                if event.key == pygame.K_BACKSPACE:
                    self.lobby.password_text = self.lobby.password_text[:-1]
                else:
                    self.lobby.password_text += event.unicode

    def init_login_noti(self):
        self.login_noti = pygame.image.load('./assets/lobby/login_noti.png')
        self.login_noti = pygame.transform.scale(self.login_noti, (716, 342))
        self.login_noti_rect = self.login_noti.get_rect(bottomleft=(0, 707))

        self.login = pygame.image.load('./assets/lobby/login.png')
        self.login = pygame.transform.scale(self.login, (146, 50))
        self.login_rect = self.login.get_rect(center=(500, 575))

    def draw_login_noti(self):
        self.lobby.screen.blit(self.login_noti, self.login_noti_rect)
        self.lobby.screen.blit(self.login, self.login_rect)