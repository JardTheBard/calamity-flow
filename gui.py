import tkinter as tk
import spotify_connect as conn
import json

class Gui(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.obtain_info()

    def obtain_info(self):
        user = {}
        user = conn.Connect('User Info').display_user_info()
        print(json.dumps(user, indent=4))

root = tk.Tk()
app = Gui(master=root)
app.mainloop()