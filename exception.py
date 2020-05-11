while True:
    try:
        x=int(input("Enter any number"))
        z=int(input("Enter any number"))
        avg=(x+y)/2
     
    except ValueError:
        print("Please provide integer value")
    
    except NameError:
        print("Please provide correct value")
    
    else:
        print("The average is ",avg)
   
