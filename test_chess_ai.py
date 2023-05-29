import pytest
import chess_engine
from Piece import Rook, Pawn, Bishop, Knight, King, Queen
from ai_engine import chess_ai
from enums import Player


@pytest.fixture
def initial_game_state():
    game_state = chess_engine.game_state()
    # Initialize White pieces
    white_rook_1 = Rook('r', 0, 0, Player.PLAYER_1)
    white_rook_2 = Rook('r', 0, 7, Player.PLAYER_1)
    white_knight_1 = Knight('n', 0, 1, Player.PLAYER_1)
    white_bishop_1 = Bishop('b', 0, 2, Player.PLAYER_1)
    white_queen = Queen('q', 0, 4, Player.PLAYER_1)
    white_king = King('k', 0, 3, Player.PLAYER_1)
    white_pawn_1 = Pawn('p', 1, 0, Player.PLAYER_1)
    white_pawn_2 = Pawn('p', 1, 1, Player.PLAYER_1)
    white_pawn_3 = Pawn('p', 1, 2, Player.PLAYER_1)

    # Initialize Black Pieces
    black_rook_1 = Rook('r', 7, 0, Player.PLAYER_2)
    black_rook_2 = Rook('r', 7, 7, Player.PLAYER_2)
    black_knight_1 = Knight('n', 7, 1, Player.PLAYER_2)
    black_knight_2 = Knight('n', 7, 6, Player.PLAYER_2)
    black_bishop_1 = Bishop('b', 7, 2, Player.PLAYER_2)
    black_bishop_2 = Bishop('b', 7, 5, Player.PLAYER_2)
    black_queen = Queen('q', 7, 4, Player.PLAYER_2)
    black_king = King('k', 7, 3, Player.PLAYER_2)
    black_pawn_1 = Pawn('p', 6, 0, Player.PLAYER_2)
    black_pawn_2 = Pawn('p', 6, 1, Player.PLAYER_2)
    black_pawn_3 = Pawn('p', 6, 2, Player.PLAYER_2)

    game_state.board = [
        [white_rook_1, white_knight_1, white_bishop_1, white_king, white_queen, Player.EMPTY, Player.EMPTY,
         white_rook_2],
        [white_pawn_1, white_pawn_2, white_pawn_3, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [black_pawn_1, black_pawn_2, black_pawn_3, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [black_rook_1, black_knight_1, black_bishop_1, black_king, black_queen, black_bishop_2, black_knight_2,
         black_rook_2]
    ]
    return game_state


def test_evaluate_board(initial_game_state):
    piece_val_dict = {
        "Rook": -50,
        "Knight": -30,
        "Bishop": -30,
        "Queen": -100,
        "King": -1000,
        "Pawn": -10,
    }
    white_expected_evaluation = (piece_val_dict["Rook"] * 2 + piece_val_dict["Knight"] + piece_val_dict["Bishop"] +
                                 piece_val_dict["Queen"] + piece_val_dict["King"] + piece_val_dict["Pawn"] * 3)
    black_expected_evaluation = (piece_val_dict["Rook"] * 2 + piece_val_dict["Knight"] * 2 +
                                 piece_val_dict["Bishop"] * 2 + piece_val_dict["Queen"] +
                                 piece_val_dict["King"] + piece_val_dict["Pawn"] * 3) * -1
    evaluate_board = chess_ai().evaluate_board(initial_game_state, Player.PLAYER_1)
    assert evaluate_board == white_expected_evaluation + black_expected_evaluation, \
        "Board evaluation is not working properly!"
