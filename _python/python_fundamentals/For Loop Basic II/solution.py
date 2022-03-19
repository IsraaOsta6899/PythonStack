def biggie_size(list):
    for i in range(0,len(list)):
        if list[i] > 0:
            list[i]='big'
    print(list)
biggie_size([-1,3,-2,5])

def count_positives(list):
    count=0
    for i in range(0,len(list)):
        if list[i] > 0:
            count=count+1
    list[len(list)-1]=count
    print(list)
count_positives([1,6,-4,-2,-7,-2])

def sum_total(list):
    totalSum=0
    for i in range(0,len(list)):
        totalSum=totalSum+list[i]
    print(totalSum)
    return totalSum
sum_total([6,3,-2])

def average(list):
    totalSum=0
    count = len(list)
    for i in range(0,len(list)):
        totalSum=totalSum+list[i]
    avg=totalSum/count
    print(avg)
    return avg
average([1,2,3,4])
def length(list):
    length = len(list)
    print(length)
    return length
length([])

def minimum(list):
    min =1000000000000
    if len(list)<=0:
        print("False")
        return False
    else:
        for i in range(0,len(list)):
            if list[i]< min:
                min = list[i]
        print(min)
        return min

minimum([1, 6, -4, -2, -7, 2])


def max(list):
    maxElement =-1000000000000
    if len(list)<=0:
        print("False")
        return False
    else:
        for i in range(0,len(list)):
            if list[i]> maxElement:
                maxElement = list[i]
        print(maxElement)
        return maxElement
max([1, 6, -4, -2, -7, 2])



def ultimate_analysis(list):
    dic={}
    dic['sumTotal']=sum_total(list)
    dic['average']=average(list)
    dic['minimum']=minimum(list)
    dic['maximum']=max(list)
    dic['length']=length(list)
    print(dic)
    return dic

ultimate_analysis([37,2,1,-9])

def reverse_list(list):
    x=0;
    y=len(list)-1
    if len(list)>1:
        while x<y:
            temp = list[x]
            list[x]=list[y]
            list[y]=temp
            x=x+1
            y=y-1
    print(list)
reverse_list([37,2,1,-9,4]) 
