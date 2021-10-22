a = int(input("Nhập số bắt đầu: "))
b = int(input("Nhập số kết thúc: "))

for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)