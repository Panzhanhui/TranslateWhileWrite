import tkinter as tk  # 要使用，先导入
from tkinter import ttk

import DrawingBoard  as board


class MainWindow:
    x = None
    y = None

    def onCreate(self, custom=False, width=None, height=None):
        global x, y

        window = tk.Tk()  # 创建一个窗口，因为后面还要用到所以用window这个变量来赋值，可以自行更改

        # 获取屏幕宽度和高度
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # print(screen_width, screen_height)
        # 设置窗口宽度和高度
        window_width = screen_width
        window_height = screen_height
        # 计算窗口左上角坐标使其居中
        x = ((window_width) // 3)
        y = ((window_height) // 3)

        window.title('translate any vocabularies while you write ')

        self.setScreenSize(window)
        window.bind('<Escape>', lambda event: self.exit_fullscreen(
            event=event, handle=window))


        b=board.Board(window)

        print('onCreate')
        window.mainloop()

    def setScreenSize(self, handle, width='-fullscreen', height=True):
        if height:
            handle.attributes(width, height)
        else:
            handle.geometry(f'{width}x{height}')

    def exit_fullscreen(self, handle, event=None):
        # 退出全屏
        handle.attributes('-fullscreen', False)
        # self.window.update()



    def setButton(self, handle, wannado, width, height):
        global x, y
        print(x, y)
        self.button = tk.Button(
            self.window, text='start to write', command=wannado, width=width, height=height)
        self.button.pack(side='top', padx=x, pady=y)

    def setStyleButton(self, handle, wannado, width, height, defaultStyle='TButton', padding=10, font=('Helvetica', 12), borderwidth=5, relief="raised", background="white"):
        global x, y
        style = ttk.Style()
        style.configure(defaultStyle,
                        padding=padding,
                        font=font,
                        borderwidth=borderwidth,
                        relief=relief,  # 设置按钮边框的样式，可以选择 "flat", "ridge", "groove", "solid", 等
                        background=background,  # 设置按钮的背景颜色
                        )

        # 创建带有样式的按钮
        self.button = ttk.Button(
            self.window, text='start to write', command=wannado, style=defaultStyle)
        self.button.pack(side='top', padx=x, pady=y)


window = MainWindow().onCreate()


# def clickme():
#     b = board()
#     b.setClearBtn()
#     b.setColorandWidth()
#     b.bindDevice()
#     b.canvas.mainloop()


# window.setStyleButton(clickme, 50, 25)
# window.LaunchScreen()
