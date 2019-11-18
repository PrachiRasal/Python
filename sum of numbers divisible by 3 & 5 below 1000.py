total=0

for ele in [i for i in range(1000)] :
    if (ele%3==0 or ele%5==0):
        total=total+ele
    else:
        continue

print("Total:",total)
