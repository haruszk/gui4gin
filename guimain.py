#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import tkinter

root = tkinter.Tk()
root.title(u"Silver Searcher GUI")
root.geometry("400x300")

def gobutton(event):
    searStr = searStrForm.get()
    searDir = searDirForm.get()
    print('ag -i ' + searStr + ' ' + searDir)

searStrLbl = tkinter.Label(text=u'検索文字列')
searStrLbl.place(x=30, y=4)
searStrForm = tkinter.Entry()
searStrForm.pack()

searDirLbl = tkinter.Label(text=u'検索対象パス')
searDirLbl.place(x=30, y=20)
searDirForm = tkinter.Entry()
searDirForm.pack()

searGoButton = tkinter.Button(text=u'検索GO')
searGoButton.bind("<Button-1>", gobutton)
searGoButton.place(x=130, y = 20)
searGoButton.pack()

root.mainloop()
