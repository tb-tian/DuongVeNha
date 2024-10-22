import pygame
import random
import os.path
from sys import exit

class Flashcards:
    def __init__(self, screen, clock):
        pygame.init()
        self.screen = screen
        self.clock = clock
        self.question_count = 3
        self.current_question = random.randint(1, self.question_count)
        self.state = 'question'

    def init_background(self):
        self.background = pygame.image.load('./assets/flashcards/background_flashcards.png').convert()
        self.background = pygame.transform.scale(self.background, (1000, 707))
        self.background_rect = self.background.get_rect(topleft = (0, 0))

    def draw_background(self):
        self.screen.blit(self.background, self.background_rect)

    def init_exit_button(self):
        self.exit_button = pygame.image.load('./assets/flashcards/exit.png').convert_alpha()
        self.exit_button = pygame.transform.scale(self.exit_button, (146, 50))
        self.exit_button_rect = self.exit_button.get_rect(topleft = (50, 30))

    def draw_exit_button(self):
        self.screen.blit(self.exit_button, self.exit_button_rect)

    def init_question(self, question_number):
        self.init_background()
        self.init_exit_button()

        self.question = pygame.image.load('./assets/flashcards/stages/questions/question_' + str(question_number) + '.png').convert_alpha()
        self.question = pygame.transform.scale(self.question, (598, 394))
        self.question_rect = self.question.get_rect(center = (500, 383))

    def draw_question(self):
        self.draw_background()
        self.draw_exit_button()

        self.screen.blit(self.question, self.question_rect)

    def init_answer(self, question_number):
        self.init_background()
        self.init_exit_button()

        self.answer = pygame.image.load('./assets/flashcards/stages/answers/answer_' + str(question_number) + '.png').convert_alpha()
        self.answer = pygame.transform.scale(self.answer, (598, 394))
        self.answer_rect = self.answer.get_rect(center = (500, 383))

    def draw_answer(self):
        self.draw_background()
        self.draw_exit_button()

        self.screen.blit(self.answer, self.answer_rect)

    def init_tip(self, question_number):
        if (os.path.isfile('./assets/flashcards/stages/tips/tip_' + str(question_number) + '.png')):
            self.tip = pygame.image.load('./assets/flashcards/stages/tips/tip_' + str(question_number) + '.png').convert_alpha()
            self.tip_rect = self.tip.get_rect(bottomright = (1000, 707))

    def draw_tip(self, question_number):
        if (os.path.isfile('./assets/flashcards/stages/tips/tip_' + str(question_number) + '.png')):
            self.screen.blit(self.tip, self.tip_rect)

    def update_qa_state(self, question_number):
        if (self.state == 'question'):
            self.init_question(question_number)
            self.draw_question()
        else:
            self.init_answer(question_number)
            self.draw_answer()
            self.init_tip(question_number)
            self.draw_tip(question_number)
                

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.question_rect.collidepoint(event.pos)):
                        if self.state == 'question':
                            self.state = 'answer'
                        else: self.state = 'question'
                    
                    if (self.exit_button_rect.collidepoint(event.pos)):
                        running = False
                        break
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.state = 'question'

                    k = random.randint(1, self.question_count)
                    while (k == self.current_question):
                        k = random.randint(1, self.question_count)
                    self.current_question = k

            self.update_qa_state(self.current_question)
                
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    screen = pygame.display.set_mode((1000, 707))
    clock = pygame.time.Clock()
    flashcards = Flashcards(screen, clock)
    flashcards.run()