nums=[1,3,4,6,5,7,13,23,55,44,55,34,77,78,74,75]
eval_list=[]
for i in nums:
    if i%2==0:
        eval_list.append(i)
print(f"筛选出来的偶数列表是{eval_list}")
#新增新功能
def cal_sun(a,b):
    toatal=a+b
    return toatal
class Rectange(object):
    def __init__(sel,a,b):
        self.length=a
        self.width=b
    def get_area(self):
        return self.length*self.width
    def get_perimeter(self):
        return 2*(self.length+self.width)
retangle=Rectangle(5,10)
print(retangle.get_area())
print(retangle.get_perimeter())
if __name__=="__main__":
    num=10
    num2=18
    res=cal_sun(num1,num2)
    print("计算结果是{res}")
nums2=[1,-5,8,-3,10,14]
def outer(fn):
    def inner(name):
        print(f"新产生的列表是{fn(name)}")
    return inner
@outer
def funa(nums):
    a=[]
    for i in nums:
        if i>=0:
            a.append(i)      
    return a
funa(nums2)


