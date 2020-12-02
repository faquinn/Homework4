#Flammond Quinn
#PSID: 1659392



num_calls = 0


def partition(user_ids, x, y):
  
    lower = ( x-1 ) 
    middle = (x+y)//2
    piv = user_ids[middle] 
    user_ids[middle],user_ids[y] = user_ids[y],user_ids[middle]
    for i in range(x , y):
        if user_ids[i] <= piv:
            lower = lower+1
            user_ids[lower],user_ids[i] = user_ids[i],user_ids[lower]
    user_ids[lower+1],user_ids[y] = user_ids[y],user_ids[lower+1]
    return ( lower+1 )
  

def quicksort(user_ids, x, i):
    global num_calls
    num_calls+=1
    if x < i:
        pivot_index = partition(user_ids, x, i)
        quicksort(user_ids, x, pivot_index-1)
        quicksort(user_ids, pivot_index+1, i)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
  
    quicksort(user_ids, 0, len(user_ids) - 1)
  

    print(num_calls)
  

    for user_id in user_ids:
        print(user_id)

