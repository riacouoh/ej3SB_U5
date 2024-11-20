def mezcla_equilibrada_ordenar(lista, depth=0):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    print(f"{'  ' * depth}Dividiendo: {lista} -> Izquierda: {lista[:medio]}, Derecha: {lista[medio:]}")
    
    izquierda = mezcla_equilibrada_ordenar(lista[:medio], depth + 1)
    derecha = mezcla_equilibrada_ordenar(lista[medio:], depth + 1)
    
    resultado = mezclar(izquierda, derecha, depth)
    print(f"{'  ' * depth}Resultado combinado: {resultado}")
    
    return resultado

def mezclar(izquierda, derecha, depth):
    resultado = []
    indice_izquierda, indice_derecha = 0, 0
    
    while indice_izquierda < len(izquierda) & indice_derecha < len(derecha):
        if izquierda[indice_izquierda] < derecha[indice_derecha]:
            resultado.append(izquierda[indice_izquierda])
            indice_izquierda += 1
        else:
            resultado.append(derecha[indice_derecha])
            indice_derecha += 1
            
    resultado.extend(izquierda[indice_izquierda:])
    resultado.extend(derecha[indice_derecha:])
    
    print(f"{'  ' * (depth + 1)}Mezclando: {izquierda} y {derecha} -> {resultado}")
    return resultado

def main():
    n = int(input("¿Cuántos números deseas ordenar? "))
    lista = []
    for i in range(n):
        num = int(input(f"Introduce el número {i + 1}: "))
        lista.append(num)
    
    print("Lista original:", lista)
    lista_ordenada = mezcla_equilibrada_ordenar(lista)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()
