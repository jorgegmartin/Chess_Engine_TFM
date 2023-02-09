import pygame
import sys
import chess
import chess.engine

from constants import *
from board import *
from move import Move
from game import Game
from engine import Engine


class Main:

    def __init__(self):
        pygame.init()
        self.current_board = chess.Board()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()
        self.engine = Engine()

    def mainloop(self):

        game = self.game
        screen = self.screen
        board = self.game.board
        mouse = self.game.mouse
        current_board = self.current_board
        calculating_param = 0
        engine = self.engine
        promotion = 0

        while True:
            # show methods
            game.show_background(screen)
            game.show_pieces(screen)
            game.show_last_move(screen)
            
            current_player = self.game.next_player

            while current_player == 'black':
                game.show_background(screen)
                game.show_pieces(screen)
                game.show_last_move(screen)
                if calculating_param == 0:
                    calculating_param = 1
                    move_ai = engine.get_ai_move(current_board, 1) 

                    # create possible move
                    initial = Square(7-chess.square_rank(move_ai.from_square), chess.square_file(move_ai.from_square))
                    final = Square(7-chess.square_rank(move_ai.to_square), chess.square_file(move_ai.to_square))
                    selected_move = Move(initial, final)
                    print(selected_move) # CHECKPOINT

                    # normal capture
                    black_piece = board.squares[initial.rank][initial.file].piece
                    string_move_ai = str(move_ai)

                    if (string_move_ai[3]=='1') and (board.squares[initial.rank][initial.file].piece.name == 'pawn'):
                        promotion = 1
                    # special moves:
                    if current_board.is_en_passant(chess.Move.from_uci(string_move_ai)):
                        # update gui
                        board.move(black_piece, selected_move, enpassant=True)

                    # check castle
                    elif current_board.is_castling(chess.Move.from_uci(string_move_ai)):
                        if current_board.is_kingside_castling(chess.Move.from_uci(string_move_ai)):
                            # update gui
                            board.move(black_piece, selected_move, kingcastling=True, piece_colour='black')
                        
                        elif current_board.is_queenside_castling(chess.Move.from_uci(string_move_ai)):
                            # update gui
                            board.move(black_piece, selected_move, queencastling=True, piece_colour='black')
                        
                        # normal capture

                                
                    # check promotion
                    elif promotion==1:
                        board.move(black_piece, selected_move, promotion=True, piece_colour='black')
                        promotion=0 
                        # normal capture

                    
                    # normal move
                    else:
                        board.move(black_piece, selected_move)
                        
                    
                    captured = board.squares[final.rank][final.file].has_piece()

                    # engine.square_to_index(move_ai))
                    current_board.push_uci(string_move_ai)


                    # sounds
                    game.play_sound(captured)
                    # show methods
                    game.show_background(screen)
                    game.show_last_move(screen)
                    game.show_pieces(screen)
                    # next turn
                    game.next_turn()

                    current_player = self.game.next_player
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
                            string_move = str(move)

                            if (string_move[3]=='8') and (board.squares[initial.rank][initial.file].piece.name == 'pawn'):
                                promotion = 1
                                string_move = string_move+'q'

                            # check if valid move
                            if board.valid_move(string_move, current_board):
                                # check en passant capture
                                if current_board.is_en_passant(chess.Move.from_uci(string_move)):
                                    captured_square = board.squares[initial.rank][final.file]
                                    # normal capture
                                    captured = captured_square.has_piece()
                                    # update gui
                                    board.move(mouse.piece, move, enpassant=True)

                                # check castle
                                elif current_board.is_castling(chess.Move.from_uci(string_move)):
                                    if current_board.is_kingside_castling(chess.Move.from_uci(string_move)):
                                        # update gui
                                        board.move(mouse.piece, move, kingcastling=True)
                                        
                                    elif current_board.is_queenside_castling(chess.Move.from_uci(string_move)):
                                        # update gui
                                        board.move(mouse.piece, move, queencastling=True)

                                    # normal capture
                                    captured = board.squares[released_rank][released_file].has_piece()
                                
                                # check promotion
                                elif promotion==1:
                                    board.move(mouse.piece, move, promotion=True)
                                    promotion=0 
                                    # normal capture
                                    captured = board.squares[released_rank][released_file].has_piece()
                                
                                # normal move
                                else:
                                    board.move(mouse.piece, move) 
                                    captured = board.squares[released_rank][released_file].has_piece()                           
                                
                                # push move to board
                                current_board.push_uci(string_move)    

                                # sounds
                                game.play_sound(captured)
                                # show methods
                                game.show_background(screen)
                                game.show_last_move(screen)
                                game.show_pieces(screen)
                                # next turn
                                game.next_turn()
                                current_player = self.game.next_player

                            
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
                    
                    
                    # quitting
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


            pygame.display.update()




main = Main()
main.mainloop()