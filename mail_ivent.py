import tkinter as tk
# ウィジェットを生成するメソッド
def create_widgets(self):
# ～省略～
    
    self.button = tk.Button(self, text="送信", command=lambda:self.click_event())
    self.button.grid(row=4, column=2, sticky=tk.E, pady=10)

def click_event(self):
    to = self.to_entry.get()
    subject = self.subject_entry.get()
    body = self.body_text.get()

    print(f"宛先:{to}")
    print(f"件名:{subject}")
    print(f"本文:{body}")