lst1=[1,3,5,7,9,11,34]
lst2=[5,13,45,7,20,65,1]
s=int(0)
c=int(0)
for i in lst1 and lst2:
    if len(lst1)==len(lst2):
        print("list are of same lenghth")
        break
    else:
        print("list have different lenghth")
        break
for i in range(0,len(lst1) and len(lst2)):
         s=s+lst1[i]
         c=c+lst2[i]
for i in range(0,len(lst1) and len(lst2)):
        if s==c:
         print("sum of values are same")
         break
        else:
            print("sum of values are different")
            break
print("Elements that matched are:")
l=[]
for i in range(0,len(lst1)):
    for j in range(0,len(lst2)):
     if lst1[i]==lst2[j]:
         l.append(lst1[1]and lst2[j])
    else:
        p=i
        continue
print(l)                 