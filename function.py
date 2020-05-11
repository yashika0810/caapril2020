#with argument w return type

# def add(): #--> Formal parameters
#     print("this is the second type")
#     a=int(input("Enter value of a"))
#     b=int(input("Enter value of b"))
#     return(a+b)

# a=add() #actual paramters

# print(a)

def is_even(l):
    list1=[]
    for i in l:
        if i%2==0:
            list1.append(i)
    return list1
print(is_even([1,2,3,4,5,7,43,13]))


#s=ConsultaddTraining1234

# def check(str1):
#     new_dict={}
#     for i in str1:
#         if i.isalpha():
#             if i in new_dict:
#                 new_dict[i]+=1
#             else:
#                 new_dict[i]=1
#         else:
#             pass
#     return new_dict
# print(check("Consultadd1234"))


def reverse(str1):
    new=''
    index=len(str1)
    while index>0:
        new+=str1[index-1] #--> Consultadd len=10, index=10 str1[9]--> d --> new='dd'
        index=index-1 #index=9
    return new
print(reverse("consultadd"))
















