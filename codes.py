#consultadd--> cnsltdd/ oua
def get_vowels(string):
    return [i for i in string if i not in 'aieou']
obj=get_vowels("consultadd")
print("".join(obj))


def palin(a):
    return a == a[::-1]
print(palin("abaca"))

n=2
s="consultadd"
print(s*2)


#chunk a list into smaller lists--> [1,2,3,4,5,6]--> [[1,2],[3,4],[5,6]]


def chunk(list,size):
    return [ list[i:i+size] for i in range(0,len(list),size)]
y=chunk([1,2,3,4,5,6,7,8,9],2)
print(y)





