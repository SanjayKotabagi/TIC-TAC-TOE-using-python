import random as r
arr = [ '0','1','2','3','4','5','6','7','8']
total = 0
def board(p,value):
    if(arr[p] == 'O' or arr[p] == 'X'):
        print("Place already occupied \n Enter diffrent position :) ")
        return 0
    else:
        arr.__delitem__(p)
        arr.insert(p,value)
        pcinsert()
        for i in range(9):
            print(" ",arr[i] ,"|",end="")
            if(i==2 or i==5):
                print()
                print(" --------------")       
        return 1
    
    
def pcinsert():
    status = 0
    while(status==0):
        pcpos = r.randint(0,8)
        if(arr[pcpos] == 'O' or arr[pcpos] == 'X'):
            status = 0
        else:
            status = 1
            arr.__delitem__(pcpos)
            arr.insert(pcpos,'O')  
            global total
            total += 1
    if(total > 3):
        verify(arr)
        return
        
             
    
def verify(arr):
    items = ['X','O']
    for item in items:
        flag=0;
        for i in range(3):
            if(item == arr[i]):
                flag += 1
                if(flag==3):
                    win(item)
                    return
        flag=0;
        for i in range(3,6,1):
            if(item == arr[i]):
                flag += 1
                if(flag==3):
                    win(item)
                    return
        flag=0;
        for i in range(6,9,1):
            if(item == arr[i]):
                flag += 1
                if(flag==3):
                    win(item)
                    return
        flag=0;
        for i in range(0,7,3):
            if(item == arr[i]):
                flag += 1
                if(flag==3):
                    win(item)
                    return
        flag=0;
        for i in range(1,8,3):
            if(item == arr[i]):
                flag += 1
                if(flag==3):
                    win(item)
                    return
        flag=0;
        for i in range(2,9,3):
            if(item == arr[i]):
                flag += 1
                if(flag==3):
                    win(item)
                    return
        flag=0;
        for i in range(0,9,4):
            if(item == arr[i]):
                flag += 1
                if(flag==3):
                    win(item)
                    return
        flag=0;
        for i in range(2,7,2):
            if(item == arr[i]):
                flag += 1
                if(flag==3):
                    win(item)
                    return
            
def win(item):
    if (item == 'X'):
        print("""
                             hurrayyyyyyyyyyyyyyyyyy
                                !!! USER WINS !!!
        """)
        
    elif (item == 'O'):
        print("""
                             nopeeeeeeeeeeeeeeeeeee
                             !!! COMPUTER WINS !!!
        """)
    return
        
        
print("User => X \nComputer => O")
arr = [ '0','1','2','3','4','5','6','7','8']
for i in range(9):
    print(" ",arr[i] ,"|",end="")
    if(i==2 or i==5):
        print()
        print(" --------------")
i=0;
while(i<4):
    userpos = int(input("Enter the position in which you want X to be : "))
    res = board(userpos,'X')
    if (res == 1):
        i += 1
print()
print("THANK YOU")
    