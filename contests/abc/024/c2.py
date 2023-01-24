# -*- coding: utf-8 -*-
# abc024c exodus

def main():
    n, d, k = map(int, input().split())

    restrictions = [list(map(int, input().split())) for _ in range(d)]
    tribes = [list(map(int, input().split())) for _ in range(k)]

    for tribe in tribes:

        live, dest = tribe[0], tribe[1]
        stay = live
        day_spent = 0

        for restriction in restrictions:

            restrict_from = restriction[0]
            restrict_to = restriction[1]
            day_spent += 1

            if live < dest:
                if restrict_from <= stay < restrict_to:
                    if dest <= restrict_to:
                        stay = dest
                        break
                    else:
                        stay = restrict_to
            else:
                if restrict_from < stay <= restrict_to:
                    if restrict_from <= dest:
                        stay = dest
                        break
                    else:
                        stay = restrict_from

        print(day_spent)


if __name__ == "__main__":
    main()
