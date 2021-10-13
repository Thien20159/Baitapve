a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
sum = 0
for i in range(a, b+1):
    sum += i
print(f'Tổng 2 số {a} và {b} = {sum}')