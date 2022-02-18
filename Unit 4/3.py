def prod_list(l):
    
    if len(l) == 1:
        return l[0]
    
    else:
        return l[0] * prod_list(l[1:])


b = 0
def max_list(l):
    global b

    if len(l) == 1:
        return l[0]

    else:
        max_list(l[1:])
        c = l[-1]

        if c < l[0] and b < l[0]:
            b = l[0]
        
        elif c > l[0] and c > b:
            b = c
        
        return b


smallest = 9
def min_list(l):
    global smallest

    if len(l) == 1:
        return l[0]
    
    else:
        min_list(l[1:])
        last_num = l[-1]

        if last_num > l[0] and smallest > l[0]:
            smallest = l[0]
        
        elif last_num < l[0] and last_num < smallest:
            smallest = last_num

        return smallest


counter = 0
def count_0(l):
    global counter    

    if len(l) == 1:
        if l[0] == 0:
            counter += 1
        return l[0]
    
    
    else:
        if l[0] == 0:
            counter += 1

        return count_0(l[1:]), counter
    
element_counter = 0
def count_list(l, n):
    global element_counter

    if len(l) == 1:
        if n == l[0]:
            element_counter += 1
        return l[0]
    
    else:
        if n == l[0]:
            element_counter+= 1
        
        return count_list(l[1:], n), element_counter

def print_list(l):
    if len(l) == 1:
        return l[0]
    
    else:
        print (l[0])
        return print_list(l[1:]), l[-1]


def print_reverse(l):
    if len(l) == 1:
        return l[0]
    
    else:
        print (l[-1])
        return print_reverse(l[:-1]), l[0]

reverse_nums, last_reverse = print_reverse([1,2,3,4])
print (last_reverse)


def main():
    print(prod_list([1,2,3,4]))
    print(max_list([9,4,5,1]))
    print(min_list([9,4,5,1]))
    
    a , b = (count_0([1,2,0,5,0]))
    nums, user_element = count_list([1,3,3,4,3], 3)
    print(user_element)
    
    first_num, last_nums = print_list([1,2,3,4])
    print(last_nums)
    
main()
