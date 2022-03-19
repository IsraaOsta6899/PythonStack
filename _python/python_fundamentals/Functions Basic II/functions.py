def Countdown(num):
    myList=[]
    for i in range(num ,-1,-1):
        myList.append(i)
    print(myList)
Countdown(7)

def print_and_return(my_list):
    print(my_list[0])
    return my_list[1]
y=print_and_return([1,2])
print(y)

def first_plus_length(list):
    return(list[0]+list[len(list)-1])
y=first_plus_length([1,2,3,5])
print(y)

def values_greater_than_second(list):
    newlist=[]
    if len(list)<=1 :
        return False;
    for i in range(0,len(list)-1,1):
        if list[i]>list[i+1] :
            newlist.append(list[i])
    newlist.append(list[len(list)-1])
    print(len(newlist))
    return newlist
y=values_greater_than_second([3])
print(y)
y=values_greater_than_second([5,2,3,2,1,4])
print(y)


def length_and_value(x,y):
    newlist=[]
    for i in range(0,x):
        newlist.append(y)
    print(newlist)
    return newlist
length_and_value(5,1)

        
