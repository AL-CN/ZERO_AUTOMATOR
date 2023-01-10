# ALCO This code is made for automation in dealing with files, directories, and folders. (next version will be focused on renaming them)
import genericpath
import os
import pathlib

text2 = '\n You fail to choose a valid option! Try again!'
variable_general = ''

def main_function():
    main_messages()

def clear_console():
    os.system('cls')

def main_messages():
    text = '\n Hello, choose one of the functions to be display from the OS Library: \n(1) - Show the location from which this code is running \n(2) Show from which platform are you running this code \n(3) Create a folder \n(4) Remove a folder \n[5] Exit the program \n Type here: '
    f_contact = (input(text))
    ans = ['1', '2', '3','4','5']
    while f_contact not in ans:
        print(text2)
        f_contact = (input(text))
    if f_contact == '1':
        show_directory()
        contin()
    elif f_contact == '2':
        name_plataform()
        contin()
    elif f_contact == '3':
        create_directory()
        contin()
    elif f_contact == '4':
        remove_folder()
        contin()
    elif f_contact == '5':
        exit()

#utility function
def contin():
    ans = ['yes', 'no']
    question = input('\nDo you want to continue? \n Type yes or no: ')
    while question.lower() not in ans:
        print(text2)
        question = input('\nDo you want to continue? \n Type yes or no: ')
    if question.lower() == 'yes':
        main_function()
        clear_console()
    elif question.lower() == 'no':
        exit()

#option function
def remove_folder():
    #Texts and condition lists
    ans3 = ['1', 'yes', '2', 'no', '3']
    entry_text = f'\nDo you want to remove a folder from the current directory or from a specific path?\n(1) Current directory - {pathlib.Path.cwd()}\n(2) Specific path \n[3] Go Back to start menu\nType here: '
    entry_folder = '\nWhat is the name of the folder that you wanna delete?\nType here:'
    entry_path = '\nWhat is the path that you wanna delete?\nType here:'
    error_text = '\nThe typed folder does not exist!'
    error_path = '\nThe typed path does not exist!'
    alert_text = '\nYou are going to delete the folder below!'
    alert_text2 = '\nYou are going to delete the path below!'
    continuation = '\nDo you want to continue? [YES] OR [NO]?\n\nType here: '

    #Variables
    current = pathlib.Path.cwd()

    #Funtions
    def option1():
        entry_quest2 = input(entry_folder)
        select_folder = str(current) + '\\' + entry_quest2
        verify_folder = genericpath.exists(select_folder)

        while verify_folder == False:
            entry_quest3 = input(f'{error_text} \n {continuation}')
            while entry_quest3 not in ans3:
                entry_quest3 = input(f'{text2} \n {continuation}')
            if entry_quest3.lower() == ans3[1]:
                option1()
            elif entry_quest3.lower() == ans3[3]:
                main_function()
        if verify_folder == True:
            entry_quest4 = input(f'{alert_text} \n {select_folder} <- (this folder) {continuation}')
            while entry_quest4.lower() not in ans3:
                print(text2)
                entry_quest0 = input(continuation)
                while entry_quest0 not in ans3:
                    print(text2)
                    entry_quest0 = input(continuation)
                if entry_quest0 == ans3[1]:
                    entry_quest4 = input(f'{alert_text} \n {select_folder} <- (this folder) {continuation}')
                if entry_quest0 == ans3[3]:
                    entry_quest4 = ans3[3]
            if entry_quest4 == ans3[1]:
                os.rmdir(select_folder)
                print('\nThe folder has been deleted!\nGoing back to star menu...')
                main_function()
            elif entry_quest4 == ans3[3]:
                remove_folder()

    def option2():
        entry_quest5 = input(entry_path)
        verify_path = genericpath.exists(entry_quest5)

        while verify_path == False:
            entry_quest6 = input(f'{error_path} \n {continuation}')
            while entry_quest6 not in ans3:
                print(text2)
                entry_quest6 = input(f'{error_path} \n {continuation}')
            if entry_quest6 == ans3[1]:
                option2()
            elif entry_quest6 == ans3[3]:
                main_function()

        if verify_path == True:
            entry_quest7 = input(f'{alert_text2} \n {entry_quest5} <- (this path) {continuation}')
            while entry_quest7.lower() not in ans3:
                print(text2)
                entry_quest00 = input(continuation)
                while entry_quest00 not in ans3:
                    print(text2)
                    entry_quest00 = input(continuation)
                if entry_quest00 == ans3[1]:
                    entry_quest7 = input(f'{alert_text2} \n {entry_quest5} <- (this path) {continuation}')
                if entry_quest00 == ans3[3]:
                    entry_quest7 = ans3[3]

            if entry_quest7.lower() == ans3[1]:
                os.rmdir(entry_quest5)
                print('\nThe path has been deleted!\nGoing back to star menu...')
                main_function()
            elif entry_quest7.lower() == ans3[3]:
                remove_folder()

    entry_quest = input(entry_text)

    while entry_quest not in ans3:
        print(text2)
        entry_quest = input(entry_text)
    if entry_quest == ans3[0]:
        option1()
    elif entry_quest == ans3[2]:
        option2()
    elif entry_quest == '3':
        main_function()

