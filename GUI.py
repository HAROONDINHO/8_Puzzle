import tkinter as tk
import time
from eightpuzzle import *
game = '436215087'
steps=A_star(game,manhattan)
window=tk.Tk()

for x in range(len(steps)):
    step = [int(h) for h in steps[x]]
    print(step)
    time.sleep(0.5)
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)
            frame.grid_columnconfigure(4, minsize=100)
            num=step.pop(0)
            if num == 0:
                label = tk.Label(master=frame)
            else:
                label = tk.Label(master=frame, text=f"{num}", font='Helvetica 18 bold')
            label.pack(padx=50,pady=50)
    window.update()

window.mainloop()




window.mainloop()

