# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1954004
# Date: 7.11.2022

#function for getting the data from the user
def getting_the_inputs():
    global progress
    global defer
    global fail
    global std_id
    global std_id_list
    global total
    std_nbr=0
    #declaring the range that credits should be at
    global range_1
    print("please enter UOW IDs only")
    #input student ID
    std_id = input("Enter the student ID:")
    if std_id[0]=='w' or std_id[0]=='W':
        try:
            #Check whether the entered stud id have 7 characters
            std_nbr=int(std_id[1:])
            if std_nbr in range(1,9999999):
                std_id_list.append(std_id)
                try :
                    #input pass credits and check whether it is out of range
                    progress=int(input("Enter the progress:"))
                    if progress not in range_1:
                        print('out of range')
                    else:
                        #input defer credits and check whether it is out of range
                        defer=int(input("Enter the defer:"))
                        if defer not in range_1:
                            print('out of range')
                        else:
                            #input fail credits and check whether it is out of range
                            fail=int(input("Enter the fail:"))
                            if fail not in range_1:
                                print('out of range')
                            else:
                                #proceed if the 
                                total=progress+defer+fail
                                if total!=120:
                                    print('Total incorrect')
                                else:
                                    #returning data to use in another function
                                    return (progress,defer,fail,std_id_list,std_id,total)
                except:
                    print('Integer required')
            else:
                print(' enter a valid student id')
        except:
            print (' enter a valid student id')
    else:
        print(' enter a valid student id')

#function for the process of the credits and to create the lists that uses in this program    
def getting_the_list(progress, defer, fail, std_id):
    global LIST
    global LIST_2
    global DICT
    global hg_progress
    global hg_mt
    global hg_exclude
    global hg_dr
    global prog_outcome
    #declaring the range of fail credits to exclude
    range_2=(80,100,120)
    if progress==120:
        prog_outcome='Progress'
        #getting the count to use in the histogram
        hg_progress=hg_progress+1
    elif progress==100:
        prog_outcome='Progress-module trailer'
        hg_mt=hg_mt+1
    elif fail in range_2:
        prog_outcome='Exclude'
        hg_exclude=hg_exclude+1
    else:
        prog_outcome='Do not progress-module retriever'
        hg_dr=hg_dr+1
    #creating a simple list for each outcome
    LIST=(prog_outcome ,'-', progress, ',', defer, ',', fail)
    #appending the simple list to the main list to use it as a nested list
    LIST_2.append(LIST)
    #creating the dictionary as well
    DICT[std_id]=LIST
    return (LIST_2, hg_progress, hg_mt, hg_exclude, hg_dr, LIST, DICT, prog_outcome)

#function for the histogram
def histogram(hg_progress, hg_mt, hg_exclude, hg_dr, LIST_2):
    print('Progress', hg_progress,':', '*'*hg_progress)
    print('Progress-module trailer', hg_mt,':', '*'*hg_mt)
    print('Do not progress-module retriever', hg_dr,':', '*'*hg_dr)
    print('Exclude', hg_exclude,':', '*'*hg_exclude)
    print(len(LIST_2), ' outcomes in total.')

#function for printing the dictionary
def dictionary(std_id_list, DICT):
    for num in range (len(std_id_list)):
        id=std_id_list[num]
        output=DICT.get(id)
        print(id,' : ',*output)
    
    
    
#funtion for the use of saff
def menu(LIST_2):
    global loop
    choice_2=0
    choice_3=0
    choice_4=0
    print('''enter 1 to enter another set of data
enter 2 to quit''')
    try:
        choice_2=int(input('Enter your choice: '))
        if choice_2==1:
            loop = True
        elif choice_2==2:
            loop = False
            print('''enter 1 to display the histogram
enter 2 to print the list
enter 3 to save the list to a file
enter 4 to get the dictionary
enter 5 to quit''')
            try:
                choice_3=int(input('Enter your choice: '))
                if choice_3==1:
                    #calling the functions
                    histogram(hg_progress, hg_mt, hg_exclude, hg_dr, LIST_2)
                    
                elif choice_3==2:
                    loop = False
                    #printing the list 1 by 1 from the main list
                    for i in range (len(LIST_2)):
                        print(*LIST_2[i])
                    
                elif choice_3==3:
                    loop = False
                    print('''Enter 1 to overwrite the file (Warning : This will DELETE all the data stored in the file)
Enter 2 to append your data to the file''')
                    try :
                        choice_4=int(input('Enter your choice : '))
                        if choice_4 == 1:
                            try:
                                file = open('student.txt','x')
                                file.close()
                                file = open("student.txt", "w")
                                for i in range (len(LIST_2)):
                                    file.write(''.join(map(str,LIST_2[i])))
                                    file.write('\n')
                                file.close()
                            except:
                                file = open("student.txt", "w")
                                for i in range (len(LIST_2)):
                                    file.write(''.join(map(str,LIST_2[i])))
                                    file.write('\n')
                                file.close()
                        if choice_4 == 2:
                            file = open("student.txt", "a")
                            for i in range (len(LIST_2)):
                                file.write(''.join(map(str,LIST_2[i])))
                                file.write('\n')
                            file.close()
                    except:
                        print('Integer Required')
                    
                    
                elif choice_3==4:
                    loop = False
                    dictionary(std_id_list, DICT)
                    
                elif choice_3==5:
                    loop = False
                    
                else:
                    print('Invalid choice')
                
            except:
                print('enter a valid input')

        else:
            print('Invalid choice')
    except:
        print('Integer required1')
    return(loop)

progress=''
defer=''
fail=''
std_id=''
hg_progress=0
hg_mt=0
hg_exclude=0
hg_dr=0
LIST_2=[]
LIST=[]
std_id_list=[]
DICT={}
loop = True
range_1=(0,20,40,60,80,100,120)
print('''enter 1 for the student part
enter 2 for the staff part
enter 3 to quit''')
try:
    choice_1=int(input('Enter your choice: '))
    if choice_1==1:
        getting_the_inputs()
        if progress in range_1 and defer in range_1 and fail in range_1 and total == 120:
            getting_the_list(progress, defer, fail, std_id)
            print(*LIST[0])
    elif choice_1 == 2:
        while loop == True:
            getting_the_inputs()
            if progress in range_1 and defer in range_1 and fail in range_1 and total == 120:
                getting_the_list(progress, defer, fail, std_id)
                print(prog_outcome)
                menu(LIST_2)
            if loop==False:
                break
    elif choice_1 == 3:
        exit()
    else:
        print('Invalid input')
except:
    print('Integer required ')

