import zeroP
import oneP

while(True):
    sys_type = int(input('0P:0, 1P:1\n>>')) #0P:先に撮影　1P:先に受取
    if(sys_type == 0):
        print('0P')
        break
    elif(sys_type == 1):
        print('1P')
        break
    else:
        print('Put 0 or 1')



if (sys_type == 0): #0P
    print('0P')
    
elif(sys_type == 1):
    print('1P')
    
