numbers = [4,3,2,10,12,1,5,6]

for index in range(len(numbers)-1):
    print(numbers)
    if (numbers[index+1] < numbers[index]):
        for sort in range(len(numbers)-1):
            if (numbers[index+1] < numbers[sort]):
                numbers.insert(sort,numbers[index+1])
                numbers.pop(index+2)
                break

print(numbers)