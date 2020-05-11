# with open("data.txt",'r') as file:
#    content = file.readlines()
#    for i in content:
#        word =i.split()
#        print(word)

# training=["java",'python','aws']
# print("my trainings are :")
# print(" ".join(training))

# try:

#     filehandler=open('testing.txt','r')
#     content=filehandler.read()
#     print(content)
   

# except:
#     print("Enter the correct name of file")

# finally:
#      filehandler.close()


# argv--> helps to read command line arguments / variables from scripts--> unpacks your values


from sys import argv
nameofprogram , filename = argv


print("Name of program is :", nameofprogram)
print("Name of file is", filename)


while True:
    try:
 
        fh=open(filename,'r')
        content=fh.read()
        print(content)
        fh.close()
        break

    except:
        print("The name entered is wrong. Provide correct name")
        try_again = input("DO you want to try again? Press 'Y' for Yes and press 'N' for NO!!")
        if try_again == "Y":
            filename = input("Please enter the correct file name this time")
        else:
            break

    
    


