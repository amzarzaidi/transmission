entree = "00010111001010001"
# mettre un buffer de 00 avant de string. pr exemple, si le bit est 0110, mettez 000110. 
result = []

def add(a, b, c=0):
    result = a + b + c
    return result % 2

for i in range(2, len(entree)):
    bit1 = add(int(entree[i-1]), int(entree[i]))
    bit2 = add(int(entree[i-2]), int(entree[i-1]), int(entree[i]))
    result.append(bit2)
    result.append(bit1)

result_string = ''.join(map(str, result))
print(result_string)
