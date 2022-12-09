import pygame
import sys

from constants import *
from board import *
from move import Move
from game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        game = self.game
        screen = self.screen
        board = self.game.board
        mouse = self.game.mouse

        while True:
            # show methods
            game.show_background(screen)
            game.show_pieces(screen)
            game.show_last_move(screen) ##TODO

            # event checking
            for event in pygame.event.get():

                # checking for clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if piece selected
                    if mouse.picking:
                        mouse.update_mouse(event.pos)

                        released_row = mouse.mouseY // SQSIZE
                        released_col = mouse.mouseX // SQSIZE

                        # create possible move
                        initial = Square(mouse.initial_rank, mouse.initial_file)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)
                        print(move)

                        # valid move ?
                        if board.valid_move(move) == True:
                            # normal capture
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(mouse.piece, move)                            

                            # sounds
                            game.play_sound(captured)
                            # show methods
                            game.show_background(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            # next turn
                            game.next_turn()
                    
                        mouse.unpick_piece()

                    # if piece not selected
                    elif mouse.picking == False:
                        mouse.update_mouse(event.pos)

                        clicked_rank = mouse.mouseY // SQSIZE
                        clicked_file = mouse.mouseX // SQSIZE
                        print((clicked_rank, clicked_file))

                        # checking if square has piece
                        if board.squares[clicked_rank][clicked_file].has_piece():
                            piece = board.squares[clicked_rank][clicked_file].piece
                            if piece.colour == game.next_player:    
                                mouse.save_initial(event.pos)
                                mouse.pick_piece(piece)
                                print(piece)

                # checking for movement MAYBE NOT USEFUL!!!!
                elif event.type == pygame.MOUSEMOTION:
                    pass

                # checking for clicks release
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                
                
                # quitting
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.update()




main = Main()
main.mainloop()