#Find first recurring element

print('Provide input string :')
list1=input()
input_str=list(list1)
##print(input_str)
x=0
y=1
out_str=[]
while x<(len(input_str)-1):
    y=x+1
    while y<len(input_str):
        if input_str[x]==input_str[y]:
            out_str.append(input_str[x])
            break
        y+=1
    x+=1       

print('First Recurring character:',out_str[0])
print('All recurring characters:',set(out_str))
