import random
random.random()
M = random.randint(0, 5)
N = int(input("Nhập số bất kì từ 0 đến 9: "))
if M==N:
    print("Dự đoán đúng")
else:
    print("Dự đoán sai")
print(M)
