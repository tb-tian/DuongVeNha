import pygame

pygame.init()

# Set up display
WIDTH, HEIGHT = 1000, 707
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PEACH = (255, 218, 185)

font = pygame.font.Font("./Roboto-Medium.ttf", 25)


class Question:
    def __init__(self, image_path, answers, correct_answer, note_image_path):
        self.image = pygame.image.load(image_path)
        self.answers = answers
        self.correct_answer = correct_answer
        self.note_image = pygame.image.load(note_image_path)

class GiaiDo:
    def __init__(self):
        self.questions = [
            Question("./assets/quiz/question1/question.png", ["Đỏ - Xanh - Vàng", "Đỏ - Xanh - Tím", "Đỏ - Hồng - Vàng", "Cam - Xanh - Vàng"], 0, "./assets/quiz/question1/note.png")
        ]
        self.current_question = 0
        self.state = "question"  # can be "question" or "note"
        self.selected_answer = None
        self.background = pygame.image.load("./assets/quiz/bg.png")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def handle_click(self, pos):
        if self.state == "question":
            for i in range(4):
                x = 140 + (i % 2) * 375
                y = 360 + (i // 2) * 150
                if pygame.Rect(x, y, 350, 100).collidepoint(pos):
                    self.selected_answer = i
                    return
            
            if self.selected_answer is not None:
                if self.selected_answer == self.questions[self.current_question].correct_answer:
                    # Check if the "Next" button is clicked
                    if pygame.Rect(800, 50, 200, 50).collidepoint(pos):
                        self.state = "note"
                        self.selected_answer = None
        elif self.state == "note":
            if pygame.Rect(800, 50, 200, 50).collidepoint(pos):
                self.current_question += 1
                if self.current_question >= len(self.questions):
                    self.current_question = 0
                self.state = "question"
                self.selected_answer = None
    
    def draw_question(self):
        screen.blit(self.background, (0, 0))
        question = self.questions[self.current_question]
        question.image = pygame.transform.scale(question.image, (800, 200))
        screen.blit(question.image, (110, 120))
        for i, answer in enumerate(question.answers):
            x = 140 + (i % 2) * 375
            y = 360 + (i // 2) * 150
            border_color = BLACK  
            inner_color = PEACH  
            if self.selected_answer is not None:
                if i == self.selected_answer:
                    if self.selected_answer == question.correct_answer:
                        inner_color = GREEN
                    else:
                        inner_color = RED
            pygame.draw.rect(screen, border_color, (x - 5, y - 5, 360, 110), border_radius=20)  # Border
            pygame.draw.rect(screen, inner_color, (x, y, 350, 100), border_radius=20)  
            answer_text = font.render(answer, True, BLACK)
            text_rect = answer_text.get_rect(center=(x + 175, y + 50))  # Center the text
            screen.blit(answer_text, text_rect)
        
        if self.selected_answer is not None and self.selected_answer == question.correct_answer:
            next_x, next_y = 800, 50
            pygame.draw.rect(screen, BLACK, (next_x - 10, next_y - 5, 170, 60), border_radius=20)  # Border
            pygame.draw.rect(screen, PEACH, (next_x - 5, next_y, 160, 50), border_radius=20)  
            next_text = font.render("Tiếp tục", True, BLACK)
            next_text_rect = next_text.get_rect(center=(next_x + 75, next_y + 25))
            screen.blit(next_text, next_text_rect)
            
    def draw_note(self):
        screen.blit(self.background, (0, 0))
        question = self.questions[self.current_question]
        question.note_image = pygame.transform.scale(question.note_image, (900, 620))
        screen.blit(question.note_image, (45, 100))
        next_question_x, next_question_y = 800, 50
        pygame.draw.rect(screen, BLACK, (next_question_x - 10, next_question_y - 5, 170, 60), border_radius=20)  # Border
        pygame.draw.rect(screen, PEACH, (next_question_x - 5, next_question_y, 160, 50), border_radius=20)  
        next_question_text = font.render("Tiếp tục", True, BLACK)
        next_question_text_rect = next_question_text.get_rect(center=(next_question_x + 75, next_question_y + 25))
        screen.blit(next_question_text, next_question_text_rect)

    def draw_current_state(self):
        if self.state == "question":
            self.draw_question()
        elif self.state == "note":
            self.draw_note()
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
            
            self.draw_current_state()
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = GiaiDo()
    game.run()