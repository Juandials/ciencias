

def poligono(lista,numero_lados,longitud_lados,n):
    suma_lados=0
    p=numero_lados
    for i in range(n):
        for j in range(i-n,i):
            suma_lados=suma_lados+lista[j]
            if suma_lados>longitud_lados:
                suma_lados=0
                break
            if suma_lados==longitud_lados:
                #print(p)
                p=p-1
                suma_lados=0
            if p==0:
                return True
    return -1


n=int(input())
while n!=0:
    lista = list(map(int,input().strip().split()))[:n]
    s=sum(lista)
    for i in range(n,2,-1):
        if s%i==0:
            numero_lados=i
            longitud_arco=s/i
            if poligono(lista,numero_lados,longitud_arco,n)==True:
                print(n-i)
                break
    else:
        print (poligono(lista,numero_lados,longitud_arco,n))
                
            
    n=int(input())
