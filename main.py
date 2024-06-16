PATH = '/home/danimir/PycharmProjects/LazyDo/'

def usage_help():
    return 'Usage: command\nhelp - print this help message\nlist or l - print all tasks\nadd task1, task2 - add "task1" and "task2"\ncomplete task1, task2 - move "task1" and "task2 to archive\narchive - show archive\nexit - close the app'


def tasks_list():
    with open(f'{PATH}TODO', 'r') as file:
        res = file.read()
    return res


def add_tasks(tasks: list):
    with open(f'{PATH}TODO', 'a') as file:
        file.write('\n' + '\n'.join(tasks))


def move_tasks_to_archive(complete_tasks: list):
    tasks_to_move = []
    wrong_tasks = []
    with open(f'{PATH}TODO', 'r') as file:
        tasks = file.read().split('\n')
        for i in range(len(complete_tasks)):
            if complete_tasks[i] in tasks:
                tasks.remove(complete_tasks[i])
                tasks_to_move.append(complete_tasks[i])
            else:
                wrong_tasks.append(complete_tasks[i])
    with open(f'{PATH}TODO', 'w') as file:
        file.write('\n'.join(tasks))
    with open(f'{PATH}archive', 'a') as file:
        file.write('\n'.join(tasks_to_move) + '\n')
    if wrong_tasks:
        print(f'Tasks "{', '.join(wrong_tasks)}" are not in TODO-list')


def archive():
    with open(f'{PATH}archive', 'r') as file:
        res = file.read()
    return res[:-1]


def exec_func(prompt: str):
    if prompt == 'help':
        print(usage_help())
    elif prompt in ('list', 'l'):
        print(tasks_list())
    elif prompt[0:3] == 'add':
        add_tasks(prompt[4:].split(', '))
    elif prompt[0:8] == 'complete':
        move_tasks_to_archive(prompt[9:].split(', '))
    elif prompt[0:7] == 'archive':
        print(archive())
    else:
        print('Incorrect command. Type "help" for available command list.')


while True:
    command = input('\n>>> ')
    print('\n' * 100)
    if command == 'exit':
        break
    else:
        exec_func(command)
