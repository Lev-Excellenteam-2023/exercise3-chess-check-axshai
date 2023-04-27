import pytest
import chess_engine
from Piece import Knight, Rook, Pawn
from enums import Player


@pytest.fixture
def tested_knight():
    return Knight('n', 3, 4, Player.PLAYER_1)


@pytest.fixture
def initial_game_state():
    game_state = chess_engine.game_state()
    white_pawn_1 = Pawn('p', 2, 2, Player.PLAYER_2)
    white_pawn_2 = Pawn('p', 1, 3, Player.PLAYER_2)
    white_pawn_3 = Pawn('p', 1, 5, Player.PLAYER_2)
    white_pawn_4 = Pawn('p', 2, 6, Player.PLAYER_2)
    white_pawn_5 = Pawn('p', 4, 2, Player.PLAYER_2)
    white_pawn_6 = Pawn('p', 5, 3, Player.PLAYER_2)
    white_pawn_7 = Pawn('p', 5, 5, Player.PLAYER_2)
    white_pawn_8 = Pawn('p', 4, 6, Player.PLAYER_2)
    board = [
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, white_pawn_2, Player.EMPTY, white_pawn_3, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, white_pawn_1, Player.EMPTY, Player.EMPTY, Player.EMPTY, white_pawn_4,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, white_pawn_5, Player.EMPTY, Player.EMPTY, Player.EMPTY, white_pawn_8,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, white_pawn_6, Player.EMPTY, white_pawn_7, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY]
    ]
    game_state.board = board
    return game_state


def test_get_valid_piece_takes(tested_knight, initial_game_state):
    # test_case 1 - simple knight situation: knight in the middle and can eat 8 pieces
    # pres test
    expected_res = ((1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3))
    # tested func
    valid_piece_takes = tested_knight.get_valid_piece_takes(initial_game_state)
    # post test checks
    assert set(expected_res) == set(valid_piece_takes), "simple knight situation test case failed!"

    # test_case 2 -  same player situation: knight in the middle but 2 pieces are of the same player
    # pres test
    initial_game_state.board[5][5] = initial_game_state.board[5][3] = Rook('r', 0, 0, Player.PLAYER_1)
    expected_res = ((1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6))
    # tested func
    valid_piece_takes = tested_knight.get_valid_piece_takes(initial_game_state)
    # post test checks
    assert set(expected_res) == set(valid_piece_takes), f"same player situation test case failed!"

    # test_case 3 - empty player situation: knight in the middle but 2 cells are empty
    # pres test
    initial_game_state.board[5][5] = initial_game_state.board[5][3] = Player.EMPTY
    expected_res = ((1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6))
    # tested func
    valid_piece_takes = tested_knight.get_valid_piece_takes(initial_game_state)
    # post test checks
    assert set(expected_res) == set(valid_piece_takes), f"empty player situation test case failed!"


def test_get_valid_peaceful_moves(tested_knight, initial_game_state):
    # test_case 1 - empty peaceful situation: knight in the middle and can eat 8 pieces
    # pres test
    expected_res = ()
    # tested func
    valid_piece_takes = tested_knight.get_valid_peaceful_moves(initial_game_state)
    # post test checks
    assert set(expected_res) == set(valid_piece_takes), "empty peaceful situation test case failed!"

    # test_case 2 - full peaceful situation: knight in the middle and all 8 cells are empty
    # pres test
    for r in range(8):
        for c in range(8):
            initial_game_state.board[r][c] = Player.EMPTY
    expected_res = ((1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3))
    # tested func
    valid_piece_takes = tested_knight.get_valid_peaceful_moves(initial_game_state)
    # post test checks
    assert set(expected_res) == set(valid_piece_takes), f"full peaceful situation test case failed!"

    # test_case 3 - corner situation: board is empty but knight is in the corner
    # pres test
    knight = Knight('n', 0, 0, Player.PLAYER_1)
    expected_res = ((1, 2), (2, 1))
    # tested func
    valid_piece_takes = knight.get_valid_peaceful_moves(initial_game_state)
    # post test checks
    assert set(expected_res) == set(valid_piece_takes), f"corner situation situation test case failed!"


def test_get_valid_piece_moves(tested_knight, initial_game_state):
    # test_case_1 - knight in the middle, 2 cells are empty
    # pres test
    initial_game_state.board[5][5] = initial_game_state.board[5][3] = Player.EMPTY
    expected_res = ((1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3))
    # tested func
    valid_piece_moves = tested_knight.get_valid_piece_moves(initial_game_state)
    # post test checks
    assert set(expected_res) == set(valid_piece_moves), "test_case_1 failed!"
