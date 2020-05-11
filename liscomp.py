# numbers=[1,2,3,5,6,8]
# new_list=[]
# for i in numbers:
#     if i%2==0:
#         new_list.append(i)
# print(new_list)


# my_list=[]
# for i in [20,40,60]:
#     for j in [2,4,6]:
#         my_list.append(i*j)
# print(my_list)


s="hello 1234 consultadd"
new=[i for i in s if i.isdigit()]
print("".join(new))