n = eval(input())
wc = input().split(" ")
tc = input().split(" ")
m = eval(input())
wl = []
tl = []
for w in wc:
    wl.append(eval(w))
for t in tc:
    tl.append(eval(t))
# print(wc)
result = 1
rmed = 0
for i in range(len(wl)):
    w = min(wl)
    method = 0
    flag = False
    j = 0
    while j < len(tl):
        # if flag:
        #     j -= 1
        #     flag = False
        if w >= tl[j]:
            method += 1
            # j -= 1
            # flag = True
        j += 1
    # result *= (method - rmed)
    if method > 0:
        tl.remove(min(tl))
        result *= method
        rmed += 1
    wl.remove(w)
print(result % m)
