import tkinter as tk

def create_hello_box():
    window = tk.Tk()
    window.title("Hello Box")

    label = tk.Label(window, text="Hello!", borderwidth=2, relief="solid")
    label.pack(padx=20, pady=20) 

    window.mainloop()

if __name__ == "__main__":
    create_hello_box()
