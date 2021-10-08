weight = float(input("enter your weight :"))
height = float(input("enter your height :"))
BMI = weight / (height ** 2)

if BMI < 16:
    print("Gầy cấp độ III")
elif 16 <= BMI < 17:
    print("Gầy cấp độ II")
elif 17<= BMI < 18.5:
    print("Gầy cấp độ I")
elif 18.5 <= BMI < 25:
    print("Bình thường")
elif 25 <= BMI < 30:
    print("Thừa cân")
elif 30 <= BMI < 35 :
    print("Béo phì cấp độ I")
elif 35 <= BMI < 40:
    print("Béo phì cấp độ II")
elif BMI >= 40:
    print("Béo phì cấp độ III")
print("Chỉ số BMI của bạn là : " + str(BMI))