for i in range(1, 101):
    if 11 <= i <= 19 or i % 10 == 0:
        print(f'{i} процентов.')
    else:
        n = i % 10
        if 2 <= n < 4:
            print(f'{i} процента.')
        elif n == 1:
            print(f"{i} процент.")
        elif 5 <= n <= 9:
            print(f'{i} процентов.')