#import json
//TODO Test
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

def log2(num):
    if num < 1:
        log_num = 2 ** num
#        log_dict[str(log_num)] = "2^x = {} >> x = log2({}) >> x = {}".format(str(log_num), str(log_num), str(num))
#        print(json.dumps(log_dict, indent=4))
        log_stack.push("{}: logbase2({}):: 2^x = {} >> x = log2({}) >> x = {}".format(str(num), str(log_num), str(log_num),
                        str(log_num), str(num)))
        return
    log_num = 2 ** num
#    log_dict[str(log_num)] = "2^x = {} >> x = log2({}) >> x = {}" .format(str(log_num), str(log_num), str(num))
#    print("{}: ".format(str(num)), log_dict[str(log_num)])
    log_stack.push("{}: logbase2({}):: 2^x = {} >> x = log2({}) >> x = {}".format(str(num), str(log_num), str(log_num),
                    str(log_num), str(num)))
    num -= 1
    log2(num)

def log_stack_print():
    if log_stack.is_empty():
        return
    print_val = log_stack.pop()
    print(print_val)
    log_stack_print()


log_stack = Stack()
print("log base 2 or log2(x) means how many times do I need to multiply 2 by itself (exponents) to get x.\n\n")
num = int(input("Enter the highest number to create a log2 list for: "))
#log_dict = {}
log2(num)
log_stack_print()