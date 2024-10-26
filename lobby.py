import pygame
from sys import exit
import csv

from setting import Setting
from login import Login
from mode import Mode

class Lobby:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 707))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('DuongVeNha')
        self.state = 'lobby'
        self.init = False
        self.font = pygame.font.SysFont('Consolas', 32, True)
        self.username_text = ''
        self.password_text = ''

        self.settings = Setting(self)
        self.login = Login(self)
        self.mode = Mode(self)

    def init_lobby(self):
        self.background = pygame.image.load('./assets/lobby/background.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft = (0, 0))

        self.start = pygame.image.load('./assets/lobby/start.png')
        self.start = pygame.transform.scale(self.start, (245, 85))
        self.start_rect = self.start.get_rect(center = (500, 635))

        self.setting = pygame.image.load('./assets/lobby/setting.png')
        self.setting = pygame.transform.scale(self.setting, (59, 59))
        self.setting_rect = self.setting.get_rect(center = (940, 52))

        self.feedback = pygame.image.load('./assets/lobby/feedback.png')
        self.feedback = pygame.transform.scale(self.feedback, (65, 47))
        self.feedback_rect = self.feedback.get_rect(center = (943, 125))

        self.account = pygame.image.load('./assets/lobby/account.png')
        self.account = pygame.transform.scale(self.account, (68, 68))
        self.account_rect = self.account.get_rect(center = (942, 203))

        self.name = pygame.image.load('./assets/lobby/game_name.png')
        self.name = pygame.transform.scale(self.name, (424, 91))
        self.name_rect = self.name.get_rect(center = (500, 83))

        self.logo = pygame.image.load('./assets/lobby/logo.png')
        self.logo = pygame.transform.scale(self.logo, (292, 270))
        self.logo_rect = self.logo.get_rect(center = (500, 353))

        self.sign = pygame.image.load('./assets/lobby/sign.png')
        self.sign = pygame.transform.scale(self.sign, (253, 296))
        self.sign_rect = self.sign.get_rect(bottomright = (975, 725))
        self.friend_rect = pygame.Rect(780, 480, 130, 35)
        self.achievement_rect = pygame.Rect(760, 590, 185, 30)

    def draw_lobby(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.start, self.start_rect)
        self.screen.blit(self.setting, self.setting_rect)
        self.screen.blit(self.feedback, self.feedback_rect)
        self.screen.blit(self.account, self.account_rect)
        self.screen.blit(self.name, self.name_rect)
        self.screen.blit(self.logo, self.logo_rect)
        self.screen.blit(self.sign, self.sign_rect)


    def run(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(event.pos)
                    if(self.state == 'lobby'):
                        if(self.start_rect.collidepoint(event.pos)):
                            if(self.username_text != '' and self.password_text != ''):
                                print('mode')
                                self.state = 'mode'
                            else:
                                print('login_noti')
                                self.state = 'login_noti'
                        elif(self.setting_rect.collidepoint(event.pos)):
                            print('setting')
                            self.state = 'setting'
                        elif(self.feedback_rect.collidepoint(event.pos)):
                            print('feedback')
                        elif(self.account_rect.collidepoint(event.pos)):
                            print('account')
                        elif(self.friend_rect.collidepoint(event.pos)):
                            print('friend')
                        elif(self.achievement_rect.collidepoint(event.pos)):
                            print('achievement')

                    elif(self.state == 'mode'):
                        self.mode.handle_event(event)
                    
                    elif(self.state == 'setting'):
                        self.settings.handle_event(event)

                    elif(self.state == 'login'):
                        self.login.handle_event(event)
                    
                    elif self.state == 'login_noti':
                        if(self.login.login_noti_rect.collidepoint(event.pos)):
                            pass
                        else:
                            print('lobby')
                            self.state = 'lobby'
                        if(self.login.login_rect.collidepoint(event.pos)):
                            self.state = 'login'
                    
                if self.state == 'login' and self.init == True:
                    self.login.handle_keydown(event)
                    
            if(self.state == 'login'):
                if self.init == False: self.login.init_login()
                self.login.draw_login()
            
            if(self.state == 'lobby'):
                self.init_lobby()
                self.draw_lobby()    
            
            if(self.state == 'login_noti'):
                self.init_lobby()
                self.draw_lobby()
                self.login.init_login_noti()
                self.login.draw_login_noti()

            if(self.state == 'mode'):
                if(self.mode.rect_list[4] == 'right'):
                    self.mode.init_mode()
                    self.mode.draw_mode()
                elif(self.mode.rect_list[4] == 'left'):
                    pass
            
            if(self.state == 'setting'):
                self.settings.init_setting()
                self.settings.draw_setting()
            
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    lobby = Lobby()
    lobby.run()
