import random as rnd
from .stock import Stock
from .figures import Figures
import time

class Game():
    AVAILABLE_MODES = ['COINCIDENCE', 'NO_COINCIDENCE']
    STOCK_OBJ = Stock()
    def __init__(self):
        self.counter = 0
        self.stock = self.STOCK_OBJ.figures
    def define_mode(self):
        return rnd.choice(self.AVAILABLE_MODES)
    
    def play_game(self):
        while self.counter > -1:
            current_mode = self.define_mode()
            if current_mode == 'COINCIDENCE':
                self.play_coincidence()
            else: 
                self.play_not_coincidence()
            rnd.shuffle(self.play_figures)
            self.print_cards()
            user_input = self.user_input()
            
            if self.stock[user_input-1].print_figure() == self.correct_figure.print_figure():
                self.counter = self.counter + 1
                print(f"\nCORRECT !! :) {self.counter} points")
                print(f'{"-"*48}\n\n')
                
            else:
                self.counter = -1
                print("\nFAIL :(")
                print(f"Your choice is {self.stock[user_input-1].print_figure()}. Correct one is {self.correct_figure.print_figure()}")
            
    def play_coincidence(self):
        self.play_figures = [rnd.choice(self.stock)]
        second_figure = Figures(random=True)
        while second_figure.color == self.play_figures[0].color or second_figure.shape == self.play_figures[0].shape or \
            self.STOCK_OBJ.check_figure_in_stock(second_figure) == True:
            second_figure = Figures(random=True)
            
        self.play_figures.append(second_figure)
        self.correct_figure = self.play_figures[0]
    
    def play_not_coincidence(self):
        self.play_figures = [Figures(random=True)]
        aux_colors_list = self.play_figures[0].AVAILABLE_COLORS.copy()
        aux_shapes_list = self.play_figures[0].AVAILABLE_SHAPES.copy()

        while self.STOCK_OBJ.check_figure_in_stock(self.play_figures[0]) == True:
            self.play_figures[0] = Figures(random=True)
            
        aux_colors_list, aux_shapes_list = self.STOCK_OBJ.filter_list(self.play_figures[0], 
                                                                      aux_colors_list, 
                                                                      aux_shapes_list
                                                                    )
        
        second_figure = Figures(random=True)
        while second_figure.color not in aux_colors_list or \
            second_figure.shape not in aux_shapes_list or \
            second_figure.color == self.play_figures[0].color or \
            second_figure.shape == self.play_figures[0].shape or \
            self.STOCK_OBJ.check_figure_in_stock(second_figure) == True:
  
            second_figure = Figures(random=True)
        self.play_figures.append(second_figure)
        
        aux_colors_list, aux_shapes_list = self.STOCK_OBJ.filter_list(self.play_figures[1], 
                                                                      aux_colors_list, 
                                                                      aux_shapes_list
                                                                    )
        self.correct_figure = Figures(color=aux_colors_list[0], shape=aux_shapes_list[0])    
    
    def print_cards(self):
        print('Figures:')
        for fig_index in range(0, len(self.stock)):
            print(f'\t{fig_index+1} - {self.stock[fig_index].print_figure()}')
    
        print('Cards:')
        for fig_index in range(0, len(self.play_figures)):
            print(f'\t{self.play_figures[fig_index].print_figure()}')
            
    def user_input(self):
        while True:
            try:
                choice = int(input('PLAY (1-5): '))
                if 1 <= choice <= 5:
                    break  # If the choice is within the valid range, exit the loop
                else:
                    print("Invalid input! Please enter a number between 1 and 5.")
            except ValueError:
                print("Wrong input! Valid inputs are 1, 2, 3, 4, 5")
        return choice