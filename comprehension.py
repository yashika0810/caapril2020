# numbers=[1,2,3,4,5,6,7,8]
# new_list=[]
# for i in numbers:
#     if i%2==0:
#         new_list.append(i**2)

# print(new_list)


# s="Hello 1234 consultadd"
# new=[x for x in s if x.isalpha()]
# print("".join(new))


# my_list=[]
# for i in [20,40,60]:
#     for j in [2,4,6]:
#         my_list.append(i*j)
# print(my_list)

# #consultadd--> cnsltdd
# def get_vowels(string):
#     return [i for i in string if i not in 'aeiou']
# obj=get_vowels("consultadd")
# print("".join(obj))


# def palin(a):
#     return a==a[::-1]
# print(palin("mom"))

# li=[1,2,3,4,5,1]
# l=[]
# for i in li:
#      if i in l:
#           pass
#      else:
#           l.append(i) 
# print(l)





# def dup(l):
#     x=[]
#     result=[]
#     for i in l:
#         if i not in x:
#             x.append(i)
#         else:
#             result.append(i)
#     return result
# print(dup([1,2,3,1,2,4,7,4]))


# li=[1,2,3,4,5,4,3,1]
# d=dict()
# for i in li: 
#     d[i]=d.get(i,0)+1 
#     new=[i for i in d if d[i]>1] 
# print(new) 









# new_list=[1,2,3,3,4,5,2,1]
# new=[]
# var=[list[new.append(i)] for i in new_list if i not in new[]]
# prtin(var) 

# new_list=[1,2,3,3,4,5,2,1]
# res = []
# for i in new_list:
#     if i not in res:
#         res.append(i)
# print(str(res))