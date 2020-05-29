
#Función que determina si todas las cifras entre i y j son iguales
def cerouno(st,i,j):
    p=st[i]
    for k in range(i+1,j+1):
        if p!=st[k]:
            return("No")
    return("Si")



#Programa
st=str(input())
n=int(input())
arr=[]
contador=1
while st!='\n':
    for k in range(n):
        arr.append(list(map(int,input().split(" "))))
        if arr[k][0]>arr[k][1]:
            aux=arr[k][0]
            arr[k][0]=arr[k][1]
            arr[k][1]=aux
    print("Caso",contador)
    for k in range(n):
        print(cerouno(st,arr[k][0],arr[k][1]))
    st=str(input())
    n=int(input())
    arr=[]
    contador=contador+1

    #NUNCA SALE DEL WHILE!!! HAY QUE SOLUCIONAR






        
