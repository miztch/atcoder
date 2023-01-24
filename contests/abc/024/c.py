cnfL = []
cnfR = []
livein = []
moveto = []
canmove = []

N, D, K = map(int, input().split())
for i in range(D):
    L, R = map(int, input().split())
    cnfL.append(L)
    cnfR.append(R)
for i in range(K):
    S, T = map(int, input().split())
    livein.append(S)
    moveto.append(T)

for tribe in range(K):
    day = 0
    if livein[tribe] < moveto[tribe]:
        while livein[tribe] < moveto[tribe]:
            if cnfL[day] <= livein[tribe] <= cnfR[day]:
                livein[tribe] = cnfR[day]
            day += 1
        else:
            canmove.append(day)
    else:
        while livein[tribe] > moveto[tribe]:
            if cnfL[day] <= livein[tribe] <= cnfR[day]:
                livein[tribe] = cnfL[day]
            day += 1
        else:
            canmove.append(day)

for result in canmove:
    print(result)
