# This execute global vareable & class
# parent one & parent two from child

class parent_one_:
    x=800
    def driving(self):
        print("hi i am from parent two & good in hiking")
class parent_two_:
    def hiking(self):
        print("hi i am from child")
class child(parent_one_,parent_two_):
    def driving(self):
        print("hi i am from parent 90km/p")
xyz=child()
xyz.hiking()
xyz.driving()
print(xyz.x)