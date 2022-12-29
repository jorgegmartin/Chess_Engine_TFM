class Move:

    def __init__(self, initial, final):
        # initial and final are squares
        self.initial = initial
        self.final = final

    def __str__(self):
        file_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
        rank_dict = {0:'8', 1:'7', 2:'6', 3:'5', 4:'4', 5:'3', 6:'2', 7:'1'}

        initial_proc = f'{file_dict[self.initial.file]}{rank_dict[self.initial.rank]}'
        final_proc = f'{file_dict[self.final.file]}{rank_dict[self.final.rank]}'
        
        s = ''
        s += f'{initial_proc+final_proc}'
        #s += f' -> ({self.final.file}, {self.final.rank})'
        return s

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final