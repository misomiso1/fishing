import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("キャンバス作成")

# キャンバスの作成
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# ウィンドウを表示
root.mainloop()
