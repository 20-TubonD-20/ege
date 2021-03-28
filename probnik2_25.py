with open('25-A.txt') as fin:
    size = int(fin.readline())

    minR = 0
    summ = 0
    b = 0 #0 a-b else b-a
    chislo = 0
    for i in range(size):
        arr = [int(n) for n in fin.readline().split()]
        if(arr[0] < arr[1]):
            summ += arr[0]
            if(((arr[1]%3==0 and arr[0]%3!=0) or (arr[0]%3==0 and arr[1]%3!=0) ) and (minR == 0 or arr[1] - arr[0] < minR)):
               minR = arr[1] - arr[0]

        else:
            summ += arr[1]
            if(((arr[1]%3==0 and arr[0]%3!=0) or (arr[0]%3==0 and arr[1]%3!=0)) and (minR == 0 or arr[0] - arr[1] < minR)):
               minR = arr[0] - arr[1]

            
               
    
    if(summ%3!=0): summ+=minR

    print(summ)

fin.close()
            
        
