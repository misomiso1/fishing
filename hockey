import tkinter as tk
import random

# ゲームの設定
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 80, 10
PADDLE_SPEED = 10
BALL_SIZE = 10
INITIAL_BALL_SPEED = 5
BALL_ACCELERATION = 0.5

class AirHockeyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("ソロ・エアホッケー")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # パドルとボールの初期化
        self.paddle = self.canvas.create_rectangle(WIDTH/2 - PADDLE_WIDTH/2, HEIGHT - PADDLE_HEIGHT - 10, 
                                                   WIDTH/2 + PADDLE_WIDTH/2, HEIGHT - 10, fill="white")
        self.ball = self.canvas.create_oval(WIDTH/2 - BALL_SIZE/2, HEIGHT/2 - BALL_SIZE/2,
                                            WIDTH/2 + BALL_SIZE/2, HEIGHT/2 + BALL_SIZE/2, fill="white")

        # ボールの初期速度と方向
        self.dx = random.choice([-1, 1]) * INITIAL_BALL_SPEED
        self.dy = random.choice([-1, 1]) * INITIAL_BALL_SPEED

        # イベントのバインディング
        self.canvas.bind("<Motion>", self.move_paddle)
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.start_game)

        # ゲームの状態とカウンターの初期化
        self.running = False
        self.counter = 0

    def move_paddle(self, event):
        # マウスの位置に応じてパドルを移動
        x = event.x - PADDLE_WIDTH/2
        if x < 0:
            x = 0
        elif x + PADDLE_WIDTH > WIDTH:
            x = WIDTH - PADDLE_WIDTH
        self.canvas.coords(self.paddle, x, HEIGHT - PADDLE_HEIGHT - 10, x + PADDLE_WIDTH, HEIGHT - 10)

    def start_game(self, event):
        # ゲームを開始する
        if not self.running:
            self.running = True
            self.game_loop()

    def game_loop(self):
        # ゲームループ
        if self.running:
            self.canvas.move(self.ball, self.dx, self.dy)
            ball_coords = self.canvas.coords(self.ball)
            paddle_coords = self.canvas.coords(self.paddle)

            # ボールが壁に当たったときの処理
            if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:
                self.dx *= -1
            if ball_coords[1] <= 0:
                self.dy *= -1

            # ボールがパドルに当たったときの処理
            if ball_coords[3] >= paddle_coords[1] and ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2]:
                self.dy *= -1
                self.dy += BALL_ACCELERATION * abs(self.dy) / self.dy  # ボールの速度を増加
                self.counter += 1  # カウンターを増やす

            # ボールが下に落ちたときの処理
            if ball_coords[3] >= HEIGHT:
                self.game_over()
                return

            self.root.after(20, self.game_loop)

    def game_over(self):
        # ゲームオーバー時の処理
        self.running = False
        self.canvas.create_text(WIDTH/2, HEIGHT/2, text=f"Game Over\n打ち返した回数: {self.counter}", fill="white", font=("Helvetica", 24))

def main():
    root = tk.Tk()
    game = AirHockeyGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
