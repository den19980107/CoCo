
while 1:
    n = int(input())
    input1 =[]
    array =[]

    for i in range(n):
        input1.append(input())
        input1[i] = input1[i].replace(' ','')
    for i in range(n):
       array.append([])
   
    for row in range(n):
        for col in range(n):
            array[row].append(col)
            array[row][col] = 0
    newArray = array
    
    for row in range(n):
        for col in range(row+1):
            array[row][col] = input1[row][col]
    print(input1)
    for row in range(n-2,-1,-1):
        for col in range(row+1):
            if int(array[row+1][col]) > int(array[row+1][col+1]):#下比右下大
                newArray[row][col] = int(array[row][col])+int(array[row+1][col])
            else:
                newArray[row][col] = int(array[row][col])+int(array[row+1][col+1])
    print(newArray)


