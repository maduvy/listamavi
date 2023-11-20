produto1=input("digite um numero: ")
produto2 = input("digite outro numero: ")
produto3 = input("digite mais um numero: ")
if produto1 > produto2 and produto1 > produto3:
   print("vc deve comprar o produto1".format(produto1))
   
elif produto2 > produto1 and produto2 > produto3:
    print("vc deve comprar o produto2".format(produto2)) 
      
else:       
    print("vc deve comprar o produto3".format(produto3))