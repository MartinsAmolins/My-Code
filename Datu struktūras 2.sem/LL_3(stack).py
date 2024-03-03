class Node:
    def __init__(self, value, position):
        self.value = value
        self.position = position
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def is_empty(self):
        return self.height == 0

    def push(self, value, position):
        new_node = Node(value, position)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        return temp

def balancets(s):
    stack = Stack()
    brackets_map = {')': '(', '}': '{', ']': '['}

    ######  Write your program here   ######
    ######                            ######
    ######                            ######
    ######                            ######
    ########################################
    for i, char in enumerate(s,start=1):
        if char in brackets_map.values(): #check if value is corespodnign 
            stack.push(char,i)
        elif char in brackets_map.keys(): #check if the values is asigned index which is is the other value in this case is coresponding 
            if stack.is_empty():
                return i
            else:
                x = stack.pop()
                if brackets_map[char] != x.value:
                    return i
        if not stack.is_empty():
            return stack.top.position
        else:
            return "Success"

s = input("Ievadiet rindu: ")
print(balancets(s))
