##revers of string(stacks)
def reverse_stack(str):
    # Create an empty stack (list to use as stack)
    stack = []
    # Push all characters of string to stack
    for char in str:
        stack.append(char)
    # Pop all characters of string
    # and add it to the rev
    rev = ''
    while len(stack) > 0:
        last = stack.pop()
        rev = rev + last
        # print(last, rev)
       
    return rev
usr_str = input('What is your string:')
reverse = reverse_stack(usr_str)
print('Reversed is: ', reverse)
