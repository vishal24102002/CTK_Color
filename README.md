# CTK_Color
## Introduction
the library that will be used with CustomTkinter for coloring text in textbox .

## syntax
<code>CTK_Color(text_box name,text,tag,Color to be applied)</code>

## use case
This code contains <code>demo.py</code> file in which the code 

### For Highlighting particular sentence
It provide color to the text in textbox untill you press enter or specify the end of the sentence in the code 
#### Code
<pre lang="sh">
import CTK_Color
import customtkinter as ctk

win=ctk.CTk()
text=ctk.CTkTextbox(win)
text.pack()
CTK_Color(text,"box","big","red").for_line()
win.mainloop()
</pre>
#### Pre-View 
<p align="center">
<img src="https://github.com/user-attachments/assets/371899cf-61e5-414b-81ee-1f68d26afd60" width=750/>
</p>

### For Highlighting particular words in textbox
#### Code
<pre lang="sh">
import CTK_Color
import customtkinter as ctk

win=ctk.CTk()

text=ctk.CTkTextbox(win)
text.pack()
CTK_Color(text,"for","bal","red").auto()
CTK_Color(text,"print","edit","orange").auto()
CTK_Color(text,"while","gang","blue").auto()
CTK_Color(text,"boxer","baler","green").auto()
win.mainloop()
</pre>
#### Pre-View
<p align="center">
<img src="https://github.com/user-attachments/assets/c0b27e21-c605-45c5-82fb-9a67ca66ca57" width=750/>
</p>
