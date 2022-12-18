from dominio import Dominio
from tree_search import SearchProblem, SearchTree
import time
from commonMAIS import Map
# 01 ooooooooooooAAoooooooooooooooooooooo 5
# 02 ooooooooooBoAAooBooooooooooooooooooo 21
# 03 ooooCoooooCoAAooCoooooooooBBBooooooo 40
# 04 EBBBooEooFooEAAFooooCCoooDDDoooooooo 1108
# 05 BBBCCoooHIooAAHIooGDDooxGooooooooxoo 713
# 06 EoBBECCCAAoFDDoF 34
# 07 ooooooooooooooDGooooooDGooooBCEHAAooBCEHooooooFIooooooFIooooooFI 3501
# 08 ooooooooooooooEHooooCDEHoooBCDFIAAoBCDFIooooooGJooooooGJoooooooJ 34992
# 09 oooooooooooooDGJoooooDGJoooBCEHKAAoBCEHKoooooFILoooooFILoooooooo 168920
# 10 oooooooooooooooFoooooooFoooBCDEGAAoBCDEGoooooooHoooooooHoooooooo 105350
# 11 ooooooooooooCFILooooCFILoooBDGJMAAoBDGJMooooEHKNooooEHKNoooooooo 208400
with open('levels.txt', 'r') as f:
    levels = f.read().splitlines()

# run all levels and for each level print the solution and time, in the end, print total time
total_time = 0
for level in levels:
    print(level)
    m = Map(level)
    d = Dominio(m)
    p = SearchProblem(d)
    t = SearchTree(p, strategy="depth")
    start = time.time()
    sol = t.search()
    end = time.time()
    total_time += end - start
    print('Solution:', sol)
    print('Time:', end - start)
print('Total time:', total_time)


# EBBBoo
# EooFoo
# EAAFoo
# ooCCoo
# oDDDoo
# oooooo
# ---
# 0  oBBBoo 5
# 6  oooooo 11
# 12 EAAFoo 17
# 18 ECCFoo 23
# 24 EooDDD 29
# 30 oooooo 35

'''
NrSteps= 1                          #printa os separadores (estetico)
s = "---------- Passo: "            #
linhas = " ---------- "             #
print (s + repr(NrSteps) + linhas)  #
for x in m.grid:                     #dá print a cada linha da grid ao inves de numa lista
    print(x)
print(m.car_actions('A'))
# print(m.get_car_orientation('A'))

print("--------------")
#print(m.coordinates)
print(d.actions(m))             #certo
#print(d.satisfies(m))          #certo

while not d.satisfies(m):   #enquanto o carro nao chegar ao fim
    NrSteps = NrSteps+1
    
    print (s + repr(NrSteps) + linhas) #printa os separadores (estetico)
    if(('A', 'd') in d.actions(m) ):
        m.move("A", Coordinates(1,0)) #avança uma posição para a direita
    elif(('B', 's') in d.actions(m) ):
        m.move("B", Coordinates(0,1)) #avança uma posição para a baixo
    
    for x in m.grid: 
        print(x)
    print(d.action(m))             
    print(d.satisfies(m))           
    
#novoS = set()              sudo codigo para o set de todos os carros da grid 
# print(m.grid)
# for x in m.grid: #dá print a cada linha da grid ao inves de numa lista
#     if x != 'o':
#         novoS.add(x)
'''
