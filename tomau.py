import pygame
from sys import exit

class ToMau:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 707))
        self.clock = pygame.time.Clock()
        self.state = 'game'
        self.color = 'white'
        self.init = False

    def init_background(self):
        self.init = True

        self.background = pygame.image.load('./assets/tomau/background.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft = (0, 0))

        self.arrow = pygame.image.load('./assets/tomau/picture/arrow.png').convert_alpha()
        self.arrow = pygame.transform.scale(self.arrow, (500, 500))
        self.arrow_rect = self.arrow.get_rect(center = (500, 450))
        self.arrow_mask = pygame.mask.from_surface(self.arrow)
        self.arrow_coloring = self.arrow_mask.to_surface()
        self.arrow_coloring.set_colorkey((0, 0, 0))
        
        self.bg = pygame.image.load('./assets/tomau/picture/bg.png').convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (500, 500))
        self.bg_rect = self.bg.get_rect(center = (500, 450))
        self.bg_mask = pygame.mask.from_surface(self.bg)
        self.bg_coloring = self.bg_mask.to_surface()
        self.bg_coloring.set_colorkey((0, 0, 0))

        self.outline = pygame.image.load('./assets/tomau/picture/outline.png').convert_alpha()
        self.outline = pygame.transform.scale(self.outline, (500, 500))
        self.outline_rect = self.outline.get_rect(center = (500, 450))

        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'white']
        self.color_buttons = []
        button_width = 50
        button_height = 50
        for i, color in enumerate(self.colors):
            button_surface = pygame.Surface((button_width, button_height))
            button_surface.fill(pygame.Color(color))
            button_rect = button_surface.get_rect(topleft=(10 + i * (button_width + 10), 10))
            self.color_buttons.append((button_surface, button_rect, color))
        
    def draw_background(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.arrow, self.arrow_rect)
        self.screen.blit(self.bg, self.bg_rect)
        self.screen.blit(self.arrow_coloring, self.arrow_rect)
        self.screen.blit(self.bg_coloring, self.bg_rect)
        self.screen.blit(self.outline, self.outline_rect)
        for button_surface, button_rect, color in self.color_buttons:
            self.screen.blit(button_surface, button_rect)
    
    def coloring(self, surface, color):
        surf_w, surf_h = surface.get_size()
        for x in range(surf_w):
            for y in range(surf_h):
                if surface.get_at((x, y)) != (0, 0, 0):
                    surface.set_at((x, y), pygame.Color(color))

    def run(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:

                    for button_surface, button_rect, color in self.color_buttons:
                        if button_rect.collidepoint(event.pos):
                            self.color = color
                            print(self.color)
                        
                    if(self.bg_rect.collidepoint(event.pos)):
                        pos_in_bg_mask = (event.pos[0] - self.bg_rect.left, event.pos[1] - self.bg_rect.top)
                        if(self.bg_mask.get_at(pos_in_bg_mask) == 1):
                            self.coloring(self.bg_coloring, self.color)
                            print("Background")
                    
                    if(self.arrow_rect.collidepoint(event.pos)):
                        pos_in_arrow_mask = (event.pos[0] - self.arrow_rect.left, event.pos[1] - self.arrow_rect.top)
                        if(self.arrow_mask.get_at(pos_in_arrow_mask) == 1):
                            self.coloring(self.arrow_coloring, self.color)
                            print("Arrow")
                    
                
            if self.init == False:
                self.init_background()
            self.draw_background()

            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    ToMau().run()
        