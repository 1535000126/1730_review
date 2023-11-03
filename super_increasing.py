
# Implement the function super_increasing below.
# You can define other functions if it helps you decompose and solve
# the problem.
# Do not import any module that you do not use!

# Remember that if this were an exam problem, in order to be marked
# this file must meet certain requirements:
# - it must contain ONLY syntactically valid python code (any syntax
#   or indentation error that stops the file from running would result
#   in a mark of zero);
# - you MAY NOT use global variables; the function must use only the
#   input provided to it in its arguments.

def sum_seq(seq,i):
    seq_total=0
    while i>=0:
        seq_total=seq_total+seq[i]
        i=i-1
    return seq_total

def super_increasing(seq):
    for i in range(len(seq)-1):
        if sum_seq(seq,i)>=seq[1+i]:
            return False
        else:
            continue
    return True


def test_super_increasing():
    """
    This function runs a number of tests of the super_increasing function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    """

    assert not super_increasing((1, 3, 5, 7, 19)), "sum(1, 3, 5) = 9 >= 7"
    assert super_increasing([1, 3, 5, 11, 21]), "sum(1) = 1 < 3; sum(1,3) = 4 < 5; sum(1, 3, 5) = 9 < 11; sum(1, 3, 5, 11) = 20 < 21"
    assert super_increasing((0, 1, 2, 4)), "sum(0) = 0 < 1; sum(0, 1) = 1 < 2; sum(0, 1, 2) = 3 < 4"
    assert not super_increasing([0, 0, 1, 2]), "sum(0) = 0 >= 0"
    assert super_increasing((-1, 0, 0, 1)), "sum(-1) = -1 < 0; sum(-1, 0) = -1 < 0; sum(-1, 0, 0) = -1 < 1"
    assert not super_increasing((1, 2, 0, 4)), "sum(1, 2) = 3 >= 0"
    assert super_increasing((-1, 3, 4)), "sum(-1) < 3; sum(-1, 3) = 2 < 4"
    assert not super_increasing((-1, 3, 4, 5)), "sum(-1, 3, 4) = 6 >= 5"
    assert super_increasing((-2, -1, -2)), "sum(-2) < -1; sum(-2, -1) = -3 < -2"
    assert not super_increasing((-2, -1, -4)), "sum(-2, -1) = -3 >= -4"

    print("all tests passed")
