#Metodo recursivo para ordenar una lista de numeros
def sorting(list):
    print(sorted_list, list)
    #Caso base
    if len(list)==0:
        print("Lista ordenada")
        return sorted_list
    #Caso recursivo
    else:
        i=0
        while (i<len(list)-1):
            if list[0]>list[i+1]:
                list[0],list[i+1]=list[i+1],list[0]
                print(sorted_list, list)
            else:
                i+=1
                print(sorted_list, list)
        sorted_list.append(list.pop(0))
        sorting(list)
    return sorted_list

#Lista de numeros
list=[8, 4, 6, 2]
#Lista ordenada
sorted_list=[]

print("Lista desordenada")
print(list)
print("Ordenando...")
print(sorting(list))