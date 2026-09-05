nums=[1,3,4,6,5,7,13,23,55,44,55,34,77,78,74,75]
eval_list=[]
for i in nums:
    if i%2==0:
        eval_list.append(i)
print(f"打印出来的偶数列表是{eval_list}")
