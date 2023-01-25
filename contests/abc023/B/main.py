def append():
    processes.append(prc)


processes = ['b']

N = int(input())
S = input()
n = 1
while n <= 100:
    if S in processes:
        print(n-1)
        break
    elif n == 100:
        print(-1)
    else:
        if n % 3 == 1:
            prc = 'a'+processes[-1]+'c'
            append()
        elif n % 3 == 2:
            prc = 'c'+processes[-1]+'a'
            append()
        else:
            prc = 'b'+processes[-1]+'b'
            append()
    n += 1
