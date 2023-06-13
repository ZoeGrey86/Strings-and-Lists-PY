def pig_latin(string):
    print(string)
    split = string.split(' ')
    reverse = split.reverse()
    print(split)

def run_program():
    print('please input a string')
    string = input('')
    pig_latin(string)