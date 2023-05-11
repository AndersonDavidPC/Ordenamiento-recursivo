# Método recursivo para ordenar una lista de números

Este repositorio contiene una implementación de un método recursivo para ordenar una lista de números en orden ascendente.

## Descripción del algoritmo

El algoritmo utiliza un enfoque recursivo para ordenar la lista de números. Funciona de la siguiente manera:

1. **Caso base**: Si la longitud de la lista es igual a cero, significa que la lista está vacía y se considera ordenada. En este caso, se devuelve una lista vacía.

2. **Caso recursivo**: Si la lista no está vacía, el algoritmo realiza los siguientes pasos:

   a. Se inicializa un índice `i` en cero.

   b. Se itera a través de los elementos de la lista (excepto el primer elemento) utilizando un bucle `while`. En cada iteración, se compara el primer elemento con el elemento actual. Si el primer elemento es mayor, se intercambian los elementos.

   c. Después de completar el bucle, se agrega el primer elemento a una lista auxiliar llamada `sorted_list` y se elimina de la lista original.

   d. Luego, se llama recursivamente al método `sorting` con la lista actualizada.

   e. Finalmente, se devuelve la lista `sorted_list`, que contiene los elementos ordenados.

## Uso del código

1. Define una lista de números desordenados.

2. Crea una lista vacía llamada `sorted_list`.

3. Llama al método `sorting` pasando la lista desordenada y la lista `sorted_list`.

4. El método `sorting` imprimirá los pasos intermedios del proceso de ordenamiento y, finalmente, imprimirá la lista ordenada.

```python
# Ejemplo de uso

# Lista de números desordenados
list = [8, 4, 6, 2]

# Lista vacía para almacenar los números ordenados
sorted_list = []

print("Lista desordenada:")
print(list)
print("Ordenando...")
print("Lista ordenada:")
print(sorting(list))
```

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna mejora para el código, puedes abrir un "issue" o enviar una solicitud de extracción.