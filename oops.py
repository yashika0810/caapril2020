class employee:
    def name(self,x,y):
        return x+y

obj=employee()
print(obj.name(2,3))


class employee:
    def name(self, firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname

obj1=employee()
obj1.name("yashika","khatri")
print(obj1.firstname, obj1.lastname)
