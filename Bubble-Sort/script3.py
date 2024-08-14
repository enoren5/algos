# https://discuss.python.org/t/writing-a-bubble-sort-algorithm/60466
# With suggestions and assistance from user @dg-pb on the Python forums
# 

arr = [5,3,4,1,2]

print(f"Original list: {arr}")

def bubble(arr): 
    for iteration in range(0,len(arr)):
        for i in range(iteration):
            el1 = arr[i]
            el2 = arr[i+1]
            if el1 > el2:
                arr[i] = el2
                arr[i+1] = el1
            # else:
            #    continue
    return arr

sorted_list = bubble(arr)

print(f"Final sorted list: {sorted_list}")

