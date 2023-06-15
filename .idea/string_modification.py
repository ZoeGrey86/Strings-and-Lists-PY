def pig_latin(string):
    pig = string[2:len(string)] + string[0] + string[1] + 'a'
    for x in range (len(string)):
        x = x + 1
    print(pig)

def run_program():
    print('please input a string')
    string = input('')
    pig_latin(string)