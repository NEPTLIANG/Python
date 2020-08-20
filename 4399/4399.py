def count(n):
    h = hex(n)
    print(h)
    result = 0
    results = []
    for i in range(2, len(h)):
        if h[i] == 'a':
            result += 1
            if h[i+1] != 'a':
                results.append(result)
                result = 0
        # print(h[i])
    results.sort()
    return results[len(results) - 1]


print(count(12412324515234525145245236345345634563456524352345245234234523452452345535452342542545243523452542454352345521421212341234523453245234526734563456345634534524523452345234515))
