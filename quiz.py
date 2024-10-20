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

font = pygame.font.Font(".\\Roboto-Medium.ttf", 25)

exit_button_image = pygame.image.load(".\\assets\\quiz\\exit.png") 
exit_button_image = pygame.transform.scale(exit_button_image, (150, 70)) 

class Question:
    def __init__(self, image_path, answers, correct_answer, note_image_path):
        self.image = pygame.image.load(image_path)
        self.answers = answers
        self.correct_answer = correct_answer
        if note_image_path is not None:
            self.note_image = pygame.image.load(note_image_path)
        else:
            self.note_image = None

class Game:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.state = "question"  # can be "question" or "note"
        self.selected_answer = None
        self.background = pygame.image.load(".\\assets\\quiz\\bg.png")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def handle_click(self, pos):
        if self.state == "question":
            for i in range(4):
                x = 150 + (i % 2) * 375
                y = 350 + (i // 2) * 150
                if pygame.Rect(x, y, 350, 100).collidepoint(pos):
                    self.selected_answer = i
                    return
            
            if self.selected_answer is not None:
                if self.selected_answer == self.questions[self.current_question].correct_answer:
                    # Check if the "Next" button is clicked
                    if pygame.Rect(800, 50, 160, 50).collidepoint(pos):
                        if hasattr(self.questions[self.current_question], 'note_image'):
                            self.state = "note"
                            self.selected_answer = None
                        else:
                            self.current_question += 1
                            if self.current_question >= len(self.questions):
                                self.current_question = 0
                            self.state = "question"
                            self.selected_answer = None
        elif self.state == "note":
            if pygame.Rect(800, 50, 160, 50).collidepoint(pos):
                self.current_question += 1
                if self.current_question >= len(self.questions):
                    self.current_question = 0
                self.state = "question"
                self.selected_answer = None

        # Check if the exit button is clicked
        if pygame.Rect(25, 35, 150, 70).collidepoint(pos):
            pygame.quit()
            exit()
    
    def render_text(self, text, x, y, max_width, max_height):
        font_size = 25
        font = pygame.font.Font(".\\Roboto-Medium.ttf", font_size)
        lines = text.split('\n')
        rendered_lines = []

        for line in lines:
            text_surface = font.render(line, True, BLACK)
            while text_surface.get_width() > max_width and font_size > 10:
                font_size -= 1
                font = pygame.font.Font(".\\Roboto-Medium.ttf", font_size)
                text_surface = font.render(line, True, BLACK)
            rendered_lines.append(text_surface)

        total_height = sum(line.get_height() for line in rendered_lines)
        while total_height > max_height and font_size > 10:
            font_size -= 1
            font = pygame.font.Font(".\\Roboto-Medium.ttf", font_size)
            rendered_lines = []
            for line in lines:
                text_surface = font.render(line, True, BLACK)
                while text_surface.get_width() > max_width and font_size > 10:
                    font_size -= 1
                    font = pygame.font.Font(".\\Roboto-Medium.ttf", font_size)
                    text_surface = font.render(line, True, BLACK)
                rendered_lines.append(text_surface)
            total_height = sum(line.get_height() for line in rendered_lines)

        start_y = y - total_height // 2

        for line in rendered_lines:
            text_rect = line.get_rect(center=(x, start_y + line.get_height() // 2))
            screen.blit(line, text_rect)
            start_y += line.get_height()
    
    def draw_question(self):
        screen.blit(self.background, (0, 0))
        question = self.questions[self.current_question]
        question.image = pygame.transform.scale(question.image, (800, 200))
        screen.blit(question.image, (110, 120))
        for i, answer in enumerate(question.answers):
            x = 150 + (i % 2) * 375
            y = 350 + (i // 2) * 150
            border_color = BLACK  # Default border color
            inner_color = PEACH  # Default inner color
            if self.selected_answer is not None:
                if i == self.selected_answer:
                    if self.selected_answer == question.correct_answer:
                        inner_color = GREEN
                    else:
                        inner_color = RED
            pygame.draw.rect(screen, border_color, (x - 5, y - 5, 360, 110), border_radius=20)  # Border
            pygame.draw.rect(screen, inner_color, (x, y, 350, 100), border_radius=20)  
            self.render_text(answer, x + 175, y + 50, 340, 100)  
        
        if self.selected_answer is not None and self.selected_answer == question.correct_answer:
            next_x, next_y = 800, 50
            pygame.draw.rect(screen, BLACK, (next_x - 10, next_y - 5, 170, 60), border_radius=20)  # Border
            pygame.draw.rect(screen, PEACH, (next_x - 5, next_y, 160, 50), border_radius=20)  
            next_text = font.render("Tiếp tục", True, BLACK)
            next_text_rect = next_text.get_rect(center=(next_x + 75, next_y + 25))
            screen.blit(next_text, next_text_rect)
        
        screen.blit(exit_button_image, (25, 35))
            
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
        screen.blit(exit_button_image, (25, 35))

    def draw_current_state(self):
        if self.state == "question":
            self.draw_question()
        elif self.state == "note":
            if self.questions[self.current_question].note_image is not None:
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

questions = [
    Question(".\\assets\\quiz\\question1\\question.png", ["Đỏ - Xanh - Vàng", "Đỏ - Xanh - Tím", "Đỏ - Hồng - Vàng", "Cam - Xanh - Vàng"], 0, ".\\assets\\quiz\\question1\\note.png"),
    Question(".\\assets\\quiz\\question2\\question.png", ["12", "7", "3", "6"], 2, ".\\assets\\quiz\\question2\\note.png"),
    Question(".\\assets\\quiz\\question3\\question.png", ["Không quan tâm", "Nhắc nhở ba mẹ\nđội nón bảo hiểm", "Chỉ cần em \n đội nón bảo hiểm thôi", "Nhắc ba mẹ mặc áo khoác"], 1, None),
    Question(".\\assets\\quiz\\question4\\question.png", ["Ôm chặt ba để không bị té", "Không quan tâm", "Nhắc nhở ba tuân thủ luật \n giao thông để tránh \n gặp tai nạn", "Cả 3 đáp án đều sai"], 2, None),
    Question(".\\assets\\quiz\\question5\\question.png", ["Qua đường ngay lập tức", "Chờ đến khi có người \n cùng muốn qua đường để \n đi chung", "Quan sát kĩ đến khi \n đường vắng xe rồi \n mới sang đường", "Bấm còi để mọi người chú ý"], 2, None),
    Question(".\\assets\\quiz\\question6\\question.png", ["Cùng các bạn đi dàn\nhàng ngang trên đường để\nngười lái xe dễ quan sát thấy", "Chỉ cần đi chậm vì \n xe sẽ tự né mình", "Đi bộ trên vỉa hè hoặc sát\nmép đường phía bên phải\n và luôn chú ý quan sát các \n phương tiện giao thông", "Chạy thật nhanh về \n nhà để an toàn"], 2, None),
    Question(".\\assets\\quiz\\question7\\question.png", ["Chở 2 người lớn ngồi sau", "Chở 1 người ngồi sau", "Chở 1 người lớn và 2 \n trẻ em dưới 11 tuổi ngồi sau", "Tất cả đáp án đều sai"], 0, None),
    Question(".\\assets\\quiz\\question8\\question.png", ["Đi bên phải theo chiều \n đi của mình", "Đi đúng phần đường quy định", "Chấp hành biển báo \n dành cho người đi bộ", "Tất cả các ý trên đều đúng"], 3, None),
    Question(".\\assets\\quiz\\question9\\question.png", ["Biển 1", "Biển 1 và 3", "Biển 2", "Biển 2 và 3"], 2, None),
    Question(".\\assets\\quiz\\question10\\question.png", ["Biển 1", "Biển 2", "Biển 1 và 3", "Biển 2 và 3"], 1, None)
]

if __name__ == "__main__":
    game = Game(questions)
    game.run()