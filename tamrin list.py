# tamrin list mohsmmad abdollahi gol
# tabe sazande list(2 parantez),list((5,10,15,20,25,30,35,40))
print('lotfan list besaz:5,10,15,20,25,30,35,40=',list((5,10,15,20,25,30,35,40)))
a= [5,10,15,20,25,30,35,40]
# list items= moratab,ghabe taghyeer,tekrar pazir
# index: a[3]=20
print('a[3]=',a[3])
# mahdoode index: a[0:5]=5,10,15,50,25(index az [0] shoroo mishavad)
print("a[0:5]=",a[0:5])
# a[4:]=25,30,35,40
print("a[4:]=",a[4:])
# index manfi:
print('3 ta adad ghable akhar list:  (a[-4:-1])=',a[-4:-1])    
# varoone:  a[::-1] =[40,35,30,25,20,15,10,5]
print("dastresi varoone:  a[::-1]=",a[: :-1])
# list varoone =[40,35,30,25,20,15,10,5]
a.reverse()
print("KHOROOJI VAROONE  (a.reverse())=", a)
# tekrar pazir
print("khasiat tekrar paziri:  n*[]=" ,a*2)
# tool list: tedad item
print('tedad item dar list:  len(a)=',len(a))
# type list
b=['mohammad','abdollahi','gol']
print('type str ya int dar list:',type(b))
# taghyeer item dar list
b[0]='mohammad ebrahim'
print('tagheer item aval=',b)
# metod .insert -darj item dar andex moshakhas list
b.insert(3 ,'ebne barat')
print('ebne barat be item sevom ezafe konid:(b.insert)=',b)
# metod .append -mazid item dar entehaye list
b.append('1358')
print('be enteha ,sal tavalod ezafe shavad:(b.append(1358))=',b)
# metod .remove -hazf item moshakhas shode dar list
b.remove('1358')
print('az enteha sal tavalod hazf shavad:(b.remove(1358))=',b)
# metod .pop : hazfe index moshakhas shode list
b.pop(3)
print('(item ebne barat) hazf shavad:(b.pop(3)) =',b)
#  del : hazfe index moshakhas shode list
del b[0]
print('(item aval hazf shavad:del b[0]=',b)
# metod .clear : khali shodane mohtavaye list
b.clear()
print('lotfan mohtaviate list ra hazf konid:(b.clear())=',b)
# metod .extend : afzoodane yek list be liste digar
b.extend(a)
print('list a ra dar list b vared konid:(b.extend(a))=', b)
# baresi mojood boodane yek item dar list
if 25 in b :
    print('aya adad 25 dar liste b vojood darad?:yes')
# halgheye for dar list    
for i in (b):
    print('for i in (b):', i)
for i in range(len(b)):
    print('for i in range(len(b)):', i)
 # halgheye while dar list
i = 0
while i < len(b):
  print(b[i])
  i = i + 1


  

