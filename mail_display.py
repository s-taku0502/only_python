#画面の作成
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # 画面サイズとタイトルを設定
        master.geometry("300x200")
        master.title("簡易メール送信アプリ")

        self.create_widgets()

    # ウィジェットを生成するメソッド
    def create_widgets(self):
        self.label = tk.Label(self,text="簡易メール送信アプリ")
        self.label.grid(row=0, column=0, columnspan=3)

        self.to_label = tk.Label(self, text="宛先:")
        self.to_entry = tk.Entry(self, width=20)
        self.to_label.grid(row=1, column=0)
        self.to_entry.grid(row=1, column=1, columnspan=2)

        self.subject_label = tk.Label(self, text="件名:")
        self.subject_entry = tk.Entry(self, width=20)
        self.subject_label.grid(row=2, column=0)
        self.subject_entry.grid(row=2, column=1, columnspan=2)

        self.body_label = tk.Label(self, text="本文:")
        self.body_text = tk.Entry(self, width=20)
        self.body_label.grid(row=3, column=0)
        self.body_text.grid(row=3, column=1, columnspan=2)

        self.button = tk.Button(self, text="送信")
        self.button.grid(row=4, column=2, sticky=tk.E, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    Application(master=root)
    root.mainloop()