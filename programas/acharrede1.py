def nao_sei (op):
    octetos = op.split('.')
    add = 0
    for i, octeto in enumerate(octetos):
        add += int(octeto) << (24 - 8 * i)
    return add

def tbm_n_sei (op):
    return ".".join(map(str, op))

def mais_um (op):
    oi = []
    for i in op:
        oi.append(int(i, 2))
    return oi

def nome (op):
    oi = []
    index = 0
    for i in range(1,5):
        binario = ""
        for j in range(index*8, index*8+8):
            binario = binario + op[j]
        oi.append(binario)
        index = index + 1
    return oi

rede1 = input("Digite um ip de rede ex: ---.---.---.--- com valores entre 0 e 255: ")
rede2 = input("Digite um ip de rede ex: ---.---.---.--- com valores entre 0 e 255: ")
mascara = int(input("Digite um mascara de rede, sendo um valor entre 1 e 32: "))

arrayrede1 = rede1.split(".")
arrayrede2 = rede2.split(".")

erro = 0
for i in range(4):
    if (not(0 <= int(arrayrede1[i]) <= 255) or (not(0 <= int(arrayrede2[i]) <= 255)) or (not(1 <= mascara <= 32))):
        print(arrayrede1[i], arrayrede2[i])
        erro = 1
        break

if erro == 1:
    print("Valor invalido")
else:
    rede1bin = ""
    for i in arrayrede1:
        binario = bin(int(i))[2:]
        binario = binario.zfill(8)
        rede1bin = rede1bin + binario

    mascarabin = ""
    for i in range(mascara):
        mascarabin = mascarabin + "1"

    for i in range(32 - mascara):
        mascarabin = mascarabin + "0"

    inicio = ""
    for i in range(32):
        if rede1bin[i] == "1" and mascarabin[i] == "1":
            inicio = inicio + "1"
        else:
            inicio = inicio + "0"

    fim = ""
    for i in range(mascara):
        if rede1bin[i] == "1" and mascarabin[i] == "1":
            fim = fim + "1"
        else:
            fim = fim + "0"

    for i in range(32-mascara):
        fim = fim + "1"

    iniciodec = nome(inicio)
        
    fimdec = nome(fim)

    iniini = mais_um(iniciodec)

    fimfim = mais_um(fimdec)

    stringini = tbm_n_sei(iniini)
    stringfim = tbm_n_sei(fimfim)

    addini = nao_sei(stringini)

    addfim = nao_sei(stringfim)

    addrede2 = nao_sei(rede2)

    if addini <= addrede2 <= addfim:
        print("True")
    else:
        print("False")

    print(stringini)
    print(stringfim)
    print(rede2)