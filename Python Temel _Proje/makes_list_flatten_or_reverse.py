# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
# Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
# Örnek olarak:
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
##
# output: [1,'a','cat',2,3,'dog',4,5]

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
# Örnek olarak:
# input: [[1, 2], [3, 4], [5, 6, 7]]
##
# output: [[[7, 6, 5], [4, 3], [2, 1]]



def flatten(x):
    if len(x) == 0:
        return x
    if isinstance(x[0], list):
        return flatten(x[0]) + flatten(x[1:])
    return x[:1] + flatten(x[1:])


L1=[]
def revers(y):
    # print(L.reverse())
    for o in reversed(y):
        L1.append(o)
    return L1


input1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
input2=[[1, 2], [3, 4], [5, 6, 7]]

fonc=input("Which fonction do ypu vant to try\nFor flatten enter 1,\nFor return enter 2 : ")
if fonc =='1':
  print( flatten(input1))
elif fonc == '2':
    print(revers(input1))