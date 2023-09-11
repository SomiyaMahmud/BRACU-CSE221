

inp=open("/content/drive/MyDrive/CSE221 Lab/Lab 01/input 1a.txt" , 'r')
end=open("/content/drive/MyDrive/CSE221 Lab/Lab 01/output 1a.txt" , 'w')
t=inp.readline().strip()

for i in range(0,int(t)):
    current_num=inp.readline().strip()
    if int(current_num)%2==0:
        end.write(f'{current_num} is an Even number.\n ')
    else:
        end.write(f'{current_num} is a Odd number.\n ')

inp.close()
end.close()