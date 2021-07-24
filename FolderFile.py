import os

path = 'D:\\Temp'


def listdir(path, level):
    # folders first
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('  ' * level + path + '\\' + i)
            listdir(path + '\\' + i, level + 1)
    # files second
    for i in os.listdir(path):
        if os.path.isfile(path + '\\' + i):
            print('  ' * level + path + '\\' + i)


print(path)

listdir(path, 1)
