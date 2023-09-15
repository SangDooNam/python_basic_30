"""Task: You are given a list and two indizes. 
Implement a method swap that takes the list and the two indizes as arguments, 
swaps the values at the given indizes and returns the list."""

def swap(list,a,b):
    
    list[a], list[b] = list[b], list[a]
    
    return list

swap_list = [23, 65, 19, 90]

print(swap(swap_list, 1, 3))