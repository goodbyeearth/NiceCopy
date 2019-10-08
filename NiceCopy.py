'''
Concatenating all lines of the text. (Optional for removing digits.)
'''
from tkinter import *
import re


def concat_lines(remove_digit):
    original_text = root.clipboard_get()
    new_text = original_text.replace('\n', ' ').replace('\r', '')
    if remove_digit:
        new_text = re.sub(r'\d', '', new_text)
    root.clipboard_clear()
    root.clipboard_append(new_text)


root = Tk()
root.title("NiceCopy")
root.wm_attributes('-topmost', 1)


b = Button(root, text='Concatenating lines', command=lambda: concat_lines(remove_digit=False), width=18,
           height=4, activebackground='red', relief=GROOVE, bg='orange')
b.pack(side=LEFT)
b2 = Button(root, text='Concatenating lines\n&\nRemoving digits', command=lambda: concat_lines(remove_digit=True), width=18,
           height=4, activebackground='red', relief=GROOVE, bg='DarkOrange1')
b2.pack(side=RIGHT)

root.mainloop()
