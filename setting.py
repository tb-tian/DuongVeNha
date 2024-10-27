import pygame

class Setting:
    def __init__(self, lobby):
        self.lobby = lobby

    def init_setting(self):
        self.background = pygame.image.load('./assets/setting/background.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft=(0, 0))

        self.name = pygame.image.load('./assets/setting/game_name.png')
        self.name = pygame.transform.scale(self.name, (424, 91))
        self.name_rect = self.name.get_rect(center=(500, 83))

        self.bulletin_board = pygame.image.load('./assets/setting/bulletin_board.png').convert_alpha()
        self.bulletin_board = pygame.transform.scale(self.bulletin_board, (573, 488))
        self.bulletin_board_rect = self.bulletin_board.get_rect(center=(500, 373))

        self.exit = pygame.image.load('./assets/setting/exit.png')
        self.exit = pygame.transform.scale(self.exit, (146, 50))
        self.exit_rect = self.exit.get_rect(center=(500, 587))

    def draw_setting(self):
        self.lobby.screen.blit(self.background, self.background_rect)
        self.lobby.screen.blit(self.name, self.name_rect)
        self.lobby.screen.blit(self.bulletin_board, self.bulletin_board_rect)
        self.lobby.screen.blit(self.exit, self.exit_rect)

    def handle_event(self, event):
        if self.exit_rect.collidepoint(event.pos):
            self.lobby.state = 'lobby'
