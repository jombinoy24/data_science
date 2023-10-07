print("******************************")
print("JOM BINOY")
print("--SJC22MCA-2033--")
print("--20MCA241--DATA SCIENCE LAB--")
print("--BATCH : 2022-2024--")
print("******************************")
def repeat_times(n):
    s = 0
    n_str = str(n)
    while (n > 0):
        n -= sum([int(i) for i in list(n_str)])
        n_str = list(str(n))
        s += 1
    return s

print(repeat_times(9))
print(repeat_times(21))
