#adding 1 in last element of list


print('provide comma separated values :')
list_num=input()
print('input :',list_num)
str_num=''.join(map(str,list_num.split(',')))
int_num=int(str_num)
add_num=int_num+1
out_num=str(add_num)
result_num =[]
for x in out_num:
    result_num.append(int(x))
    x=int(x)
    x+=1

print ('output :' , result_num)
