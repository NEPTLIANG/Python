# 九九乘法表
for rows in range(1, 10):
    for cols in range(1, 10):
        if cols <= rows:
            print("{}*{}={}".format(cols, rows, cols * rows), end="\t")
    print("")
