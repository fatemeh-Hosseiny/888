# in mashin hesab az + ,- ,* ,/ ra ba taghadom ha va vojood () hal mikonad.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
#################################################
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    # add an element to top of stack
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    # deleting the top node
    
    def pop(self):
        if self.isEmpty():
            return None
        theNode = self.head
        theData = theNode.data
        self.head = theNode.next
        del theNode
        self.size -= 1
        return theData
    # returning the top node
    def top(self):
        if self.isEmpty():
            return None
        return self.head.data

    def isEmpty(self):
        return self.size == 0
    
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
###################################################################

###################################################################
# operation class is for evaluate expressions
class Operation:
    def __init__(self,expression):
        self.exp = expression
        self.COLLECTION = ["(",")","[","]","{","}"]
    # making number's stack and character's stack
    def StackMaker(self):
        self.charstack = Stack()
        self.numberstack = Stack()
    # delete number's stack and character's stack for space management
    def deleteStacks(self):
        del self.charstack
        del self.numberstack
    # a function wich is being used to check bracket's balance
    def checker(self):
        self.checkerstack = Stack()
        for char in self.exp:
            if char in self.COLLECTION:
                self.checkerstack.push(char)
                if self.checkerstack.top() == ")":
                    self.checkerstack.pop()
                    if self.checkerstack.top() == "(":
                        self.checkerstack.pop()
                    else:
                        return False
        result = self.checkerstack.isEmpty()
        del self.checkerstack
        return result
        # a function for operation's priority
    def priority(self,char):
        if char == "+" or char == "-":
            return 1
        elif char == "*" or char == "/" :
            return 2
        elif char =="^":
            return 3
        else:
            return 0
        # calculation the sub expressions
    def simpleOperator(self,num1,num2,char):
        if char == "+":
            return int(num1 + num2)
        if char == "-":
            return int(num2 - num1)
        if char == "*":
            return int(num2 * num1)
        if char == "/":
            return float(num2 / num1)
        if char == "^":
            return int(num2**num1)
        # main function wich evaluate the main expression
    def Operator(self):
        # check in order to figure out if brackets are balanced or not 
        if self.checker():
            i = 0
            self.StackMaker()
            # iterate the expression to handle the stacks with priorities
            while i < len(self.exp):
                # identify ( in expresion
                if self.exp[i] == "(":
                    self.charstack.push(self.exp[i])
                # identify numbers in expression
                elif self.exp[i].isnumeric():
                    num = 0
                    #identify full numbers for instace 23 instead of 2,3
                    while i < len(self.exp) and self.exp[i].isnumeric():
                        num = (num*10) + int(self.exp[i])
                        i += 1
                    self.numberstack.push(num)
                    i -= 1
                # finding ) to operate
                elif self.exp[i] == ")":
                    while not self.charstack.isEmpty() and self.charstack.top() != "(":
                        num1 = self.numberstack.pop()                    
                        num2 = self.numberstack.pop()
                        charr = self.charstack.pop()
                        self.numberstack.push(self.simpleOperator(num1,num2,charr))
                    self.charstack.pop()
                else:
                    self.charstack.push(self.exp[i])
                i += 1
                # calculating the stacks with priority
            while not self.charstack.isEmpty():
                num1=self.numberstack.pop()
                num2=self.numberstack.pop()
                charr = self.charstack.pop()
                self.numberstack.push(self.simpleOperator(num1,num2,charr))
            finalres = self.numberstack.top()
            self.deleteStacks()
            return finalres
        else:
            return "brackets are not balanced"
#########################################################


exp = input()
exp = "(" + exp + ")"
exp.replace(" ","")
exp.replace("{","(")
exp.replace("}",")")
exp.replace("[","(")
exp.replace("]",")")
for i in range(len(exp)):
    if exp[i].isnumeric() and exp[i+1] == "(":
        self.exp = exp[:i+1] + "*"+exp[i+1:]
expression = Operation(exp)
print(expression.Operator())
