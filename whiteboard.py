import tkinter as tk
from tkinter.colorchooser import askcolor

class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard")

        self.color = "black"
        self.brush_size = 5

        # Create canvas
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Controls frame
        self.controls = tk.Frame(self.root)
        self.controls.pack(fill=tk.X)

        tk.Button(self.controls, text="Clear", command=self.clear_canvas).pack(side=tk.LEFT)
        tk.Button(self.controls, text="Color", command=self.choose_color).pack(side=tk.LEFT)

        self.brush_slider = tk.Scale(self.controls, from_=1, to=20, orient=tk.HORIZONTAL, label="Brush Size")
        self.brush_slider.set(self.brush_size)
        self.brush_slider.pack(side=tk.LEFT)

        self.last_x = None
        self.last_y = None

    def draw(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    fill=self.color,
                                    width=self.brush_slider.get(),
                                    capstyle=tk.ROUND, smooth=True)
        self.last_x = event.x
        self.last_y = event.y

    def reset(self, event):
        self.last_x = None
        self.last_y = None

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = askcolor(color=self.color)[1]
        if color:
            self.color = color

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()
