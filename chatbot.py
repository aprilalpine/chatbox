import openai
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image

openai.api_key = "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"


class Chatbot:

    def __init__(self, window, chat_frame, input_frame, button_frame, width, height, bg):
        self.bg = bg
        self.width = width
        self.user_input_box = ScrolledText(input_frame, wrap=tk.WORD, width=int(width/3), height=int(height/6), padx=15, pady=15)
        self.user_input_box.pack(side="left", expand=False, padx=10, pady=15)
        self.button = tk.Button(button_frame, bg=bg, command=self.send_button, text="send", font="Georgia")
        self.button.pack(side="left", padx=15)
        # bind enter key
        window.bind('<Return>', lambda event:self.send_button())
        tk.Label(chat_frame, bg=bg, width=5).grid(row=0, column=0)
        tk.Label(chat_frame, bg=bg, width=52).grid(row=0, column=1)
        tk.Label(chat_frame, bg=bg, width=8).grid(row=0, column=2)

        self.chat_frame = chat_frame
        self.row = 0

        self.user_avatar = ImageTk.PhotoImage(Image.open("resources/dog.png").resize((20, 20)))
        self.assistant_avatar = ImageTk.PhotoImage(Image.open("resources/cat.png").resize((20, 20)))

    def send_button(self):
        user_input = self.get_entry()
        self.add_box(user_input, "e", 2)
        self.clear_entry()
        self.get_response(user_input)

    def get_entry(self):
        return self.user_input_box.get('1.0', tk.END).strip()

    def clear_entry(self):
        self.user_input_box.delete('1.0', tk.END)

    def add_box(self, text, side, num=0):
        box = tk.Label(self.chat_frame, bg="white", text=text, font="Calibri")
        box.config(wraplength=self.width*2/3)
        box.grid(row=self.row, column=1, sticky=side, padx=10, pady=10)
        # avatar
        img = self.assistant_avatar
        if num == 2:
            img = self.user_avatar
        avatar = tk.Canvas(self.chat_frame, bg=self.bg, width=20, height=20)
        avatar.create_image(10, 10, anchor="center", image=img)
        avatar.grid(row=self.row, column=num, pady=10, sticky="n")
        self.row += 1

    def get_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content']
        self.add_box(answer, "w")

