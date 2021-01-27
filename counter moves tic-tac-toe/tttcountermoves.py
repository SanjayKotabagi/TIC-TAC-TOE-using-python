import random as r
arr = [ ' ',' ',' ',' ',' ',' ',' ',' ',' ']
total = 0
if1=if2=if3=if4=if5=if6=if7=if8=if9=if10=if11=if12=if13=if14=if15=if16 = 0
def board(p,value):
    if(arr[p] == 'O' or arr[p] == 'X'):
        print("Place already occupied \n Enter diffrent position :) ")
        return 0
    else:
        arr.__delitem__(p)
        arr.insert(p,value)
        for i in range(9):
            print(" ",arr[i] ,"|",end="")
            if(i==2 or i==5):
                print()
                print(" --------------")
        print()
        print()
        print("------------------------------------------------------------")
        pccounter()
        for i in range(9):
            print(" ",arr[i] ,"|",end="")
            if(i==2 or i==5):
                print()
                print(" --------------")       
        return 1
    
    
def pccounter():
    flag=0
    global if1,if2,if3,if4,if5,if6,if7,if8,if9,if10,if11,if12,if13,if14,if15,if16
    while(flag == 0):
        if (arr[0] == 'X' and arr[1] == 'X' and if1==0):
            pcpos = 2
            flag = pcinsert(pcpos)
            if1 = 1
        elif (arr[0] == 'X' and arr[4] == 'X' and if2==0):
            pcpos = 8
            flag = pcinsert(pcpos)
            if2==1
        elif (arr[0] == 'X' and arr[3] == 'X' and if3==0):
            pcpos = 6
            flag = pcinsert(pcpos)
            if3==1
        
        elif (arr[1] == 'X' and arr[2] == 'X' and if4==0):
            pcpos = 0
            flag = pcinsert(pcpos)
            if4==1
        elif (arr[1] == 'X' and arr[4] == 'X' and if5==0):
            pcpos = 7
            flag = pcinsert(pcpos)
            if5==1
            
        elif (arr[2] == 'X' and arr[5] == 'X' and if6==0):
            pcpos = 8
            flag = pcinsert(pcpos)
            if6==1
        elif (arr[2] == 'X' and arr[4] == 'X' and if7==0):
            pcpos = 6
            flag = pcinsert(pcpos)
            if7==1
        
        elif (arr[3] == 'X' and arr[4] == 'X' and if8==0):
            pcpos = 5
            flag = pcinsert(pcpos)
            if8==1
        elif (arr[3] == 'X' and arr[6] == 'X' and if9==0):
            pcpos = 0
            flag = pcinsert(pcpos)
            if9==1
        
        elif (arr[4] == 'X' and arr[5] == 'X' and if10==0):
            pcpos = 3
            flag = pcinsert(pcpos)
            if10==1
        elif (arr[4] == 'X' and arr[7] == 'X' and if11==0):
            pcpos = 1
            flag = pcinsert(pcpos)
            if11==1
        elif (arr[4] == 'X' and arr[8] == 'X' and if12==0):
            pcpos = 0
            flag = pcinsert(pcpos)
            if12==1
        elif (arr[4] == 'X' and arr[6] == 'X' and if13==0):
            pcpos = 2
            flag = pcinsert(pcpos)
            if13==1
            
        elif (arr[5] == 'X' and arr[8] == 'X' and if14==0):
            pcpos = 2
            flag = pcinsert(pcpos)
            if14==1
        
        elif (arr[6] == 'X' and arr[7] == 'X' and if15==0):
            pcpos = 8
            flag = pcinsert(pcpos)
            if15==1
        
        elif (arr[7] == 'X' and arr[8] == 'X' and if16==0):
            pcpos = 6
            flag = pcinsert(pcpos)
            if16==1
        else:
            pcpos = r.randint(0,8)   
            flag = pcinsert(pcpos)
    return
            
                
def pcinsert(pcpos):    
    status = 0
    global total
    total += 1
    if(total > 3):
        verify(arr)
        return 1
    while(status==0):
        if(arr[pcpos] == 'O' or arr[pcpos] == 'X'):
            return 0
        else:
            arr[pcpos] = 'O'
            return 1
        
             
    
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
        
arrs = [0,1,2,3,4,5,6,7,8]        
print("User => X \nComputer => O")
for i in range(9):
    print(" ",arrs[i] ,"|",end="")
    if(i==2 or i==5):
        print()
        print(" --------------")
i=0;
while(i<5):
    userpos = int(input("Enter the position in which you want X to be : "))
    res = board(userpos,'X')
    if (res == 1):
        i += 1
print()
print("THANK YOU")