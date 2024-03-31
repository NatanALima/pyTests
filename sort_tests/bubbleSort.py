from typing import List;

arr = [2, 5, 3, 1, 4];
arr2 = [1, 8, 5, 4, 2, 7, 3, 6]


# O primeiro Resultado que cheguei
'''
 A lógica usada para esse é:
 -> Percorrer todo o array passado na função e verificando os elementos de 2 em 2 (index > index + 1)
 -> O processo acima deverá se repetir até a variável RemainingRepeat chegue a zero
    -> A variável RemainingRepeat recebe o tamanho do array - 1 indicando quantas vezes o laço filho se repetirá
    -> A cada iteração completa do laço filho, a variável RemainingRepeat diminuirá em -1;
'''


def bubbleSortDefasado(arrValue: List[int]) -> List[int]:
    newArr = arrValue;
    remainingRepeat = len(arrValue) - 1;
    while remainingRepeat > 0:
        index = int(0);
        while index < len(arrValue) - 1:
            if newArr[index] > newArr[index + 1]:
                tempValue = newArr[index];
                newArr[index] = newArr[index + 1];
                newArr[index + 1] = tempValue;
            index += 1
        remainingRepeat -= 1;
    return newArr;


# Resultado Final (Melhorado utilizando outro código como referência)
def bubbleSort(arrValue: List[int]) -> List[int]:
    newArr = arrValue;
    for i in range(len(arrValue) - 1):
        for index in range(len(arrValue) - 1):
            if newArr[index] > newArr[index + 1]:
                tempValue = newArr[index];
                newArr[index] = newArr[index + 1];
                newArr[index + 1] = tempValue;
    return newArr;


sortedArr = bubbleSort(arr);
sortedArr2 = bubbleSort(arr2);
print(sortedArr)
print(sortedArr2)
