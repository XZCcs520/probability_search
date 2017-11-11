import bayesian
def test_random_board():
    board, belief, target_row, target_col= bayesian.random_board(10)
    print board
    print belief
    print target_row
    print target_col


def test_is_found():
    print bayesian.is_found(0.1)


def _main():
    P = [0.1, 0.3, 0.7, 0.9]
    print P[0]
    test_is_found()
    test_random_board()


_main()