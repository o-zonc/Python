#Ch12 p.438 tk_ex01.py 참조
import tkinter as tk

win = tk.Tk()
win.title('파이썬 마지막 실시간') # 타이틀

lbl = tk.Label(win, text='원하는 방문자의 이름을 입력하세오')
lbl.grid(row=1, column=0, columnspan=2) # 그리드 첫째 줄
txt = tk.Entry(win)
txt.grid(row=1, column=0, columnspan=2, pady=6) # 그리드 둘째 줄

but1 = tk.Button(win, text='새창', width = 10)
but1.grid(row=3, column=0, padx=10, pady=5) # 그리드 세째 줄, 첫째 칸
but2 = tk.Button(win, text='취소', width = 10, command = win.destroy)
but2.grid(row=3, column=1, padx=10) # 그리드 세째 줄, 둘째 칸

win.mainloop()