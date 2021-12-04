def func(num_egg, cases_array):
    cases_array.sort(reverse=True)
    val = int(num_egg)
    basket = []

    for j in cases_array:
        n_cases = int(val) // j
        val = int(val) % j
        basket.append(n_cases)
    basket.append(val)
    print("Number of Eggs : {}".format(int(num_egg)))
    print(basket) # order: large to small

cases = [12, 24, 36, 48]
sell = [9, 12, 16, 24, 30, 36, 40, 48, 56, 60, 72]

for i in sell:
    func(i, cases)
