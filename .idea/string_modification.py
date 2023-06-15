def pig_latin(string):
    pig = string[2:len(string)] + string[0] + string[1] + 'a'
    print(pig)

def run_program():
    string = input('please input a string\n')
    pig_latin(string)