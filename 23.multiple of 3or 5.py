#1,2,3,4,5,6,7,8,9,
#3 or 5 bakhshpazir bashand
#3,5,6,9-> sum=23
#100000
n=1000
jam=0
rangeadad=range(1,n)
for anynumber in rangeadad:
    if anynumber%3==0 or anynumber%5==0:
       jam=jam+anynumber
       print(jam)