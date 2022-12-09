class Move:

    file_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    rank_dict = {0:'1', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8'}

    def __init__(self, initial, final):
        # initial and final are squares
        self.initial = initial
        self.final = final

    def __str__(self):
        columnas = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
        filas = {0:'1', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8'}
        initial = (2, 4)
        final = (3, 5)

        initial_proc = f'{columnas[initial[0]]}{filas[initial[1]]}'
        final_proc = f'{columnas[final[0]]}{filas[final[1]]}'
        initial_proc+final_proc
        s = ''
        s += f'({self.initial.file}, {self.initial.rank})'
        s += f' -> ({self.final.file}, {self.final.rank})'
        return s

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final