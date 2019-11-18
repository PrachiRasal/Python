Values=(input("Enter set of comma separated values:"))

list1= Values.split(',')

for element in list1:
    if int(element)%3==0 and int(element)%5==0:
        print("FIZZBUZZ")
    elif int(element)%3==0:
        print("FIZZ")
    elif int(element)%5==0:
        print("BUZZ")
    else:
        print(None)
