import tkinter as tk # tkiner のインストール
from smtplib import SMTP 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

        self.button = tk.Button(self, text="送信", command=lambda:self.click_event())
        self.button.grid(row=4, column=2, sticky=tk.E, pady=10)

    def click_event(self):
        to = self.to_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get()
    
        self.send_mail(to=to, subject=subject, body=body)

    # メール送信処理
    def send_mail(self, to, subject, body):
        # 送信に必要な情報を定数で定義
        ID = "mail_address"
        PASS = "password"
        HOST = "smtp.gmail.com"
        PORT = 587

        # メール本文を設定
        msg = MIMEMultipart()
        msg.attach(MIMEText(body, "html"))

        # 件名、送信元アドレス、送信先アドレスを設定
        msg["Subject"] = subject
        msg["From"] = ID
        msg["To"] = to

        # SMTPサーバへ接続し、TLS通信開始
        server=SMTP(HOST, PORT)
        server.starttls()   # TLS通信開始

        server.login(ID, PASS) # ログイン認証処理

        server.send_message(msg)    # メール送信処理

        server.quit()       # TLS通信終了

if __name__ == "__main__":
    root = tk.Tk()
    Application(master=root)
    root.mainloop()