
def arithmetic_arranger(problems, statprint=False):
    # check problema lista
    first = ''
    second = ''
    sumx = ''
    lines = ''
    # El problema maximo es 5
    if len(problems) >= 6:
        return 'Error: Too many problems.'
    # Dividir problema para separar componentes.
    for i in problems:
        a = i.split()
        firsts = a[0]
        seconds = a[2]
        operands = a[1]
        # comprobar la longitud del número, máximo 4 dígitos
        if (len(firsts) > 4 or len(seconds) > 4):
            return "Error: Numbers cannot be more than four digits."

        # verifique la entrada como dígitos válidos
        if not firsts.isnumeric() or not seconds.isnumeric():
            return "Error: Numbers must only contain digits."

        if (operands == '+' or operands == '-'):
            if operands == "+":
                sums = str(int(firsts) + int(seconds))
            else:
                sums = str(int(firsts) - int(seconds))
            # establecer la longitud de la suma y los valores superior, inferior y de línea
            length = max(len(firsts), len(seconds)) + 2
            top = str(firsts).rjust(length)
            bottom = operands + str(seconds).rjust(length - 1)
            line = ''
            res = str(sums).rjust(length)
            for s in range(length):
                line += '-'
            #agregar a la cadena general
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            return "Error: Operator must be '+' or '-'."
    # eliminar los espacios a la derecha de la cadena
    first.rstrip()
    second.rstrip()
    lines.rstrip()
    if statprint:
        sumx.rstrip()
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        arranged_problems = first + '\n' + second + '\n' + lines
    return arranged_problems

#probando la funcion

if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
    print(arithmetic_arranger(['1 + 2', '1 - 9380'], True))
    print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'], True))
    print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True))
    print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'], True))
    print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'], True))
    print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'], True))
    print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'], True))
    print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
    print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
