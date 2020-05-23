# Digant Kumar

# Returns the list of elements in the numeric list which exceed all the previous elements.
def numlist(lst):
    new_list = []
    if len(lst) == 1 or len(lst)==0:       # If the list contains only 1 element or no element, we return it
        new_list = lst
    for i in range(len(lst)-1):
        if i == 0:
            new_list.append(lst[i])                     # We always store the 1st element in the list.
            if lst[i+1] > lst[i]:
                new_list.append(lst[i+1])
                continue
        if lst[i+1] > lst[i]:
            new_list.append(lst[i+1])
            continue
    return new_list

# Returns True if the integer n is a perfect cube, False otherwise.
def is_cube(n):
    is_perfect_cube = False
    if n>=0:
        num = n
    else:
        num = -n
    for i in range(0,num+1):
        cube = i*i*i
        if cube == num:
            is_perfect_cube = True
            break
    if is_perfect_cube:
        return "True"
    return "False"

# Returns the smallest perfect cube which exceeds the non-negative number n.
def first_cube_above(n):
    num = n + 1
    new_cube = is_cube(num)
    if new_cube == "True":
        return num
    else:
        num = num + 1
        new_cube = is_cube(num)
        while new_cube != "True":
            num = num + 1
            new_cube = is_cube(num)
    return num

