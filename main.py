from objects.GameManager import GameManager
from players.RandomPlayer import RandomPlayer

player1 = RandomPlayer("X")
player2 = RandomPlayer("0")
game_manager = GameManager(player1, player2)

game_manager.run_game()
