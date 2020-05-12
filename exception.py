while True:
    try:
        x=int(input("Enter any number"))
        z=int(input("Enter any number"))
        avg=(x+y)/2
     
    except ValueError:
        print("Please provide integer value")
    
    except NameError:
        print("Please provide correct value")
        
    except IOError:
        print("Error!!! Can't open the file")
    
    else:
        print("The average is ",avg)
   
