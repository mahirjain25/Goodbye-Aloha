#!/usr/bin/python3

import random

def resolve_func(contention_list, resolved_list, n) :

    if(n == 1) :
        resolved_list.append(contention_list);
        print("resolved_list = ", resolved_list)
        return;

    else :
        left = random.randint(1 , n);     #Starting from 1 because atleast let there be 1 leaf as the left branch.
        right = n - left;

        left_list = []
        right_list = []

        i = 0

        while i < left :                #Got to know why while loop os useful.
            temp = random.randint(0, n-1)
            if(contention_list[temp] != -1) :
                left_list.append(contention_list[temp])
                i = i + 1
                contention_list[temp] = -1


        for i in range(len(contention_list)) :
            if(contention_list[i] != -1) :
                right_list.append(contention_list[i])

        print("left_list = ", left_list);
        print("right_list = " , right_list);

        resolve_func(left_list, resolved_list, len(left_list));
        resolve_func(right_list, resolved_list, len(right_list));








if __name__ == "__main__" :

    no_of_dev = int(input("Enter the number of devices competing for 1 slot: "))
    print("\nThe Device IDs are 0 to ",no_of_dev-1)
    contention_list = []
    for i in range(0 , no_of_dev) :
        contention_list.append(i)

    resolved_list = []

    resolve_func(contention_list, resolved_list, no_of_dev);
