from tkinter import *
import utils
import settings
from cellss import Cell
root=Tk()
#override the settings
root.configure(bg="black")
root.geometry('1440x720')
root.title('Minesweeper')
root.resizable(False, False)

top_frame=Frame(
    root,
    bg='black',
    width=1440,
    height=180
)
top_frame.place(x=0, y=0)

left_frame=Frame(
    root, 
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75),

)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame=Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c= Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=10, y=0
) 

Cell.randomize_mines()

#window running
root.mainloop()