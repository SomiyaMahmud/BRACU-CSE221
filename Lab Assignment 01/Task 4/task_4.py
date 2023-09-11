inp=open('/content/drive/MyDrive/CSE221 Lab/Lab 01/input 4.txt','r')
out=open('/content/drive/MyDrive/CSE221 Lab/Lab 01/output 4.txt', 'w')
t=inp.readline()

name=[]
place=[]
time=[]

for i in range(int(t)):
    train=list(inp.readline().strip().split())
    name.append(train[0])
    place.append(train[4])
    time.append(train[6])

for j in range(int(t)):
    idx=j
    for k in range(j+1,int(t)):
        if name[k]<name[idx]:
            idx=k
    name[j],name[idx]=name[idx],name[j]
    place[j],place[idx]=place[idx],place[j]
    time[j],time[idx]=time[idx],time[j]

dic={}
for l in range(int(t)):
    if name[l] in dic:
        dic[name[l]][0].append(time[l])
        dic[name[l]][1].append(place[l])
    else:
        dic[name[l]]=[[time[l]],[place[l]]]

for val in dic.values():
    for m in range(len(val[0])):
        idx=m
        for n in range(m+1,len(val[0])):
            if val[0][n]>val[0][idx]:
                idx=n
        val[0][m],val[0][idx]=val[0][idx],val[0][m]
        val[1][m],val[1][idx]=val[1][idx],val[1][m]

for key, values in dic.items():
    for value in range(len(values[0])) :
        out.write(f'{key} will departure for {values[1][value]} at {values[0][value]}\n')


inp.close()
out.close()