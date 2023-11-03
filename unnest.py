
# Implement the function unnest below.
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



def new_list(alist):
    new_list=[]
    for i in range(len(alist)):
        if isinstance(alist[i],int)==True:
            new_list=new_list+[alist[i]]
        else:
            new_list=new_list+alist[i]
    return new_list

def check (alist):
    for i in range(len(alist)):
        if isinstance(alist[i],int)==True:
            continue
        else:
            return False
    return True
   
def unnest(alist):
   new= new_list(alist)
   right=check(new)
   while right == False:
        new= new_list(new)
        right=check(new)
   return new


def test_unnest():
    """
    This function runs a number of tests of the unnest function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    """
    
    assert unnest([2, 1, 3, [0, 4]]) == [2, 1, 3, 0, 4]
    assert unnest([1, [3], [2, 4], 0]) == [1, 3, 2, 4, 0]
    assert unnest([[[3, 0], 1], 4, 2]) == [3, 0, 1, 4, 2]
    assert unnest([1, [2], [[3], [[4], 5]]]) == [1, 2, 3, 4, 5]
    assert unnest([0, [[2, [1], 4]], [[3]]]) == [0, 2, 1, 4, 3]
    assert unnest([[[0], 2], 3, 1, 4]) == [0, 2, 3, 1, 4]
    assert unnest([[9, 5, 0, 4], [8, 7, 1], 6, 3, 2]) == [9, 5, 0, 4, 8, 7, 1, 6, 3, 2]
    assert unnest([6, 9, [2, 8, 7, 4], [[0, [5]], 1, 3]]) == [6, 9, 2, 8, 7, 4, 0, 5, 1, 3]

    assert unnest([[0], [[[2, 4, 3]], [1]]]) == [0, 2, 4, 3, 1]
    assert unnest([[4, [[1]]], 0, 2, 3]) == [4, 1, 0, 2, 3]
    assert unnest([[[1, 3, 4, [[[[2]]]]]], 0]) == [1, 3, 4, 2, 0]
    assert unnest([[4], 1, [[3, [0], [[2]]]]]) == [4, 1, 3, 0, 2]
    assert unnest([[[0]], 4, [[[3]]], [1, 2]]) == [0, 4, 3, 1, 2]
    assert unnest([7, [[5], [2], 4], 6, [[[0, [8], 1]], 9], [[3]]]) == [7, 5, 2, 4, 6, 0, 8, 1, 9, 3]
    assert unnest([[2, 6, [[[5]]], [7], 4, 9, 1, 0, 8], [[3]]]) == [2, 6, 5, 7, 4, 9, 1, 0, 8, 3]
    assert unnest([8, 6, 2, 1, 5, 7, 3, 9, [[[[[[[4]]]]]]], [0]]) == [8, 6, 2, 1, 5, 7, 3, 9, 4, 0]
    assert unnest([[4, [[[1]], 5, 2, 8, [[[3]], 0, 6]], 7, 9]]) == [4, 1, 5, 2, 8, 3, 0, 6, 7, 9]
    assert unnest([[[[1, 9], [3]], [2, [7, 5, 8], 6, 0]], 4]) == [1, 9, 3, 2, 7, 5, 8, 6, 0, 4]

    assert unnest([1, [], [2], [[3], [], [[4], [], 5]]]) == [1, 2, 3, 4, 5]
    assert unnest([1, [[3], []], [], [[], 2, 4], 0]) == [1, 3, 2, 4, 0]
    assert unnest([0, [[], [2, [1], 4]], [[], [3]]]) == [0, 2, 1, 4, 3]
    assert unnest([[], [[], [[], 3, 0], 1], [], 4, 2]) == [3, 0, 1, 4, 2]
    assert unnest([[[0], [], 2], [], [], 3, 1, [], 4]) == [0, 2, 3, 1, 4]
    assert unnest([2, [[]], 1, [3], [[0, 4]]]) == [2, 1, 3, 0, 4]
    assert unnest([[[]]]) == []

    print("all tests passed")
