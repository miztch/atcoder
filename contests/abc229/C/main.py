# -*- coding: utf-8 -*-
# ABC229C

N, W = map(int, input().split())

Cheeses = [list(map(int, input().split())) for i in range(N)]

Tastiness = [Cheeses[i][0] for i in range(N)]
Amount = [Cheeses[i][1] for i in range(N)]

zip_lists = zip(Tastiness, Amount)
zip_sort = sorted(zip_lists, reverse=True)
Tastiness, Amount = zip(*zip_sort)

max_tastiness, net_amount = 0, 0
for t, a in zip(Tastiness, Amount):
    past_max_tastiness = max_tastiness
    past_net_amount = net_amount

    max_tastiness += t*a
    net_amount += a

    if net_amount > W:
        max_tastiness = past_max_tastiness
        net_amount = past_net_amount
        max_tastiness += t * (W - net_amount)

        break

print(max_tastiness)
