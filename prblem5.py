a = [1,4,3,6,8,7,1,2,1]
b = [3,9,8,0,11,2,1,1]
c=[]

for i in range(0,len(a)):
   for j in range(0,len(b)):
       if(a[i]==b[j]):
           c.append(a[i]);

c=set(c);
c=list(c);
print(c);

print(set(a).intersection(b))


