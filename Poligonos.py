

def poligono(lista,numero_lados,longitud_lados):
    suma_lados=0
    p=numero_lados
    for i in range(len(lista)):
        #print("iterazioa",i)
        for j in range(i-len(lista),i):
            suma_lados=suma_lados+lista[j]
            #print("Lista[j]",lista[j])
            #print(suma_lados)
            if suma_lados>longitud_lados:
                suma_lados=0
                break
            if suma_lados==longitud_lados:
                #print(p)
                p=p-1
                suma_lados=0
            if p==0:
                return True


n=int(input())
while n!=0:
    #lst1 = [int(item) for item in input("Enter the list items : ").split()]
    lista = list(map(int,input().strip().split()))[:n]
    s=sum(lista)
    for i in range(s//2,2,-1):
        if s%i==0 and n>=i:
            #print(i)
            numero_lados=i
            longitud_arco=s/i
            #print("numero de lados:",numero_lados)
            #print("longitud_arco:",longitud_arco)
            if poligono(lista,numero_lados,longitud_arco)==True:
                print(n-i)
            elif i==3:
                print(-1)
                
            
    n=int(input())
                    
                




    
          
        
#print(poligono([2,2,3,5,1,4,1],5,4))

    #Como máximo vamos a tener un conjunto de n-numero lados-1
    
    







    
    
    
