def fizz_buzz(n):
    # печатаем числа от 1 до n с правилами Fizz/Buzz
    for i in range(1, n + 1):  # начинаем с 1, до n включительно
        if i % 3 == 0 and i % 5 == 0:  # делится и на 3, и на 5
            print("FizzBuzz")
        else:
            if i % 3 == 0:  # только делится на 3
                print("Fizz")
            else:
                if i % 5 == 0:  # только делится на 5
                    print("Buzz")
                else:  # не делится ни на 3, ни на 5 — печатаем число
                    print(i)


fizz_buzz(15)
