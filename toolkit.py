
from functools import wraps

import os
import random
import re
security=True

def fun_starter(fun):
    @wraps(fun)
    def wrapper():
        os.system('cls')
        print(f'\t\t\t\twellcome to {fun.__name__}')
        fun()
    return wrapper

@fun_starter
def character_counter():
    text= input('Enter a word :\n--> ')
    count_value={}
    for i in text:
        count_value[i]=text.count(i)
    for i in count_value: 
        print(f'{i} -----> {count_value[i]}')
    print(f'Total character  ------> {len(text)}')
    flow_control(character_counter)
@fun_starter
def text_replacer():
    o_text=input('Enter Text:\n--> ')
    old_text=input('Enter Old Text:\n--> ')
    new_text=input('Enter New Text:\n--> ')
    print(f'your Text\n\n{o_text.replace(old_text,new_text)}')
    flow_control(text_replacer)
@fun_starter
def python_help():
    print(help())
    flow_control(help)
@fun_starter
def Guess_game():

    print('You have only 10 guesses')
    wining_number= random.randint(1,100)
    guess_times_left =10
    guess_times_count= 1
    game_over=False
    while not game_over:
        number= int(input("Enter a number between 1 to 100:\n"))
        if number!=wining_number:
            if number >wining_number:
                print('too high')
            elif number<wining_number:
                print('too low')
            guess_times_left-=1
            guess_times_count+=1
            print(f'{guess_times_left} guess are left')
        elif  number==wining_number:
            print(f'you win this game after {guess_times_count} guess')
            game_over=True
            
        if guess_times_left==0:
            print('you lose this game \n  Game over')
            game_over= True
    flow_control(Guess_game)
@fun_starter
def i_d__u_Python_package():
    print('you can\'t use this fun\n under working')
    flow_control(i_d__u_Python_package)
@fun_starter
def password_generator():
    characters ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*'
    length_pw=(input('Enter the length of requide password \n--> '))
    number_pw=(input('Enter the number of requide password \n--> '))
    
    for i in range(0,int(number_pw)):
        pw=''
        for i in range(0,int(length_pw)):
            pw+= random.choice( characters)
        print('your Generated Password is ',pw)
    flow_control(password_generator)
@fun_starter
def email_validation_checker():
    condition ='^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    email=input('Enter your email :\n--> ')
    if re.search(condition,email):
        print('valid email')
    else:
        print('invalid email')
    flow_control(email_validation_checker)

def flow_control(fun_name):
    while True:
        choice= input(f'''
        Enter your choice
        1.Back Main Menu 
        2.Continue current tool 
        3.lock Tool kit
        4.Exit
    -->''')
        if choice == '1':
            os.system('cls')
            main_menu()
        elif choice=='2':
            fun_name()
        elif choice=='3':
            Security()
        elif choice == '4':
            print("Thank for using my Toolkit  \n"
                "Follow me on My YouTube Channel wadood academy")
            exit()
        else:
            os.system('cls')
            print('input error')
            continue

def  Security():
    os.system('cls')
    print('\t\t\t\t\twellcome to python Tool kit')
    for i in range(1,4):
        password=input('Enter Toolkit password\n--> ')
        if password=='123':
            return main_menu()
        else:
            print('worng password')
    os.system('cls')
    print('\t\tyour are not my boss so you can not use my Tool')
    input()
    exit()

def main_menu():
    os.system('cls')
    global security
    if security==True:
        security = False
        Security()
    
    choice_input= input('''
    Enter your choice 
    1.) Python 3.7's help utility 
    2.) Character and length Counter
    3.) Text Replacer 
    4.) Guess game
    5.) Install,Delete and Update Python package
    6.) Password Generator 
    7.) Email Validation Checker
    8.) lock Tool kit
    --> ''')
    if choice_input=='1':
        python_help()
    elif choice_input =='2':
        character_counter()
    elif choice_input == '3':
        text_replacer()
    elif choice_input=='4':
        Guess_game()
    elif choice_input =='5':
        i_d__u_Python_package()
    elif choice_input=='6':
        password_generator()
    elif choice_input == '7':
        email_validation_checker()
    elif choice_input=='8':
        Security()
    else:
        main_menu()

main_menu()
