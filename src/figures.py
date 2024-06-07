from .colors import Colors
import random as rnd

class Figures():
    AVAILABLE_COLORS = [Colors.white, Colors.green, Colors.yellow, Colors.blue, Colors.red]
    AVAILABLE_SHAPES = ['ghost', 'bottle', 'mouse', 'book', 'chair']
    
    def __init__(self, random=False,color=None, shape=None):
        if random == True: 
            color = rnd.choice(self.AVAILABLE_COLORS)
            shape = rnd.choice(self.AVAILABLE_SHAPES)
        if color in self.AVAILABLE_COLORS:
            self.color = color
        else: 
            raise Exception(f"Color '{color}' is not in the list of available colors {self.AVAILABLE_COLORS}")
        if shape in self.AVAILABLE_SHAPES:
            self.shape = shape
        else: 
            raise Exception(f"Shape '{shape}' is not in the list of available shapes {self.AVAILABLE_SHAPES}")
               
    def print_figure(self):
        #color = 'Colors.'+self.color.upper()
        return f'{self.color} {self.shape}{Colors.default}'
        #return f'{color} - {message}{Colors.DEFAULT}\n'
    
    

