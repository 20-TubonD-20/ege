with open('25-B.txt') as fin:
    size = int(fin.readline())

    minR = 0
    kCh = 0
    kN = 0
    maxC = 0

    for i in range(size):
        arr = [int(n) for n in fin.readline().split()]
        if(arr[0] > arr[1]):
            maxC += arr[0]
            if(arr[0]%2==0):
                kCh+=1
                if(arr[1] %2 !=0 and (minR == 0 or arr[0]-arr[1] < minR)):
                   minR = arr[0]-arr[1]
            else:
                kN+=1
                if(arr[1] %2 ==0 and (minR == 0 or arr[0]-arr[1] < minR)):
                   minR = arr[0]-arr[1]
        else:
            maxC += arr[1]
            if(arr[1]%2==0):
                kCh+=1
                if(arr[0] %2 !=0 and (minR == 0 or arr[1]-arr[0] < minR)):
                   minR = arr[1]-arr[0]
            else:
                kN+=1
                if(arr[0] %2 ==0 and (minR == 0 or arr[1]-arr[0] < minR)):
                   minR = arr[1]-arr[0]

    if(maxC%2==0 and kCh < kN):
        maxC = maxC - minR
    elif(maxC%2!=0 and kN < kCh):
        maxC = maxC - minR

    print(minR)
    print(maxC)

fin.close()

            
