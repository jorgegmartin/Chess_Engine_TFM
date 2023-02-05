import pygame
import sys

from constants import *
from board import *
from move import Move
from game import Game
import chess
import chess.engine
from engine import Engine


class Main:

    def __init__(self):
        pygame.init()
        self.current_board = chess.Board()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()
        self.engine = Engine()
        #self.current_player = self.game.next_player

    def mainloop(self):

        game = self.game
        screen = self.screen
        board = self.game.board
        mouse = self.game.mouse
        current_board = self.current_board
        # current_player = self.game.next_player
        calculating_param = 0
        engine = self.engine

        while True:
            # show methods
            game.show_background(screen)
            game.show_pieces(screen)
            game.show_last_move(screen)
            
            current_player = self.game.next_player

            if current_player == 'black':
                game.show_background(screen)
                game.show_pieces(screen)
                game.show_last_move(screen)
                if calculating_param == 0:
                    calculating_param = 1
                    print('motor encendido')
                    move_ai = engine.get_ai_move(current_board, 1) 
                    print(move_ai)

                    # create possible move
                    initial = Square(7-chess.square_rank(move_ai.from_square), chess.square_file(move_ai.from_square))
                    final = Square(7-chess.square_rank(move_ai.to_square), chess.square_file(move_ai.to_square))
                    test_move = Move(initial, final)
                    print(test_move)

                    # normal capture
                    print('initial rank', initial.rank)
                    print('initial file', initial.file)
                    print('final rank', final.rank)
                    print('final file', final.file)                        
                    print('initial piece', initial.has_piece())
                    print('final piece', final.has_piece())
                    print('initial?', board.squares[initial.rank][initial.file].has_piece())

                    black_piece = board.squares[initial.rank][initial.file].piece
                    captured = board.squares[final.rank][final.file].has_piece()
                    board.move(black_piece, test_move)                            

                    # engine.square_to_index(move_ai))
                    current_board.push_uci(str(move_ai))


                    # sounds
                    game.play_sound(captured)
                    # show methods
                    game.show_background(screen)
                    game.show_last_move(screen)
                    game.show_pieces(screen)
                    # next turn
                    game.next_turn()

                    current_player = self.game.next_player
                    print(current_player)
                    calculating_param = 0
                

            for event in pygame.event.get():
                if current_player == 'black':
                    pass
                
                
                elif current_player == 'white':
                    # event checking
                

                    # checking for clicks
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # if piece selected
                        if mouse.picking:
                            mouse.update_mouse(event.pos)

                            released_rank = mouse.mouseY // SQSIZE
                            released_file = mouse.mouseX // SQSIZE

                            # create possible move
                            initial = Square(mouse.initial_rank, mouse.initial_file)
                            final = Square(released_rank, released_file)
                            move = Move(initial, final)
                            print(move) #CHECKPOINT
                            

                            # valid move ?
                            if board.valid_move(str(move), current_board):
                                # check en passant capture
                                if current_board.is_en_passant(chess.Move.from_uci(str(move))):
                                    print("EN PASSANT!") #TODO capturar el peon capturado al paso (eliminar piece y sprite)

                                # push move to board
                                current_board.push_uci(str(move))

                                # normal capture
                                captured = board.squares[released_rank][released_file].has_piece()
                                board.move(mouse.piece, move)                            

                                # sounds
                                game.play_sound(captured)
                                # show methods
                                game.show_background(screen)
                                game.show_last_move(screen)
                                game.show_pieces(screen)
                                # next turn
                                game.next_turn()
                                current_player = self.game.next_player
                                print(current_player)

                            
                            else:
                                pass
                        
                            mouse.unpick_piece()

                        # if piece not selected
                        elif mouse.picking == False:
                            mouse.update_mouse(event.pos)

                            clicked_rank = mouse.mouseY // SQSIZE
                            clicked_file = mouse.mouseX // SQSIZE
                            print((clicked_rank, clicked_file)) #CHECKPOINT

                            # checking if square has piece
                            if board.squares[clicked_rank][clicked_file].has_piece():
                                piece = board.squares[clicked_rank][clicked_file].piece
                                if piece.colour == game.next_player:    
                                    mouse.save_initial(event.pos)
                                    mouse.pick_piece(piece)
                                    print(piece) #CHECKPOINT

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