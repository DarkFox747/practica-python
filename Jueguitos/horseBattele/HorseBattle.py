
from traceback import print_tb

# pide muchos recursos pero anda pa nashe
lst=[5, 15, 17, 3, 8, 11, 28, 6, 55, 7]
lst2=list()
dic = dict()
dic2 = dict()
for num in lst:
    dic[num]= dic.get(num,0)+1
rep = [i  for i,j in dic.items() if j >1]
if rep != []:
    print(rep)
else:
    for i in lst:
        for x in lst:
            if i == x:
                continue
            else:
                r =abs(i-x)
            dic2[r]=dic2.get(r,0)+1
            # lst2.append(abs(r))
    # lst2.sort()
    print(min(dic2))


# mas eficiente
# lst.sort()
# m=float('inf')
# for i in range(len(lst)-1):
#     m=min(abs(lst[i+1]-lst[i],m))