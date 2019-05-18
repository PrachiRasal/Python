
##-------------Method 1-------------##
original = list(range(97, 123))
input1="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
input2=list(input1)
output2=input2
output1=[ord(x) for x in input2]
i= 0
while i < len(input2):
    if output1[i] in original:
        if output1[i] not in [121,122]:
            output2[i]=(chr(output1[i]+2))
        elif output1[i] == 121:
            output2[i]=(chr(97))
        elif output1[i] == 122:
            output2[i]=(chr(98))
            
    else:
         output2[i]=(chr(output1[i]))

    i=i+1
   
print("".join(output2))



##-------------Method 2-------------##
from string import *
input1="abcdefghijklmnopqrstuvwxyz"
output1="cdefghijklmnopqrstuvwxyzab"
str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
trans= str.maketrans(input1,output1)
print(str.translate(trans))
