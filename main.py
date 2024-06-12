import tkinter as tk
import module1
import module2

def show_message():
    message = module1.get_message()
    print(message)

app = tk.Tk()
app.title("Complex App")

message_button = tk.Button(app, text="Show Message", command=show_message)
message_button.pack(pady=20)

app.mainloop()
