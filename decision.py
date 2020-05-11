# x=int(input("Enter any number"))
# if x < 0:
#     if(x > -5):
#         print("result is greater than -5")
#     else:
#         print("result is less than -5")

# elif x==0:
#     print("result is 0")
# elif x>0 and x<30:
#     print("result is positive and in range of 30")
# else:
#     print("result is greater than 30")



# while True:
#     print("Enter any number but -1 will quit the loop and -2 will keep you in the loop")
#     x=int(input("Enter the number"))
#     if x==-1:
#         break
#     if x==-2:
#         continue
#         print(" I am inside")
# print("I am outside the loop")


avg=0
total=0
count=0
print("Enter the grade (-1 to quit) ")
grade=int(input("Enter your grades"))
while grade!=-1:
    total=total+grade
    count=count+1
    print("Enter grades")
    grade=int(input("Enter your grades"))
    if count==3:
        break


avg=total/count
print("Avg of subjects is" , avg)    







