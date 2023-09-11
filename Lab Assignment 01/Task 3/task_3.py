inp=open('/content/drive/MyDrive/CSE221 Lab/Lab 01/input 3.txt', 'r')
out=open('/content/drive/MyDrive/CSE221 Lab/Lab 01/output 3.txt', 'w')
t=inp.readline()
id=inp.readline().strip().split(' ')
marks=inp.readline().strip().split(' ')


for i in range(int(t)):
    idx=i
    for j in range(i+1,int(t)):
        if marks[j]>marks[idx]:
            idx=j
    marks[i],marks[idx]=marks[idx],marks[i]
    id[i],id[idx]=id[idx],id[i]


dic={}
for k in range(int(t)):
    if marks[k] in dic:
        dic[marks[k]].append(id[k])
    else:
        dic[marks[k]]=[id[k]]

for key, value in dic.items():
    for val in sorted(value):
        out.write(f'ID: {val} Marks: {key}\n')


inp.close()
out.close()