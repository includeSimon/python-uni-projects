'''
Ideea solutiei: voi crea submultimi ale lui v si verific daca sunt sortate, returnand lungimea maxima
Observatii:
    1. Pentru multimea v1 = [5,6,4], submultimile vor fi [5,6], [5,6,4], [6,4]
       Pentru multimea v2 = [1,2,3,4], submultimile vor fi [1,2], [1,2,3], [1,2,3,4], [2,3,4], [3,4]
'''
v = [8, 5, 7, 8, 1, 6, 2]
lungimeMaxima = 1
inceput = 0         #va fi primul element din lista, la care se adauga elemente cate 1 pe rand ca in ex. de mai sus

while inceput < len(v):
    for i in range(len(v) - inceput):
        submultime = v[inceput:inceput + i + 1]     #creez o submultime din ce in ce mai mare
        if submultime == sorted(submultime):        #verific daca este sortata
            if len(submultime) > lungimeMaxima:
                lungimeMaxima = len(submultime)
    inceput += 1
print(lungimeMaxima)