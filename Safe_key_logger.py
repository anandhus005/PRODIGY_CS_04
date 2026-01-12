import tkinter as tk
from datetime import datetime

LOG_FILE = "key_log.txt"

def log_key(event):
    key = event.keysym
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} : {key}\n")

def main():
    root = tk.Tk()
    root.title("Safe Key Logger (Educational)")
    root.geometry("450x250")

    label = tk.Label(root, text="Type inside this window.\nKeys will be logged to key_log.txt",
                     font=("Arial", 12))
    label.pack(pady=20)

    text = tk.Text(root, height=6, width=45)
    text.pack()

    text.bind("<Key>", log_key)

    root.mainloop()

if __name__ == "__main__":
    main()
