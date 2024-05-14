def main():
    # گرفتن دو آرایه از کاربر
    array1 = input("آرایه اول را وارد کنید (با فاصله جدا کنید): ").split()
    array2 = input("آرایه دوم را وارد کنید (با فاصله جدا کنید): ").split()

    # تبدیل اعضای آرایه‌ها به اعداد صحیح
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]

    while True:
        choice = int(input("لطفاً یکی از اعداد 1، 2، 3 یا 5 را وارد کنید: "))

        if choice == 1:
            result = sum_arrays(array1, array2)
            print("جمع آرایه‌ها:", result)
        elif choice == 2:
            result = multiply_arrays(array1, array2)
            print("ضرب آرایه‌ها:", result)
        elif choice == 3:
            print("آرایه اول:", array1)
            print("آرایه دوم:", array2)
        elif choice == 5:
            break
        else:
            print("ورودی نامعتبر!")

def sum_arrays(array1, array2):
    # تابع برای جمع دو آرایه
    return [x + y for x, y in zip(array1, array2)]

def multiply_arrays(array1, array2):
    # تابع برای ضرب دو آرایه
    return [x * y for x, y in zip(array1, array2)]

if name == "main":
    main()