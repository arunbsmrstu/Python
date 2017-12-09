primes = range(2, 20)
for i in range(1, 8):
    primes = filter(lambda x: x == i or x % i==0, primes)
print(list(primes))


for num in range(1,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)


#for num in range(1,101):
 #   prime = True
  #  for i in range(2,num):
   #     if (num%i==0):
    #        prime = False
    #if prime:
     #  print (num)