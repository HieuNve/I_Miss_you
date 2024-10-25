import random
import os
import pygame
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
import tkinter.font as tkFont

def create_window(message):
    window = ttk.Toplevel()
    window.title("Thông báo")
    window.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.ico'))

    # Tạo hình ảnh với font tùy chỉnh
    img = Image.new('RGB', (300, 100), color='#FFB6C1')
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'fonts', 'UVNVan_B.ttf'), 24)
    ImageDraw.Draw(img).text((10, 10), message, font=font, fill=(255, 255, 255))

    # Chuyển đổi hình ảnh sang định dạng Tkinter
    tk_image = ImageTk.PhotoImage(img)
    label = ttk.Label(window, image=tk_image)
    label.image = tk_image  # Giữ tham chiếu đến hình ảnh
    label.pack(padx=20, pady=20)

    # Đặt vị trí ngẫu nhiên cho cửa sổ
    window.geometry(f"+{random.randint(0, window.winfo_screenwidth() - 300)}+{random.randint(0, window.winfo_screenheight() - 200)}")
    window.configure(bg='#FFB6C1')

def create_windows(count=200, delay=50):
    if count > 0:
        create_window("Anh nhớ em!")
        root.after(delay, create_windows, count - 1, delay)

def start_creating_windows():
    pygame.mixer.init()  
    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "tranbonho.wav"))
    pygame.mixer.music.play()  
    create_windows()

# Tạo cửa sổ gốc với ttkbootstrap
root = ttk.Window(themename="cosmo")
root.title("Hello em!")
root.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.ico'))
root.geometry("600x400")
root.resizable(False, False)

# Ngăn chặn nhấp đúp để mở rộng cửa sổ
root.bind("<Double-Button-1>", lambda event: None)

# Đặt vị trí cửa sổ chính ở giữa màn hình
x = (root.winfo_screenwidth() // 2) - 300
y = (root.winfo_screenheight() // 2) - 200
root.geometry(f"600x400+{x}+{y}")

# Thiết lập hình nền
bg_image = ImageTk.PhotoImage(Image.open('bg.png').resize((600, 400), Image.LANCZOS))
ttk.Label(root, image=bg_image).place(relwidth=1, relheight=1)

# Tạo style cho nút
style = ttk.Style()
font = tkFont.Font(family="UVN Van", size=24, weight="bold")
style.configure('Custom.TButton',
                font=font,
                foreground='white',
                background='#FF69B4',
                borderwidth=0,
                relief='flat',
                padding=10)

style.map('Custom.TButton',
          background=[('active', '#FF1493'), ('pressed', '#C71585')])

# Tạo nút để bắt đầu tạo cửa sổ
ttk.Button(root, text="Nhấn zô đii!", command=start_creating_windows, style='Custom.TButton', width=20).place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
