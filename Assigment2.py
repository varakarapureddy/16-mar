#write a program to separate even numbers and odd numbers.
s=input()
l=list(s)
x=[]
for i in l:
    x.append(int(i))
res=[]
odd=[]
even=[]
for i in x:
    if i%2==1:
        odd.append(i)
    else:
        even.append(i)
res.extend(odd)
res.append(" ")
res.extend(even)
for i in (res):
    print(i,end='')
