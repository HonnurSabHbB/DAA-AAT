def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    index += 1

    P = [0] * (n + 1)
    for i in range(1, n + 1):
        P[i] = int(data[index])
        index += 1

    X = [0] * (n + 1)
    events = []
    for i in range(1, n + 1):
        X[i] = int(data[index])
        index += 1
        events.append((X[i], (0, i)))

    m = int(data[index])
    index += 1

    y = [0] * (m + 1)
    for i in range(1, m + 1):
        y[i] = int(data[index])
        index += 1

    r = [0] * (m + 1)
    for i in range(1, m + 1):
        r[i] = int(data[index])
        index += 1
        events.append((y[i] - r[i], (-i, 0)))
        events.append((y[i] + r[i], (i, 0)))

    events.sort()
    S = set()
    will_add = {}
    ans = 0

    for event in events:
        if event[1][0] > 0:  # remove
            id = event[1][0]
            S.remove(id)
        elif event[1][0] < 0:  # add
            id = -event[1][0]
            S.add(id)
        else:  # query
            id = event[1][1]
            if len(S) == 0:
                ans += P[id]
            elif len(S) == 1:
                onl = next(iter(S))
                if onl in will_add:
                    will_add[onl] += P[id]
                else:
                    will_add[onl] = P[id]

    max_add = 0
    for key in will_add:
        max_add = max(max_add, will_add[key])

    print(ans + max_add)

if __name__ == "__main__":
    main()
