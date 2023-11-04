import tkinter as tk
from tkinter import filedialog

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("400x400")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)
        
        self.brush_size = 7
        self.brush_color = "black"
        
        self.pen = False
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()
        
        self.save_button = tk.Button(root, text="Save", command=self.save_image)
        self.save_button.pack()

    def start_paint(self, event):
        self.pen = True
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.brush_size, y - self.brush_size,
                                x + self.brush_size, y + self.brush_size,
                                fill=self.brush_color, outline=self.brush_color)

    def paint(self, event):
        if self.pen:
            x, y = event.x, event.y
            self.canvas.create_oval(x - self.brush_size, y - self.brush_size,
                                    x + self.brush_size, y + self.brush_size,
                                    fill=self.brush_color, outline=self.brush_color)

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.canvas.postscript(file=file_path, colormode='color')
            self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
