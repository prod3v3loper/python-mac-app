import tkinter as tk

def say_hello():
    print("Hello, World!")

app = tk.Tk()
app.title("Simple App")

hello_button = tk.Button(app, text="Say Hello", command=say_hello)
hello_button.pack(pady=20)

app.mainloop()