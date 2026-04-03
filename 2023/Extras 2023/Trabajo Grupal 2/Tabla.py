tab1x1 = "a"
tab1x2 = "X"
tab1x3 = "S"
tab1x4 = "X"
print("|", tab1x1, "|", tab1x2, "|", tab1x3, "|", tab1x4, "|")
print("|", tab1x1, "|", tab1x2, "|", tab1x3, "|", tab1x4, "|")
print("|", tab1x1, "|", tab1x2, "|", tab1x3, "|", tab1x4, "|")
print("|", tab1x1, "|", tab1x2, "|", tab1x3, "|", tab1x4, "|")
tab1XA = [tab1x1, tab1x2, tab1x3]
tab1XB = [tab1x2, tab1x3, tab1x4]
if tab1XA == ["X", "X", "X"]:
    print("A")
if tab1XB == ["X", "S", "X"]:
    print("B")
    print(tab1XB)
