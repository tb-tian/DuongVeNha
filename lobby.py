import pygame
from sys import exit

# pygame.init()
# pygame.display.set_caption('DuongVeNha')
# clock = pygame.time.Clock()



class Lobby:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 707))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('DuongVeNha')
        self.state = 'lobby'
        self.rect_list = [0, 0, 0, 0, 'right']

    def init_lobby(self):
        self.background = pygame.image.load('./assets/background.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft = (0, 0))

        self.start = pygame.image.load('./assets/start.png')
        self.start = pygame.transform.scale(self.start, (245, 85))
        self.start_rect = self.start.get_rect(center = (500, 635))

        self.setting = pygame.image.load('./assets/setting.png')
        self.setting = pygame.transform.scale(self.setting, (59, 59))
        self.setting_rect = self.setting.get_rect(center = (940, 52))

        self.feedback = pygame.image.load('./assets/feedback.png')
        self.feedback = pygame.transform.scale(self.feedback, (65, 47))
        self.feedback_rect = self.feedback.get_rect(center = (943, 125))

        self.account = pygame.image.load('./assets/account.png')
        self.account = pygame.transform.scale(self.account, (68, 68))
        self.account_rect = self.account.get_rect(center = (942, 203))

        self.name = pygame.image.load('./assets/game_name.png')
        self.name = pygame.transform.scale(self.name, (424, 91))
        self.name_rect = self.name.get_rect(center = (500, 83))

        self.logo = pygame.image.load('./assets/logo.png')
        self.logo = pygame.transform.scale(self.logo, (292, 270))
        self.logo_rect = self.logo.get_rect(center = (500, 353))

        self.sign = pygame.image.load('./assets/sign.png')
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
        

    def init_mode(self):
        self.background = pygame.image.load('./assets/mode.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft = (0, 0))

        self.flashcards = pygame.image.load('./assets/flashcards.png')
        self.flashcards = pygame.transform.scale(self.flashcards, (206, 206))
        self.flashcards_rect = self.flashcards.get_rect(center = (248, 375))

        self.giaido = pygame.image.load('./assets/giaido.png')
        self.giaido = pygame.transform.scale(self.giaido, (206, 206))
        self.giaido_rect = self.giaido.get_rect(center = (500, 375))

        self.tomau = pygame.image.load('./assets/tomau.png')
        self.tomau = pygame.transform.scale(self.tomau, (206, 206))
        self.tomau_rect = self.tomau.get_rect(center = (751, 375))

        self.right_arrow = pygame.image.load('./assets/right_arrow.png')
        self.right_arrow = pygame.transform.scale(self.right_arrow, (83, 107))
        self.right_arrow_rect = self.right_arrow.get_rect(center = (930, 375))

        self.rect_list = [self.flashcards_rect, self.giaido_rect, self.tomau_rect, self.right_arrow_rect, 'right']


    def draw_mode(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.flashcards, self.flashcards_rect)
        self.screen.blit(self.giaido, self.giaido_rect)
        self.screen.blit(self.tomau, self.tomau_rect)
        self.screen.blit(self.right_arrow, self.right_arrow_rect)

    def init_setting(self):
        self.background = pygame.image.load('./assets/background.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft = (0, 0))

        self.name = pygame.image.load('./assets/game_name.png')
        self.name = pygame.transform.scale(self.name, (424, 91))
        self.name_rect = self.name.get_rect(center = (500, 83))

        self.bulletin_board = pygame.image.load('./assets/bulletin_board.png').convert_alpha()
        self.bulletin_board = pygame.transform.scale(self.bulletin_board, (573, 488))
        self.bulletin_board_rect = self.bulletin_board.get_rect(center = (500, 373))

        
    def draw_setting(self):
        
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.name, self.name_rect)
        self.screen.blit(self.bulletin_board, self.bulletin_board_rect)


    def change_mode(self, direction):
        if direction == 'right':
            # del self.flashcards
            # del self.flashcards_rect
            # del self.giaido
            # del self.giaido_rect
            # del self.tomau
            # del self.tomau_rect
            # del self.right_arrow
            # del self.right_arrow_rect

            self.background = pygame.image.load('./assets/mode.png').convert()
            self.background = pygame.transform.scale(self.background, (1000, 707))
            self.background_rect = self.background.get_rect(topleft = (0, 0))

            self.left_arrow = pygame.image.load('./assets/left_arrow.png')
            self.left_arrow = pygame.transform.scale(self.left_arrow, (83, 107))
            self.left_arrow_rect = self.left_arrow.get_rect(center = (70, 375))

            self.divenha = pygame.image.load('./assets/divenha.png')
            self.divenha = pygame.transform.scale(self.divenha, (206, 206))
            self.divenha_rect = self.divenha.get_rect(center = (248, 375))

            self.dieukhienxe = pygame.image.load('./assets/dieukhienxe.png')
            self.dieukhienxe = pygame.transform.scale(self.dieukhienxe, (206, 206))
            self.dieukhienxe_rect = self.dieukhienxe.get_rect(center = (500, 375))

            self.giaimamecung = pygame.image.load('./assets/giaimamecung.png')
            self.giaimamecung = pygame.transform.scale(self.giaimamecung, (206, 206))
            self.giaimamecung_rect = self.giaimamecung.get_rect(center = (751, 375))

            self.screen.blit(self.background, self.background_rect)
            self.screen.blit(self.divenha, self.divenha_rect)
            self.screen.blit(self.dieukhienxe, self.dieukhienxe_rect)
            self.screen.blit(self.giaimamecung, self.giaimamecung_rect)
            self.screen.blit(self.left_arrow, self.left_arrow_rect)

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



    def run(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.state == 'lobby'):
                        if(self.start_rect.collidepoint(event.pos)):
                            del self.background
                            del self.background_rect
                            del self.start
                            del self.start_rect
                            del self.setting
                            del self.setting_rect
                            del self.feedback
                            del self.feedback_rect
                            del self.account
                            del self.account_rect
                            del self.name
                            del self.name_rect
                            del self.logo
                            del self.logo_rect
                            
                            print('mode')
                            self.state = 'mode'
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
                        if(self.rect_list[0].collidepoint(event.pos) and self.rect_list[4] == 'right'):
                            print('flashcards')
                        elif(self.rect_list[1].collidepoint(event.pos) and self.rect_list[4] == 'right'):
                            print('giaido')
                        elif(self.rect_list[2].collidepoint(event.pos) and self.rect_list[4] == 'right'):
                            print('tomau')
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
                        
            
            if(self.state == 'lobby'):
                self.init_lobby()
                self.draw_lobby()    
            
            if(self.state == 'mode'):
                if(self.rect_list[4] == 'right'):
                    self.init_mode()
                    self.draw_mode()
                elif(self.rect_list[4] == 'left'):
                    pass
            
            if(self.state == 'setting'):
                
                self.init_setting()
                self.draw_setting()
            
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    lobby = Lobby()
    lobby.run()
