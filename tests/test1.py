from CTK_Color import CTK_Color
import customtkinter as ctk

win = ctk.CTk()
text = ctk.CTkTextbox(win)
text.pack()
CTK_Color(text, "box", "big", "red").for_line()
win.mainloop()
