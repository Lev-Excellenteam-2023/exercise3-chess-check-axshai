import chess_engine


def test_all_game():
    game_state = chess_engine.game_state()
    game_state.move_piece((1, 2), (2, 2), False)
    game_state.move_piece((6, 3), (5, 3), False)
    game_state.move_piece((1, 1), (3, 1), False)
    game_state.move_piece((7, 4), (3, 0), False)
    game_result = game_state.checkmate_stalemate_checker()
    assert not game_result, f"Expected game result was 0 (white lost) but actual result is {game_result}"
