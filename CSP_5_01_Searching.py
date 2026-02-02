import random


def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    cnt = 0
    while(True):
        cnt +=1
        i = random.randint(0,len(items)-1)
        if items [i] == target:
            print(cnt)
            return i


def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.

    for i in range(0,len(items)):
        if items [i] == target:
            return i, i+1

    return -1, i+1


def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    cnt = 0
    l = 0
    r = len(items)-1

    while(True):
        cnt+=1
        mid = l+ int((r-1)/2)
        if items[mid] == target:
            return mid, cnt
        elif items[mid] < target:
            l=mid+1
        else:
            r=mid-1
        if r < l:
            return -1,cnt
