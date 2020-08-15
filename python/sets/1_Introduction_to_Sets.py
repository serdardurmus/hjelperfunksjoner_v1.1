# Now, let's use our knowledge of sets and help Mickey.

# Ms. Gabriel Williams is a botany professor at District College. 
# One day, she asked her student Mickey to compute the average of all the 
# plants with distinct heights in her greenhouse.

def average(array):
    summ = 0
    for i in set(array):
        summ +=i
    return summ / len(set(array))

if __name__ == '__main__':
    # n = int(input())
    arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
    result = average(arr)
    print(result)