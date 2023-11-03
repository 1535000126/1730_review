def is_increasing(sequence):
    if len(sequence)==1:
        return True
    if len(sequence)==0:
        return True
    else:
        for a in range (1,len(sequence)):
           while sequence[a]>= sequence[a-1]:
               a=a+1
               if a==len(sequence):
                return True
           else:
               return False

##################################################################

def average(number_list):
    return sum(number_list)/len(number_list)

def most_average(numbers):
    closest_value = numbers[0]  
    closest_difference = abs(numbers[0] - average(numbers)) 
    
    for a in numbers:
        difference = abs(a - average(numbers))
        if difference < closest_difference:
            closest_value = a
            closest_difference = difference
            
    return closest_value

###################################################
            
def smallest_greater(list, a):
    b=None
    for element in list:
        if element > a:
            if b is None or b>element:
                b=element
    return b
    

def greatest_smaller(list, a):
    b=None
    for element in list:
        if element < a:
            if b is None or b<element:
                b=element
    return b

#####################################################

def count_duplicates(seq):
    seen = set()
    duplicates = 0
    
    for item in seq:
        if item in seen:
            duplicates += 1
        else:
            seen.add(item)
    
    return duplicates

##############################################
        
def count_in_bin(values, lower, upper):
    up_class=set()
    mid_class=set()
    low_class=set()
    for a in values:
        if a < lower:
            low_class.add(a)
        if lower<= a <= upper:
            mid_class.add(a)
        else:
            up_class.add(a)
    if len(low_class)<= len(mid_class) & len(low_class) <= len(up_class):
        return len(low_class)
    if len(mid_class)<= len(low_class) & len(mid_class) <= len(up_class):
        return len(mid_class)
    if len(up_class)<= len(mid_class) & len(up_class) <= len(low_class):
        return len(up_class)
############################


n=7
loop_times=0
if n>0:
    while n != 1:
        loop_times = loop_times+1
        if n % 2 ==1:
            n= 3*n+1
        if n % 2 ==0:
            n= int(n/2)
            
########################################################

def count_capitals(string):
    s=str()
    for m in range (0, len (string)):
        n=0
        while n <26:
            if string[m] == chr (ord('A') + n):
                s=s+string [m]
            n=n+1
                  
    return s

###################################################
def count(seq, prop):
    s=0
    for m in range (0,len(seq)):
        if seq[m] in prop is True:
            s=s+1
    return s
####################################################

def sum_odd_digits(number):
    dsum = 0
    n=100
    while n > 10:
        if number // n > 1:
            n=10*n
        if number//n==1:
            dsum=dsum+1
            number=number-n
        if number // n < 1:
            if (number //(n//10)) % 2 == 0:
                number=number%(n//10)
                n=n//10
            if (number //(n//10)) % 2 == 1:
                dsum= dsum + number //(n//10)
                number=number%(n//10)
                n=n//10
            
    if (number%10)%2==0:
        return dsum
    if (number%10)%2==1:
        return dsum+number%10



def sum_even_digits(number):
    dsum = 0
    m=number
    digit = 0
    while number > 0:
        digit = number % 10  
        dsum = dsum + digit    
        number //= 10        
    return dsum-sum_odd_digits(m)
###########################################

op= [1,2,5,3,6,4,7,8]
op.reverse()
op[7]= 805

###########################################
A=[[1,2],[3,4,5],[6,7,8,9]]
###########################################
a_list=[[1,2],[3,4]]
b_list=a_list[:]
a_list[0].reverse()
b_list.reverse()
##########################
boards = [([[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]),

          ([[1,1,1],[1,1,1],[1,1,1]],[[1,0,1],[0,0,0],[1,0,1]]),

          ([[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,0,0,0,0]],
           [[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,1,1,0],[0,0,0,0,0,0]])]


board = [[0,0,0],[0,0,0],[0,0,0]]
def left_right(board, row, column):
    number_of_1=0 
    if column ==0:
        if board[row][1]==1:
            number_of_1=number_of_1+1
    elif column ==len(board[0])-1:
        if board[row][-2]==1:
            number_of_1=number_of_1+1
    else:
        if board[row][column+1]==1:
            number_of_1=number_of_1+1
        if board[row][column-1]==1:
            number_of_1=number_of_1+1
    return number_of_1

def up_down(board, row, column):
    number_of_1=0 
    if row ==0:
        if board[1][column]==1:
            number_of_1=number_of_1+1
    elif row ==len(board)-1:
        if board[-2][column]==1:
            number_of_1=number_of_1+1
    else:
        if board[row+1][column]==1:
            number_of_1=number_of_1+1
        if board[row-1][column]==1:
            number_of_1=number_of_1+1
    return number_of_1

def count_live_neighbours(board, row, column):
    total_number_of_1=up_down(board, row, column)+left_right(board, row, column)
    if row==0:
        total_number_of_1=total_number_of_1+left_right(board, row+1, column)
    elif row ==len(board)-1:
        total_number_of_1=total_number_of_1+left_right(board, row-1, column)
    else:
        total_number_of_1=total_number_of_1+left_right(board, row-1, column)+left_right(board, row+1, column)
    return total_number_of_1

def generate_next_board(board):
    row=0
    column=0
    while row < len(board)+1:
        for column in range (len(board[0])):
            if count_live_neighbours(board, row, column) <=1:
                board[row][column]=0
            if count_live_neighbours(board, row, column) >=4:
                board[row][column]=0
            if 2<= count_live_neighbours(board, row, column)<=3:
                board[row][column]=board[row][column]
            if count_live_neighbours(board, row, column) ==3:
                board[row][column]=1
        row=row+1
#################################################
import numpy as np
arr=np.array([[1,2,3],[5,5,5]])
ar=np.arange(10,100,10)
####################################
import math

# 定义被积函数
def f(x):
    return 6 * math.log(x**3 + 5)

# 梯形法则
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    return h * result

# 中点法则
def midpoint_rule(a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + (i + 0.5) * h)
    return h * result

# 辛普森法则
def simpsons_rule(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)
    return (h / 3) * result

# 积分区间和子区间数
a = 4
b = 6
n = 10

# 计算近似积分
trap = trapezoidal_rule(a, b, n)
mid = midpoint_rule(a, b, n)
simp = simpsons_rule(a, b, n)

#####################################################
cidian={"ww":1,"jj":2}
didian=cidian
cidian["ff"]=5
cidian["re"]="jrt"
del cidian["ff"]
####################################


import numpy as np

A = np.array([[1, 0, 6,4], 
              [(-2),(-1),0,(-1)],
              [(-4),0,0,0],
              [0,(-2),(-4),(-4)]])
det_A = np.linalg.det(A)
################################

def count_kmer(sequence, k):
    """ counting occurence
    of all distinct kmers"""
    kmer = []
    storage=[]
    result = []
    for index in range(len(sequence)-k+1):
        distinct_kmers = [sequence[index:index+k]]
        kmer.extend(distinct_kmers)


    for i in range(len(kmer)):
        if kmer[i] in storage:
            continue
        else:
            storage.append(kmer[i])
            count=kmer.count(kmer[i])
            result.append((kmer[i],count))
    return result

############################################

a=np.arange(12).reshape(3,4)
print(a)



