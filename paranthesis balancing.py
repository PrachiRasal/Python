open_par = ["[","{","("] 
close_par = ["]","}",")"]

def input_str(in_str):
    count=0
    stack = []
    if len(in_str.strip())==0:
        return False
    else:
        for i in in_str:
            if i in open_par: 
                stack.append(i)
            elif i in close_par: 
                pos = close_par.index(i)
                if ((len(stack) > 0) and (open_par[pos] == stack[len(stack)-1])): 
                    stack.pop()
                else: 
                    return False
        if len(stack) == 0: 
            return True
        else:
            return False

string = input("Enter String:")
print(string,"-", input_str(string)) 
  
