def ordenamientoPorMezcla(unaLista):
    print("Dividir ", unaLista)
    if len(unaLista) > 1:
        mitad = len(unaLista) // 2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]

        ordenamientoPorMezcla(mitadIzquierda)
        ordenamientoPorMezcla(mitadDerecha)

        i = 0
        j = 0
        k = 0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                unaLista[k] = mitadIzquierda[i]
                i = i + 1
            else:
                unaLista[k] = mitadDerecha[j]
                j = j + 1
            k = k + 1

        while i < len(mitadIzquierda):
            unaLista[k] = mitadIzquierda[i]
            i = i + 1
            k = k + 1

        while j < len(mitadDerecha):
            unaLista[k] = mitadDerecha[j]
            j = j + 1
            k = k + 1
    print("Mezclar ", unaLista)

tamaño = int(input("¿Cuántos elementos tendrá la lista? "))

unaLista = []
for i in range(tamaño):
    elemento = int(input(f"Ingresa el elemento {i + 1}: "))
    unaLista.append(elemento)

print("\nLista inicial:", unaLista)
ordenamientoPorMezcla(unaLista)

print("Lista ordenada:", unaLista)