def create_directory():
    text = f'\nDo you want to create the folder on the current location or on a specific path? \n (1) Current Directory - {pathlib.Path.cwd()}\n (2) Specify the path \n [3] Go back start menu \n\nType here: '
    question = input(text)
    ans1 = ['1', '2', '3']
    while question not in ans1:
        print(text2)
        question = input(text)
    if question == ans1[0]:
        index = 0
        while index == 0:
            name = input('\nType the name of the folder that you want to create!\nType here: ')
            current_folder = pathlib.Path.cwd()
            verify_folder = str(current_folder) + '/' + name
            if genericpath.exists(verify_folder) == False:
                os.mkdir(verify_folder)
                index = 1
                contin()
            else:
                print('\nThe folder already exists\n')
    elif question == '2':
        name = input('\nType the name of the folder that you want to create!\nType here: ')
        path = input('\nType the path to were you want to create the past:\nType here: ')
        folder_info = rf'{path}\{name}'
        os.mkdir(folder_info)

    elif question == '3':
        main_function()

def name_plataform():
    name = os.name
    if name == 'nt':
        print("\nYou'r running this code on a Windows ('nt') platform!")
    else:
        print(f"\nYou'r running this code on a {name} platform!")
def show_directory():
    diretorio = os.getcwd()
    print(f'\nThe current directory is: \n{diretorio} \n')

main_function()
#remove_folder()
#create_directory()




'''  ans2 = ['yes', 'no']  # utility variable
    ans = ['1', '2']
    text_q2 = '\nDo you wanna restart this mode or go back to star menu?\n(1) Restart\n(2) Go back to star menu\n\nType here: '

    def removal_op1():
        text_function = '\nWhat is the name of the folder which you wanna remove?\nType here: '
        verified_folder = genericpath.exists(verifiy_folder_existince(text_function))
        while verified_folder == False:
            error_text = "\nThe informed folder does't exist!\n\nDo you want to try again? [Yes] or [No]\nType here: "
            error = input(error_text)
            while error.lower() not in ans2:
                print(text2)
                error = input(error_text)
            if error == ans2[0]:
                removal_op1()
            elif error == ans[1]:
                clear_console()
                main_function()
        if verified_folder == True:
            alert = input(f'\WE ARE GOING TO DELETE THIS FOLDER: {verifiy_folder_existince(0)}\nARE YOU SURE OF THIS? [YES] OR [NO]\nType here: ')
            if alert.lower() == ans2[0]:
                print(f'{verifiy_folder_existince(0)} Has been deleted!')
                os.rmdir(verifiy_folder_existince(0))
                contin()
            elif alert.lower() == ans2[1]:
                question2 = input(text_q2)
                while question2 not in ans:
                    print(text2)
                    question2 = input(text_q2)
                if question2 == ans[0]:
                    clear_console()
                    removal_op1()
                if question2 == ans[1]:
                    clear_console()
                    main_function()


    def removal_op2():
        while genericpath.exists(verify_folder) == False:
            text3 = "\nThe informed path does't exists! or isn't available\n\nDo you want to try again? [Yes] or [No]\nType here: "
            error = input(text3)
            while error.lower() not in ans2:
                print(text2)
                error = input(text3)
            if error == ans2[0]:
                removal_op2()
            elif error == ans2[1]:
                clear_console()
                main_function()
        if genericpath.exists(verifiy_folder_existince()) == True:
            text_alert = f'\WE ARE GOING TO DELETE THIS PATH: {verify_folder}\nARE YOU SURE OF THIS? [YES] OR [NO]\nType here: '
            alert = input(text_alert)
            while alert not in 2:
                print(text2)
                alert = input(text_alert)
            if alert.lower() == ans2[0]:
                os.rmdir(verify_folder)
            elif alert.lower() == ans2[1]:
                text_q2 = '\nDo you wanna restart this mode or go back to star menu?\n(1) Restart\n(2) Go back to star menu\n\nType here: '
                question2 = input(text_q2)
                while question2 not in ans:
                    print(text2)
                    question2 = input(text_q2)
                if question2 == ans[0]:
                    clear_console()
                    removal_op2()
                if question2 == ans[1]:
                    clear_console()
                    main_function()

    text = f'\n Do you want to remove a folder from the current directory or from a specific path?\n(1) Current directory - {pathlib.Path.cwd()}\n(2) Specific path\n Type here: '
    question = input(text)

    while question not in ans:
        print(text2)
        question = input(text)
    if question == ans[0]:
        removal_op1()
    elif question == ans[1]:
        removal_op2()
'''


'''


IMG_2021(7)04(9)04_054814


import os

pasta_origem = r'D:\Pasta teste\\'

for arquivo in os.listdir(pas):
    backup_name = pasta_teste + arquivo
    novo_nome = pasta_teste + 'TESTE' + arquivo
    os.rename(backup_name, novo_nome)

print(os.listdir(pasta_teste))


'''
