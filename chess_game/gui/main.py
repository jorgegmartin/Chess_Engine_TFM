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

        def select_difficulty():
            pygame.init()
            screen = pygame.display.set_mode((900, 600))
            background_img = pygame.image.load('chess_game/gui/resources/imgs/chess_background.jpeg')
            button3 = pygame.Rect(50, 60, 200, 50)
            button6 = pygame.Rect(50, 160, 200, 50)
            button10 = pygame.Rect(50, 260, 200, 50)
            button10re = pygame.Rect(50, 360, 200, 50)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        if button3.collidepoint(event.pos):
                            depth = 'easy'
                            print(depth)
                            return depth
                        if button6.collidepoint(event.pos):
                            depth = 'medium'
                            print(depth)
                            return depth
                        if button10.collidepoint(event.pos):
                            depth = 'hard'
                            print(depth)
                            return depth
                        if button10re.collidepoint(event.pos):
                            depth = 'extreme'
                            print(depth)
                            return depth
                screen.fill((0, 0, 0))
                screen.blit(background_img, (0, 0))
                pygame.display.set_caption('Chess')
                pygame.draw.rect(screen, (0, 200, 0), button3, border_radius=10)
                pygame.draw.rect(screen, (250, 250, 0), button6,  border_radius=10)
                pygame.draw.rect(screen, (255, 128, 50), button10,  border_radius=10)
                pygame.draw.rect(screen, (200, 0, 0), button10re,  border_radius=10)
                
                pygame.draw.rect(screen, (0, 150, 0), button3, width=5, border_radius=10)
                pygame.draw.rect(screen, (200, 200, 0), button6, width=5,  border_radius=10)
                pygame.draw.rect(screen, (205, 98, 20), button10, width=5,  border_radius=10)
                pygame.draw.rect(screen, (100, 0, 0), button10re, width=5,  border_radius=10)
                
                font = pygame.font.Font(None, 36)
                depth3_text = font.render("Easy", True, (0, 0, 0))
                depth6_text = font.render("Medium", True, (0, 0, 0))
                depth10_text = font.render("Hard", True, (0, 0, 0))
                depth10re_text = font.render("Extreme", True, (0, 0, 0))
                select_difficulty = font.render("SELECT DIFFICULTY", True, (255, 255, 255))
                watermark_font = pygame.font.Font(None, 14)
                watermark_text = watermark_font.render("Powered by KSCHOOL. 2023", True, (56, 56, 56))

                screen.blit(depth3_text, (100, 75))
                screen.blit(depth6_text, (100, 175))
                screen.blit(depth10_text, (100, 275))
                screen.blit(depth10re_text, (100, 375))
                screen.blit(select_difficulty, (50, 25))
                screen.blit(watermark_text, (750, 35))

                pygame.display.update()

        pygame.init()
        self.engine_difficulty = select_difficulty()
        self.current_board = chess.Board()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()
        self.engine = Engine(self.engine_difficulty)

    def mainloop(self):

        game = self.game
        screen = self.screen
        board = self.game.board
        mouse = self.game.mouse
        current_board = self.current_board
        calculating_param = 0
        engine = self.engine
        promotion = 0
        
        # selecting the difficulty of the game's engine
        game_depth = 1
        engine_difficulty = self.engine_difficulty

        while True:
            # show methods
            game.show_background(screen)
            game.show_last_move(screen)
            game.show_highlighted(screen)
            game.show_pieces(screen)
            
            current_player = self.game.next_player

            while current_player == 'black':
                game.show_background(screen)
                game.show_last_move(screen)
                game.show_pieces(screen)

                if calculating_param == 0:
                    calculating_param = 1
                    move_ai = engine.get_ai_move(current_board, game_depth, engine_difficulty) 

                    # create possible move
                    initial = Square(7-chess.square_rank(move_ai.from_square), chess.square_file(move_ai.from_square))
                    final = Square(7-chess.square_rank(move_ai.to_square), chess.square_file(move_ai.to_square))
                    selected_move = Move(initial, final)

                    # normal capture
                    black_piece = board.squares[initial.rank][initial.file].piece
                    string_move_ai = str(move_ai)

                    if (string_move_ai[3]=='1') and (board.squares[initial.rank][initial.file].piece.name == 'pawn'):
                        promotion = 1
                    # special moves:
                    if current_board.is_en_passant(chess.Move.from_uci(string_move_ai)):
                        # update gui
                        board.move(black_piece, selected_move, enpassant=True)
                        captured = True

                    # check castle
                    elif current_board.is_castling(chess.Move.from_uci(string_move_ai)):
                        if current_board.is_kingside_castling(chess.Move.from_uci(string_move_ai)):
                            # update gui
                            board.move(black_piece, selected_move, kingcastling=True, piece_colour='black')
                        
                        elif current_board.is_queenside_castling(chess.Move.from_uci(string_move_ai)):
                            # update gui
                            board.move(black_piece, selected_move, queencastling=True, piece_colour='black')
                        captured = False

                                
                    # check promotion
                    elif promotion==1:
                        captured = board.squares[final.rank][final.file].has_piece()
                        board.move(black_piece, selected_move, promotion=True, piece_colour='black')
                        promotion=0 
                        # normal capture

                    
                    # normal move
                    else:
                        captured = board.squares[final.rank][final.file].has_piece()
                        board.move(black_piece, selected_move)

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
                            string_move = str(move)

                            if (string_move[3]=='8') and (board.squares[initial.rank][initial.file].piece.name == 'pawn'):
                                promotion = 1
                                string_move = string_move+'q'

                            # check if valid move
                            if board.valid_move(string_move, current_board):
                                # check en passant capture
                                if current_board.is_en_passant(chess.Move.from_uci(string_move)):
                                    # normal capture
                                    captured = True
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

                                    captured = False
                                
                                # check promotion
                                elif promotion==1:
                                    # normal capture
                                    captured = board.squares[released_rank][released_file].has_piece()
                                    # move
                                    board.move(mouse.piece, move, promotion=True)
                                    promotion=0 

                                
                                # normal move
                                else:
                                    captured = board.squares[released_rank][released_file].has_piece() 
                                    board.move(mouse.piece, move)                           
                                
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

                            # checking if square has piece
                            if board.squares[clicked_rank][clicked_file].has_piece():
                                piece = board.squares[clicked_rank][clicked_file].piece
                                if piece.colour == game.next_player:    
                                    mouse.save_initial(event.pos)
                                    mouse.pick_piece(piece)

                            
                            game.show_background(screen)
                            game.show_last_move(screen)
                            game.show_highlighted(screen)
                            game.show_pieces(screen)
                    
                    # quitting
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


            pygame.display.update()




main = Main()
main.mainloop()