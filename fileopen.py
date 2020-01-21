todos = open('todos.txt', 'a')

print('Put out the trash', file=todos)
print('Fed the cat', file=todos)
print('Prepare the tax return', file=todos)

todos.close()

task = open('todos.txt')

for chore in task:
    print(chore, end='')

task.close()
