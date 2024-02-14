# keylogger_GUI.py

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from keylogger_core import KeyloggerCore

class KeyloggerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger Interface")

        # Use ThemedTk for a more modern look
        self.themed_master = ThemedTk(theme="arc")  # You can experiment with other themes

        frame = ttk.Frame(self.themed_master)
        frame.pack(padx=20, pady=20)

        # Use modern icons for buttons
        record_icon = tk.PhotoImage(file="record_icon.png")
        stop_icon = tk.PhotoImage(file="stop_icon.png")
        mouse_icon = tk.PhotoImage(file="mouse_icon.png")
        keyboard_icon = tk.PhotoImage(file="keyboard_icon.png")

        # Record Keylogs Button
        self.record_button = ttk.Button(frame, text="Record Keylogs", command=self.start_keylogger, image=record_icon, compound=tk.LEFT)
        self.record_button.grid(row=0, column=0, padx=10, pady=10)

        # Stop Keylogger Button
        self.stop_button = ttk.Button(frame, text="Stop Keylogger", command=self.stop_keylogger, image=stop_icon, compound=tk.LEFT)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)
        self.stop_button["state"] = tk.DISABLED

        # Control Mouse Button
        self.mouse_button = ttk.Button(frame, text="Control Mouse", command=self.control_mouse, image=mouse_icon, compound=tk.LEFT)
        self.mouse_button.grid(row=1, column=0, padx=10, pady=10)

        # Control Keyboard Button
        self.keyboard_button = ttk.Button(frame, text="Control Keyboard", command=self.control_keyboard, image=keyboard_icon, compound=tk.LEFT)
        self.keyboard_button.grid(row=1, column=1, padx=10, pady=10)

        self.keylogger_core = KeyloggerCore()

    def start_keylogger(self):
        output_file = "keylogs.txt"
        self.keylogger_core.start_keylogger(output_file)
        self.record_button["state"] = tk.DISABLED
        self.stop_button["state"] = tk.NORMAL

    def stop_keylogger(self):
        self.keylogger_core.stop_keylogger()
        self.record_button["state"] = tk.NORMAL
        self.stop_button["state"] = tk.DISABLED

    def control_mouse(self):
        # Add your mouse control logic here
        pass

    def control_keyboard(self):
        # Add your keyboard control logic here
        pass

def run_gui():
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    run_gui()
