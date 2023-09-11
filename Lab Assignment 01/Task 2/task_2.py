inp=open('/content/drive/MyDrive/CSE221 Lab/Lab 01/input 2.txt', 'r')
out=open('/content/drive/MyDrive/CSE221 Lab/Lab 01/output 2.txt', 'w')
t=inp.readline()
current_num=inp.readline().split(' ')

for j in range(len(current_num)):
        flag=0
        for k in range(len(current_num)-j-1):
            if current_num[k]>current_num[k+1]:
                flag=1
                current_num[k], current_num[k+1] = current_num[k+1], current_num[k]

        if flag==0:
          break

for l in range(len(current_num)):
    out.write(f"{str(current_num[l])} ")


inp.close()
out.close()