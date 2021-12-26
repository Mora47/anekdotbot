import random


def filter(string):
    string = string.replace('<br/>', '').replace('<p>', '').replace('<p>', '').replace('</p>', '').replace('</div>', '').replace('—', '\n').replace(']', '').replace('[', '')
    while(string[-1] == ' ' or string[-1] == ','):
        string = string[:-2]
    while(string[0] == ' ' or string[0] == ','):
        string = string[1:]
        print('vsdvcdvsd')
    return string


def randomPage(string):
    string = str(string) + str(random.randint(1, 100))
    return string


def randomInt(arr):
    l = len(arr)
    return random.randint(1, l-1)

    
def hrefFilter(string):
    if('href' in string):
        return False
    return True

