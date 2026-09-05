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

if __name__=="__main__":
    num=10
    num2=18
    res=cal_sun(num1,num2)
    print("计算结果是{res}")
