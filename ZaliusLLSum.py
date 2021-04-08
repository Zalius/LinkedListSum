
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self , sign):
        self.head = node()
        self.sign = sign

    def isNeg(self):
        if self.sign == "-":
            return True
        return False

    #adds a new data
    def append(self , data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    #gives us the length of linked list
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    #prints out and display linked list
    def display(self):
        if self.isNeg():
            print("-" ,end=" ")
        else:
            print("+", end=" ")
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    # Returns the value of the node at 'index'
    def get(self , index):
        if index >= self.length() or index < 0:
            print("ERROR: 'GET' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx +=1

    def erase(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'GET' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


def Sum(x1 , x2):
    num1 = 0
    num1_is_pos = 1

    num2 = 0
    num2_is_pos = 1

    if x1.isNeg():
        num1_is_pos = -1

    if x2.isNeg():
        num2_is_pos = -1

    for i in range(x1.length()):
        num1 += int(x1.get(i)) * pow(10,x1.length() - 1 -i)
    num1 *= num1_is_pos

    for i in range(x2.length()):
        num2 += int(x2.get(i)) * pow(10,x2.length() - 1 -i)
    num2 *= num2_is_pos

    print("The sum of these two number is:" + str(num1 + num2))
    sum = num1 + num2
    sum_is_pos = True
    if sum < 0:
        sum_is_pos = False

    if sum_is_pos:
        x3 = linked_list("+")
    else:
        x3 = linked_list("-")

    for i in range(len(str(sum))):
        x3.append(str(sum)[i])
    x3.display()
    return x3





test_list = linked_list("-")
test_list.append(1)
test_list.append(4)
test_list.append(5)
test_list.append(3)
test_list.append(9)
test_list.display()
print(test_list.length())
print(test_list.get(0))
test_list.display()

test_list2 = linked_list("+")
test_list2.append(2)
test_list2.append(4)
test_list2.append(7)
test_list2.append(8)
test_list2.display()

imTheSum = Sum(test_list2, test_list)
imTheSum.display()
