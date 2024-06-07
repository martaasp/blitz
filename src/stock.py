
from .figures import Figures

class Stock:
    def __init__(self):
        self.figures = [
                Figures(color = Figures.AVAILABLE_COLORS[0], shape = Figures.AVAILABLE_SHAPES[0]), 
                Figures(color = Figures.AVAILABLE_COLORS[1], shape = Figures.AVAILABLE_SHAPES[1]), 
                Figures(color = Figures.AVAILABLE_COLORS[2], shape = Figures.AVAILABLE_SHAPES[2]),
                Figures(color = Figures.AVAILABLE_COLORS[3], shape = Figures.AVAILABLE_SHAPES[3]),
                Figures(color = Figures.AVAILABLE_COLORS[4], shape = Figures.AVAILABLE_SHAPES[4]) 
            ]
    
    def print_stock(self):
        for fig in self.figures:
            print(fig.print_figure())
        
    def check_figure_in_stock(self, figure):
        match = False
        for fig in self.figures:
            if figure.color == fig.color and figure.shape == fig.shape:
                match = True
                print("")
                break
        return match

    def remove_characteristic(self, idx, stock):
        stock.pop(idx)
        return stock
    
    def find_characteristic_index(self, characteristic, stock):
        return stock.index(characteristic)
        
    def remove_obj(self, idx, color_stock, shape_stock):
        return self.remove_characteristic(idx, color_stock), self.remove_characteristic(idx, shape_stock)
    
    def filter_list(self, current_figure, color_stock, shape_stock):
        current_color = current_figure.color
        current_shape = current_figure.shape
        
        color_idx = self.find_characteristic_index(current_color, color_stock)
        color_stock, shape_stock = self.remove_obj(color_idx, color_stock, shape_stock)
        
        shape_idx = self.find_characteristic_index(current_shape, shape_stock)
        color_stock, shape_stock  = self.remove_obj(shape_idx, color_stock, shape_stock)
        
        return color_stock, shape_stock