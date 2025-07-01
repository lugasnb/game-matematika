import pygame
import sys
import random
import os
import json

# Inisialisasi Pygame
pygame.init()
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Game Matematika")
clock = pygame.time.Clock()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)

# Font
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 32)

# File untuk menyimpan riwayat skor
HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

history = load_history()

# Fungsi untuk membuat soal berdasarkan level (ramah untuk anak SD)
def generate_question(level):
    if level == "Mudah":
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(['+', '-'])
    elif level == "Sedang":
        a, b = random.randint(2, 10), random.randint(2, 10)
        op = random.choice(['+', '-', '*'])
    elif level == "Sulit":
        b = random.randint(1, 10)
        correct = random.randint(1, 10)
        op = random.choice(['+', '-', '*', '/'])
        if op == '/':
            a = b * correct
        else:
            a = random.randint(1, 20)
    else:
        a, b, op = 1, 1, '+'

    question = f"{a} {op} {b}"
    answer = eval(question)
    return question, round(answer)

# UI Level dan batas soal
levels = ["Mudah", "Sedang", "Sulit"]
level_limits = {"Mudah": 10, "Sedang": 15, "Sulit": 20}
current_level = None
user_answer = ''
question = ''
correct_answer = 0
score = 0
status = ''
question_count = 0
player_name = ''
waiting_for_name = False
name_input = ''
pending_level = None
show_welcome = True

# Fungsi menggambar teks
def draw_text(text, x, y, size=48, color=BLACK, center=False):
    f = pygame.font.SysFont(None, size)
    img = f.render(text, True, color)
    if center:
        rect = img.get_rect(center=(x, y))
        screen.blit(img, rect)
    else:
        screen.blit(img, (x, y))

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif show_welcome:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                start_button_x = screen_width // 2 - 150
                start_button_y = screen_height // 2 + 50
                if start_button_x <= mx <= start_button_x + 300 and start_button_y <= my <= start_button_y + 60:
                    show_welcome = False
        elif waiting_for_name:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name_input.strip():
                    player_name = name_input.strip()
                    name_input = ''
                    waiting_for_name = False
                    current_level = pending_level
                    question, correct_answer = generate_question(current_level)
                    user_answer = ''
                    status = ''
                    score = 0
                    question_count = 0
                elif event.key == pygame.K_BACKSPACE:
                    name_input = name_input[:-1]
                else:
                    name_input += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if current_level is None and not waiting_for_name:
                for i, lvl in enumerate(levels):
                    button_width = 300
                    button_height = 60
                    button_x = screen_width // 2 - button_width // 2
                    button_y = 180 + i * (button_height + 40)
                    if button_x <= mx <= button_x + button_width and button_y <= my <= button_y + button_height:
                        pending_level = lvl
                        waiting_for_name = True
                        name_input = ''
                exit_button_x = screen_width - 170
                exit_button_y = screen_height - 70
                if exit_button_x <= mx <= exit_button_x + 150 and exit_button_y <= my <= exit_button_y + 50:
                    running = False
            else:
                if screen_width - 170 <= mx <= screen_width - 20 and screen_height - 70 <= my <= screen_height - 20:
                    current_level = None

        elif event.type == pygame.KEYDOWN and current_level:
            if event.key == pygame.K_RETURN:
                try:
                    if int(user_answer) == correct_answer:
                        status = 'Benar!'
                        score += 1
                    else:
                        status = f'Salah! Jawaban: {correct_answer}'
                    question_count += 1
                    if question_count >= level_limits[current_level]:
                        status += f" | Selesai! Skor akhir: {score}/{level_limits[current_level]}"

                        existing = [h for h in history if h['nama'] == player_name and h['level'] == current_level]
                        if existing:
                            best = max(score, existing[0]['skor'])
                            history = [h for h in history if not (h['nama'] == player_name and h['level'] == current_level)]
                            history.append({"nama": player_name, "level": current_level, "skor": best})
                        else:
                            history.append({"nama": player_name, "level": current_level, "skor": score})

                        save_history(history)
                        current_level = None
                    else:
                        question, correct_answer = generate_question(current_level)
                    user_answer = ''
                except:
                    status = 'Masukkan angka valid'
            elif event.key == pygame.K_BACKSPACE:
                user_answer = user_answer[:-1]
            elif event.unicode.isnumeric() or (event.unicode == '-' and user_answer == ''):
                user_answer += event.unicode

    if show_welcome:
        draw_text("Selamat Datang di Game Matematika!", screen_width // 2, screen_height // 2 - 50, 60, BLACK, center=True)
        pygame.draw.rect(screen, GREEN, (screen_width // 2 - 150, screen_height // 2 + 50, 300, 60), border_radius=15)
        draw_text("Mulai", screen_width // 2, screen_height // 2 + 80, 36, WHITE, center=True)
    elif waiting_for_name:
        draw_text("Masukkan Nama Pemain:", screen_width // 2, 100, 48, center=True)
        draw_text(name_input + '|', screen_width // 2, 180, 48, RED, center=True)
    elif current_level is None:
        draw_text("Pilih Level:", screen_width // 2, 110, center=True)
        for i, lvl in enumerate(levels):
            button_width = 300
            button_height = 60
            button_x = screen_width // 2 - button_width // 2
            button_y = 180 + i * (button_height + 40)
            pygame.draw.rect(screen, GREEN, (button_x, button_y, button_width, button_height), border_radius=15)
            draw_text(lvl, screen_width // 2, button_y + button_height // 2, 36, WHITE, center=True)
        pygame.draw.rect(screen, RED, (screen_width - 170, screen_height - 70, 150, 50), border_radius=10)
        draw_text("Keluar", screen_width - 95, screen_height - 45, 28, WHITE, center=True)

        if status:
            draw_text(status, screen_width // 2, screen_height - 100, 32, GREEN if 'Benar' in status or 'Selesai' in status else RED, center=True)
    else:
        draw_text(f"Level: {current_level}", 20, 20, 36)
        draw_text(f"Soal: {question_count + 1}/{level_limits[current_level]}", screen_width // 2, 80, 36, center=True)
        draw_text(f"Score: {score}", screen_width - 150, 20, 36)
        draw_text(question, screen_width // 2, 200, 64, BLACK, center=True)
        draw_text(user_answer, screen_width // 2, 280, 64, RED, center=True)
        draw_text(status, screen_width // 2, 360, 36, GREEN if 'Benar' in status else RED, center=True)

        draw_text("Ranking:", 20, 80, 28, BLACK)
        filtered = [h for h in history if h['level'] == current_level]
        top_scores = sorted(filtered, key=lambda x: x['skor'], reverse=True)[:3]
        colors = [GOLD, SILVER, BRONZE]
        for k, entry in enumerate(top_scores):
            msg = f"{k+1}. {entry['nama']} - Skor: {entry['skor']}"
            draw_text(msg, 20, 120 + k * 30, 26, colors[k] if k < len(colors) else BLACK)

        draw_text("Tekan ENTER untuk submit", screen_width // 2, screen_height - 120, 28, BLACK, center=True)
        draw_text("Backspace untuk hapus | ESC untuk keluar", screen_width // 2, screen_height - 90, 28, BLACK, center=True)

        pygame.draw.rect(screen, RED, (screen_width - 170, screen_height - 70, 150, 50), border_radius=10)
        draw_text("Kembali", screen_width - 95, screen_height - 45, 28, WHITE, center=True)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
