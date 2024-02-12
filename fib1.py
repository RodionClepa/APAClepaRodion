import time

def recursive_fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return recursive_fibonacci(x - 1) + recursive_fibonacci(x - 2)


def for_fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1

    a = 1
    b = 1
    for i in range(2, x):
        temp = a + b
        a = b
        b = temp
    
    return b

def dynamic_fibonacci(x):
    fib = [0, 1]

    for i in range(2, x + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[x]

def power_matrix(fib, x):
    mat = fib.copy()
    for i in range(1,x):
        temp = [[mat[0][0]*fib[0][0]+mat[0][1]*fib[1][0], mat[0][0]*fib[0][1]+mat[0][1]*fib[1][1]], 
                [mat[1][0]*fib[0][0]+mat[1][1]*fib[0][0], mat[1][0]*fib[0][1]+mat[0][1]*fib[1][1]]]
        mat = temp.copy()
    return mat[0][0]

def matrix_fibonacci(x):
    fib = [[1,1], [1, 0]]
    return power_matrix(fib, x-1)

from decimal import Decimal

def binet_fibonacci(x):
    phi1 = (1 + Decimal(5) ** Decimal(0.5)) / Decimal(2)
    phi2 = (1 - Decimal(5) ** Decimal(0.5)) / Decimal(2)
    fib = (phi1 ** x - phi2 ** x) / Decimal(5 ** 0.5)
    return fib

# Set recursion limit to a higher value
import sys
sys.setrecursionlimit(3000)
def memorization_fibonacci(x, memo={}):
    if x in memo:
        return memo[x]
    if x <= 1:
        return x
    
    memo[x] = memorization_fibonacci(x - 1, memo) + memorization_fibonacci(x - 2, memo)
    return memo[x]


# , 15, 17, 20, 22, 25, 27,30, 32, 35, 40,45
test_inputs = [5, 7, 10, 12]
array_result = []
#"*************************recursive_fibonacci*************************")
formatted_result = ""
for x in test_inputs:
    start_time = time.time()
    result = recursive_fibonacci(x)
    end_time = time.time()
    execution_time = end_time - start_time
    formatted_result += f"{execution_time:.3f}".ljust(10)

array_result.append(formatted_result)

formatted_result = ""
for x in test_inputs:
    formatted_result += f"{x}".ljust(10)

print(formatted_result)
print(array_result[0])

print("\n")

test_inputs = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589]
#"*************************for_fibonacci*************************")
formatted_result = ""
for x in test_inputs:
    start_time = time.time()
    result = for_fibonacci(x)
    end_time = time.time()
    execution_time = end_time - start_time
    formatted_result += f"{execution_time:.3f}".ljust(10)
    
print("+")

array_result.append(formatted_result)

up_table = ""
for x in test_inputs:
    up_table += f"{x}".ljust(10)

#"*************************dynamic_fibonacci*************************")
formatted_result = ""
for x in test_inputs:
    start_time = time.time()
    result = dynamic_fibonacci(x)
    end_time = time.time()
    execution_time = end_time - start_time
    formatted_result += f"{execution_time:.3f}".ljust(10)

array_result.append(formatted_result)
print("+")
#"*************************matrix_fibonacci*************************")
formatted_result = ""
for x in test_inputs:
    start_time = time.time()
    result = matrix_fibonacci(x)
    end_time = time.time()
    execution_time = end_time - start_time
    formatted_result += f"{execution_time:.3f}".ljust(10)

array_result.append(formatted_result)
print("+")
#"*************************binet_fibonacci*************************")
formatted_result = ""
for x in test_inputs:
    start_time = time.time()
    result = binet_fibonacci(x)
    end_time = time.time()
    execution_time = end_time - start_time
    formatted_result += f"{execution_time:.3f}".ljust(10)

array_result.append(formatted_result)

print("+")
#"*************************memorization_fibonacci*************************")
formatted_result = ""
for x in test_inputs:
    start_time = time.time()
    result = memorization_fibonacci(x)
    end_time = time.time()
    execution_time = end_time - start_time
    formatted_result += f"{execution_time:.3f}".ljust(10)
print("+")
array_result.append(formatted_result)
for i in range(1, len(array_result)):
    print(up_table)
    print(array_result[i])
    print("----------------------------------------------------------")