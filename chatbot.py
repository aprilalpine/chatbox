import openai
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

openai.api_key = "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"
class Chatbot:

    def __init__(self, chat_frame, input_frame, button_frame, width, height, bg):
        self.width = width
        self.user_input_box = ScrolledText(input_frame, wrap=tk.WORD, width=int(width/3), height=int(height/6), padx=15, pady=15)
        self.user_input_box.pack(side="left", expand=False, padx=10, pady=15)
        self.button = tk.Button(button_frame, command=self.send_button, text="send")
        self.button.pack(side="left", padx=20)

        # sample labels, set row sizes
        empty1 = tk.Label(chat_frame, bg=bg, width=33)
        empty1.grid(row=0, column=0)
        print(width)

        empty2 = tk.Label(chat_frame, bg=bg, width=33)
        empty2.grid(row=0, column=1)
        self.chat_frame = chat_frame
        self.row = 0

    def send_button(self):
        user_input = self.get_entry()
        self.add_box(user_input, 1, "E")
        self.clear_entry()
        self.get_response(user_input)


    def get_entry(self):
        return self.user_input_box.get('1.0', tk.END).strip()

    def clear_entry(self):
        self.user_input_box.delete('1.0', tk.END)

    def add_box(self, text, col, side):
        box = tk.Label(self.chat_frame, text=text)
        box.config(wraplength=self.width/3)
        self.row += 1
        box.grid(row=self.row, column=col, padx=20, pady=5, sticky=side)

    def get_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[

                {"role": "user", "content": prompt}
            ]
        )
        answer = response['choices'][0]['message']['content']
        self.add_box(answer, 0, "W")

