inp=open("/content/drive/MyDrive/CSE221 Lab/Lab 01/input 1b.txt", 'r')
end=open("/content/drive/MyDrive/CSE221 Lab/Lab 01/output 1b.txt", 'w')
t=inp.readline()

for i in range(0,int(t)):
    current_num=inp.readline()
    exp=current_num[10:]

    for j in exp:
        if j=='+' or j=='-' or j=='*' or j=='/':
            operator=j
            break

    num1, num2= exp.split(operator)

    if operator=='+':
        end.write(f'The result of {num1}{operator}{num2} is {int(num1) + int(num2)}\n')
    elif operator=='-':
        end.write(f'The result of {num1}{operator}{num2} is {int(num1) - int(num2)}\n')
    elif operator=='*':
        end.write(f'The result of {num1}{operator}{num2} is {int(num1) * int(num2)}\n')
    elif operator=='/':
        end.write(f'The result of {num1}{operator}{num2} is {int(num1) / int(num2)}\n')


inp.close()
end.close()