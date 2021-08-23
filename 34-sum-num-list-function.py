# 34. Write a function to sum all the numbers in a list. 

def sum_list(list):
    total = 0
    for i in list:
        total += i
    return total

l = (1, 2, 3, 4, 5, 6)

print(f"Sum of list: {sum_list(l)}")