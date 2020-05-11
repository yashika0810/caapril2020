# x=[1,2,6,8,9,8]
# for i in x:
#     print('list elements: ', i)
# print("the list has", len(x), 'elements')

# x=[1,2,4,6,8,9]


#range((len(x)))--->len(x)-->6 -->range(6)-->[0,1,2,3,4,5]
# for i in range((len(x))):
#     x[i]=x[i]**2
# print(x)

# #1+2+3+4+5
# sum=0
# for value in range(1,20,2):
#     sum=sum*value
# print(sum)


# for i in range(3):
#     for x in range(10,14):
#         for j in range(100,104):
#             print(i,x,j)

# x=[1,2,4,5,6,7]

# #range(len(x))--> len(x)--> 6 --> range(6)--> [0,1,2,3,4,5]
# for i in range(len(x)):
#     x[i]=x[i]**3
# print(x)

# x=[1,2,3,4,5]
# sum=0
# for value in range(1,6):
#     sum=sum+value
# print(sum)



#n=5 --> {1:1 ,2:4 ,3:9,4:16 ,5:25}

# n=int(input("ENter any number"))
# d=dict()
# for i in range(n):#--> range(1,6)--> (1,2,3,4,5)
#     d[i]=i**3
# print(d)


#s="consultadd123"
#s=ConsSULTsad --> isupper(), islower()

# s=input("Enter any sentence")
# d={"DIGITS":0, "LETTERS": 0}
# for i in s:
#     if i.isdigit():
#         d["DIGITS"]+=1
#     elif i.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass # executes nothing

# print("LETTERS", d["LETTERS"])
# print("DIGITS", d['DIGITS'])

# testString = "ConsultaddTraining123"
# solDict = {}
# for i in testString:
#     if i in solDict:
#         solDict[i] += 1
#     else:
#         solDict[i] = 1
# print(solDict)


x=[1,2,5,9,7]
for elements in x:
    if elements%2==0
        print("List contains an even no")
        break
 #This else executes only if break is NEVER reached and loop terminated after all its iterations 

else:
    print("List does not contain even no")


for i in range(1,10):
    if i%11==0:
        break
    print(i)
else:
    print("Not printed")