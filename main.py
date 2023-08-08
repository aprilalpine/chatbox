from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from chatbot import Chatbot

class Main():

    def __init__(self):
        # new window
        self.window = tk.Tk()
        self.window.title("Chatbox")
        # set dimensions of chatbox
        self.width = self.window.winfo_screenwidth() / 4
        self.height = self.window.winfo_screenheight() / 2
        self.window.geometry("%dx%d" % (self.width, self.height))

        light_blue = "#cfe2f3"
        darker_blue = "#9fc5e8"
        # title frame
        frame_title = tk.Frame(self.window, height=self.height/8, width=self.width, bg=light_blue)
        frame_title.pack(side="top", fill="x")
        label_title = Label(frame_title, bg=light_blue, text="chatbox", font=("Georgia", 14), pady=10)
        label_title.pack()

        # chat frame
        frame_chat = VerticalScrolledFrame(self.window, darker_blue)
        frame_chat.pack(expand=True, fill="both")

        # for i in range(10):
        #     tk.Button(frame_chat.interior, text=f"Button {i}").pack(padx=10, pady=5)


        # input frame
        frame_input = tk.Frame(self.window, height=self.height/4, width=self.width*5/6, bg=light_blue)
        frame_input.pack(side="left")
        frame_input.pack_propagate(False)

        # button frame
        frame_button = tk.Frame(self.window, height=self.height/4, width=self.width/6, bg=light_blue)
        frame_button.pack(side="left")
        frame_button.pack_propagate(False)

        chatty = Chatbot(frame_chat.interior, frame_input, frame_button, self.width, self.height, darker_blue)

    def run(self):
        self.window.mainloop()


class VerticalScrolledFrame(ttk.Frame):
    def __init__(self, parent, bg, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = tk.Canvas(self, bd=0, bg=bg, highlightthickness=0,
                                width=200, height=300,
                                yscrollcommand=vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=self.canvas.yview)

        # Reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = tk.Frame(self.canvas, bg=bg)
        self.interior.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor=NW)

    def _configure_interior(self, event):
        # Update the scrollbars to match the size of the inner frame.
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion=(0, 0, size[0], size[1]))
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the canvas's width to fit the inner frame.
            self.canvas.config(width=self.interior.winfo_reqwidth())

    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # Update the inner frame's width to fill the canvas.
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())