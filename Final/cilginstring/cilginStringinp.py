from random import randint
from string import ascii_lowercase
from random import choice

print("Dosya Adı: ")
output = input()
out = open(output + ".txt","w")

print("soru sayısı: ")
q = int(input())
print("string uzunluğu min max: ")
minS,maxS = map(int,input().rstrip().split(" "))
print("min, max karıştırma miktarı")
minK,maxK = map(int,input().rstrip().split(" "))
print("min, max alınacak parça uzunluğu: (minP maxP)")
minP,maxP = map(int,input().rstrip().split(" "))

print(q,file=out)
for _ in range(q):
    uzunluk = randint(minS,maxS)
    kelime = ""
    nekadar = randint(minP,maxP)
    print(nekadar,file=out)
    for _ in range(uzunluk):
        kelime += (choice(ascii_lowercase))
    print(uzunluk,file=out)
    karistirma = randint(minK,maxK)
    temp=kelime
    for _ in range(karistirma):
        start = randint(0,uzunluk - nekadar - 1)
        end = start + nekadar
        kelime = kelime[:start] + kelime[end:] + kelime[start:end]
    print(temp,kelime,file=out)
