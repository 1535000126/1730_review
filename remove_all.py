
# Implement the function remove_all below.
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
    

    

def remove_all(a_list, element):
    new_list=[]
    for i in range(len(a_list)):
        if [element]==[a_list[i]]:
            new_list=new_list
        else:
            a=[a_list[i]]
            new_list.extend(a)
    a_list=new_list
    return a_list


def list_after_remove(list_in, element):
    """
    Wrapper function for testing remove_all; creates a copy of the
    input list, calls remove_all on the copy, and returns the copy
    after the call.
    """
    test_list = remove_all(list_in, element)
    return test_list

def test_remove_all():
    """
    This function runs a number of tests of the remove_all function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    """

    assert list_after_remove([1,2,3,4,5], 1) == [2,3,4,5], "should remove 1"
    assert list_after_remove([1,2,3,4,5], 3) == [1,2,4,5], "should remove 3"
    assert list_after_remove([1,2,3,4,5], 5) == [1,2,3,4], "should remove 5"
    assert list_after_remove([1,2,3,4,5], 7) == [1,2,3,4,5], "7 not in list, so should be unmodified"
    assert list_after_remove([[1,2],[1,2,3],[2,3]], [1,2,3]) == [[1,2], [2,3]], "should remove [1,2,3]"

    assert list_after_remove([1,2,3,2,3], 1) == [2,3,2,3], "should remove 1"
    assert list_after_remove([1,2,3,2,3], 2) == [1,3,3], "should remove both 2s"
    assert list_after_remove([2,2,2], 1) == [2,2,2], "1 not in list, so should be unmodified"
    assert list_after_remove([2,2,2], 2) == [], "should remove all three 2s"

    print("all tests passed")
