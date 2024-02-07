import tkinter as tk
from tkinter import ttk


queue = []
position = [0]*2
status = 1
points=[]

class Board ():

    def __init__(self, handle) -> None:
        # super().__init__()
        # self.board = handle.Tk()
        self.canvas = tk.Canvas(handle, width=500, height=500, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.setClearBtn(handle)
        self.setColorandWidth()
        self.bindDevice()

    def setClearBtn(self, handle):
        # 创建清除按钮
        clear_button = ttk.Button(
            handle, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.BOTTOM)

    def setColorandWidth(self):
        # 设置画笔颜色和宽度
        self.pen_color = "black"
        self.pen_width = 2

    def bindDevice(self, device="<B1-Motion>", reset_device="<ButtonRelease-1>"):
        
        # 绑定鼠标事件
        self.canvas.bind(device, self.paint)
        self.canvas.bind(reset_device, self.reset)
        

    def draw_points_and_lines(self,canvas, points):
        
        # 连线
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            canvas.create_line(x1, y1, x2, y2, fill="black")
        
    def paint(self, event):
        # global queue
        global points
        
        # print(f"x:{event.x},y:{event.y}")
        x1, y1 = (event.x - 0.01), (event.y - 0.01)
        x2, y2 = (event.x + 0.1), (event.y + 0.1)
        points.append((x1,y1))
        # points.append((x2,y2))
        # queue.append(f"{event.x}+{event.y}")
        self.canvas.create_oval(
            x1, y1, x2, y2, fill=self.pen_color, width=self.pen_width)
        # self.canvas.create_line(event.x,event.y,event.x+5,event.y)
        # self.draw_points_and_lines(self.canvas,points)
        # points=[]

    def reset(self, event):
        self.canvas.create_line(
            event.x, event.y, event.x, event.y, fill=self.pen_color, width=self.pen_width)

    def clear_canvas(self):
        self.canvas.delete("all")
