
# Implement the function moving_average below.
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

import numpy as np

def moving_average(seq, wsize):
    storage=[]
    for i in range(len(seq)-wsize+1):
        a=0
        b=0
        while a!=wsize:
            b=b+(seq[i+a]/wsize) 
            a=a+1
        storage.extend ([b])
    return storage


def seq_matches(seq1, seq2):
    """
    Return True if two sequences of numbers match with a tolerance of 0.001
    """
    if len(seq1) != len(seq2):
        return False
    for i in range(len(seq1)):
        if abs(seq1[i] - seq2[i]) > 1e-3:
            return False
    return True

def test_moving_average():
    """
    This function runs a number of tests of the moving_average function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    """
    
    assert seq_matches(moving_average((-1, 0, 0, -2, 1), 2), (-0.5, 0.0, -1.0, -0.5))
    assert seq_matches(moving_average([-1, 0, 0, -2, 1], 3), (-0.334, -0.667, -0.334))
    assert seq_matches(moving_average(np.array([-1, 0, 0, -2, 1]), 4), (-0.75, -0.25))
    assert seq_matches(moving_average((0, 1, 2, 0, 2), 2), (0.5, 1.5, 1.0, 1.0))
    assert seq_matches(moving_average((0, 1, 2, 0, 2), 3), (1.0, 1.0, 1.333))
    assert seq_matches(moving_average((0, 1, 2, 0, 2), 4), (0.75, 1.25))

    assert seq_matches(moving_average((-0.4, -0.4, 1.2, -1.6, 1.2), 2), (-0.4, 0.4, -0.2, -0.2))
    assert seq_matches(moving_average((-0.4, -0.4, 1.2, -1.6, 1.2), 3), (0.133, -0.267, 0.266))
    assert seq_matches(moving_average((-0.4, -0.4, 1.2, -1.6, 1.2), 4), (-0.3, 0.1))
    assert seq_matches(moving_average((0.8, 2.0, 0.2, 1.0, 0.4), 2), (1.4, 1.1, 0.6, 0.7))
    assert seq_matches(moving_average((0.8, 2.0, 0.2, 1.0, 0.4), 3), (1.0, 1.066, 0.533))
    assert seq_matches(moving_average((0.8, 2.0, 0.2, 1.0, 0.4), 4), (1.0, 0.9))

    assert seq_matches(moving_average((-1.5, -4.0, -3.0, 3.5, 4.5, 0.0, -3.5, -0.5, 4.0, 0.5), 2), (-2.75, -3.5, 0.25, 4.0, 2.25, -1.75, -2.0, 1.75, 2.25))
    assert seq_matches(moving_average((-1.5, -4.0, -3.0, 3.5, 4.5, 0.0, -3.5, -0.5, 4.0, 0.5), 5), (-0.1, 0.2, 0.3, 0.8, 0.9, 0.1))
    assert seq_matches(moving_average((-1.5, -4.0, -3.0, 3.5, 4.5, 0.0, -3.5, -0.5, 4.0, 0.5), 8), (-0.563, 0.125, 0.687))
    assert seq_matches(moving_average((2.5, -1.0, 1.0, 3.5, -5.0, -0.5, 4.5, -5.0, 5.0, -3.5), 2), (0.75, 0.0, 2.25, -0.75, -2.75, 2.0, -0.25, 0.0, 0.75))
    assert seq_matches(moving_average((2.5, -1.0, 1.0, 3.5, -5.0, -0.5, 4.5, -5.0, 5.0, -3.5), 5), (0.2, -0.4, 0.7, -0.5, -0.2, 0.1))
    assert seq_matches(moving_average((2.5, -1.0, 1.0, 3.5, -5.0, -0.5, 4.5, -5.0, 5.0, -3.5), 8), (0.0, 0.312, 0.0))
    assert seq_matches(moving_average((2.5, -2.0, -2.5, 2.5, -0.5, -2.5, 0.5, -5.0, 4.5, -4.5, 3.0, 3.5, -4.0, 1.0, 5.0, 1.0, -1.0, 2.0, 4.0, -2.0), 2), (0.25, -2.25, 0.0, 1.0, -1.5, -1.0, -2.25, -0.25, 0.0, -0.75, 3.25, -0.25, -1.5, 3.0, 3.0, 0.0, 0.5, 3.0, 1.0))
    assert seq_matches(moving_average((2.5, -2.0, -2.5, 2.5, -0.5, -2.5, 0.5, -5.0, 4.5, -4.5, 3.0, 3.5, -4.0, 1.0, 5.0, 1.0, -1.0, 2.0, 4.0, -2.0), 5), (0.0, -1.0, -0.5, -1.0, -0.6, -1.4, -0.3, 0.3, 0.5, -0.2, 1.7, 1.3, 0.4, 1.6, 2.2, 0.8))
    assert seq_matches(moving_average((2.5, -2.0, -2.5, 2.5, -0.5, -2.5, 0.5, -5.0, 4.5, -4.5, 3.0, 3.5, -4.0, 1.0, 5.0, 1.0, -1.0, 2.0, 4.0, -2.0), 8), (-0.875, -0.625, -0.938, -0.25, -0.125, -0.563, -0.125, 0.437, 1.187, 0.5, 1.312, 1.437, 0.75))
    assert seq_matches(moving_average((2.5, -2.0, -2.5, 2.5, -0.5, -2.5, 0.5, -5.0, 4.5, -4.5, 3.0, 3.5, -4.0, 1.0, 5.0, 1.0, -1.0, 2.0, 4.0, -2.0), 13), (-0.347, -0.462, 0.076, 0.346, 0.076, 0.269, 0.769, 0.576))
    assert seq_matches(moving_average((-2.5, 3.5, 0.0, 3.5, 1.0, -2.5, -4.0, 1.5, -3.5, -3.0, 1.5, 0.0, 1.5, -3.5, -4.0, 3.5, 4.5, 2.5, 0.5, 0.5), 2), (0.5, 1.75, 1.75, 2.25, -0.75, -3.25, -1.25, -1.0, -3.25, -0.75, 0.75, 0.75, -1.0, -3.75, -0.25, 4.0, 3.5, 1.5, 0.5))
    assert seq_matches(moving_average((-2.5, 3.5, 0.0, 3.5, 1.0, -2.5, -4.0, 1.5, -3.5, -3.0, 1.5, 0.0, 1.5, -3.5, -4.0, 3.5, 4.5, 2.5, 0.5, 0.5), 5), (1.1, 1.1, -0.4, -0.1, -1.5, -2.3, -1.5, -0.7, -0.7, -0.7, -0.9, -0.5, 0.4, 0.6, 1.4, 2.3))
    assert seq_matches(moving_average((-2.5, 3.5, 0.0, 3.5, 1.0, -2.5, -4.0, 1.5, -3.5, -3.0, 1.5, 0.0, 1.5, -3.5, -4.0, 3.5, 4.5, 2.5, 0.5, 0.5), 8), (0.062, -0.063, -0.875, -0.688, -1.125, -1.063, -1.188, -1.188, -0.938, 0.062, 0.75, 0.625, 0.687))
    assert seq_matches(moving_average((-2.5, 3.5, 0.0, 3.5, 1.0, -2.5, -4.0, 1.5, -3.5, -3.0, 1.5, 0.0, 1.5, -3.5, -4.0, 3.5, 4.5, 2.5, 0.5, 0.5), 13), (-0.231, -0.308, -0.885, -0.616, -0.539, -0.424, -0.193, 0.153))

    print("all tests passed")
