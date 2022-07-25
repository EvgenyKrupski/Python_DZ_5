# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compressor(txt):
    s = ''
    c = 1
    num = []
    val = []
    for i in range(len(txt)):
        if i < len(txt)-1 and txt[i] == txt[i+1]:
            c += 1
        else:
            s += str(c)+txt[i]
            num.append(c)
            val.append(txt[i])
            c = 1
    data = list(zip(num, val))
    print(f'Сжатый текст: {s}')
    return data


def restorator(pack):
    s = ''
    num, val = zip(*pack)
    for i in range(len(pack)):
        s += num[i]*val[i]
    return s


# text = input('Введите текст: ')
text = 'Bbcbbbbbnm mdjhhhhhhhhhhh.diiiiiii dfkdfjjjjjjjjjjljjjm fffff fhjJKKKKKKKsJ. Cxvb777777d7 df123555 555555678'

print(f'Исходный текст: {text}')
package = compressor(text)
unpack = restorator(package)
print(f'Восстановленный текст: {unpack}')