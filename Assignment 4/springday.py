import pygame, pygame.mixer
import ui, player, board
from evaluator import Evaluator
import random, time

BLACK = 1
WHITE = 2

class Othello:
    pygame.mixer.init()
    pygame.mixer.music.load('res/spring_day.mp3')
    pygame.mixer.music.play(-1)

    def __init__(self):
        self.gui = ui.Gui()
        self.board = board.Board()
        self.get_options()

    def get_options(self):
        player1, player2, level = self.gui.show_options()
        if player1 == "human":
            self.now_playing = player.Human(self.gui, BLACK)
        elif player1 == "computer":
            self.now_playing = player.Computer(BLACK, level + 3)
        elif player1 == "random":
            self.now_playing = player.Random(BLACK, level + 3)
        if player2 == "human":
            self.other_player = player.Human(self.gui, WHITE)
        elif player2 == "computer":
            self.other_player = player.Computer(WHITE, level + 3)
        elif player2 == "random":
            self.other_player = player.Random(WHITE, level + 3)

        self.gui.show_game()
        self.gui.update(self.board.board, 2, 2, self.now_playing.color)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if self.board.game_ended():
                whites, blacks, empty = self.board.count_stones()
                if whites > blacks:
                    winner = WHITE
                elif blacks > whites:
                    winner = BLACK
                else:
                    winner = None
                break
            self.now_playing.get_current_board(self.board)
            if self.board.get_valid_moves(self.now_playing.color) != []:
                score, self.board = self.now_playing.get_move()
                whites, blacks, empty = self.board.count_stones()
                self.gui.update(self.board.board, blacks, whites,
                                self.now_playing.color)
            self.now_playing, self.other_player = self.other_player, self.now_playing
        self.gui.show_winner(winner)
        pygame.time.wait(1000)
        self.restart()

    def restart(self):
        self.board = board.Board()
        self.get_options()
        self.run()

#running the game yay

otroad = Othello()
otroad.run()


