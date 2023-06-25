from tkinter import Button, Label
import random
import settings
class Cell:
    all=[]
    cell_count= settings.CELL_COUNT
    cell_count_label_object=None
    def __init__(self,x,y, is_mine=False):
        self.is_mine=is_mine
        self.x=x
        self.y=y
        self.is_opened=False
        self.cell_btn_object=None 

        Cell.all.append(self) #to access class methods within the class itself Cell.all is used
        #The objects are successively appended to the last of the Cell.all list
    
    def create_btn_object(self, location):
        btn=Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object=btn #can be understood as an alias/ variable 

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            if self.surrounded_cells_mines_length==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell
    @property
    def surrounded_cells(self):
        cells=[
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y+1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1)
        ]
        cells= [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count-=1
            print(self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length))

                #to replace the Cell Count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=
                f"Cells left: {Cell.cell_count}"
                ) 
        self.is_opened=True
    
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
    
    def right_click_actions(self, event):
        print(event)

    @staticmethod
    def randomize_mines():
        
        picked_cells=random.sample(
            Cell.all,
            settings.MINES_COUNT)
        for picked_cell in picked_cells:
                picked_cell.is_mine=True
    
    @staticmethod
    def create_cell_count_label(location): #no need for self because it is not ana instance method
        lbl= Label(
            location,
            text=f"Cells left: {Cell.cell_count}",
            width=12,
            height=6,
            font=("", 37)
        )
        Cell.cell_count_label_object=lbl

    #this method is set static because it is not needed to reiterate it for every cell instance but for the use case of the class as a whole

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"