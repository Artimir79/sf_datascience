from collections import deque
def brackets(line):
    
    dq = deque()
    string = list(line)
   
    for element in string:
        if element == '(':
            dq.append(element)
        if element == ')' and len(dq) == 0:
            return False
        elif element == ')' and len(dq) != 0:
            dq.pop()
    if len(dq) == 0:
        return True
    return False

print(brackets("(()())"))  
print(brackets(""))
print(brackets("(()()))"))