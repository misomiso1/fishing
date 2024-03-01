import tkinter as tk

def draw_vertical_line(y=0):
    if y <= 400:
        # 線を描画
        canvas.create_line(200, 0, 200, y, fill="black")  # 下に垂直な線
        y += 5  # 線を5ピクセル下へ移動
        root.after(100, draw_vertical_line, y)  # 100ミリ秒後に再び描画

# ウィンドウの作成
root = tk.Tk()
root.title("ゆっくり下に線を引く")

# キャンバスの作成
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# ボタンの作成
draw_button = tk.Button(root, text="線を引く", command=draw_vertical_line)
draw_button.pack()

# ウィンドウを表示
root.mainloop()
