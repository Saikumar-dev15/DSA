# 0(n) 
def get_squared_numbers(numbers):
    squared_numbers = []
    for i in numbers:
        squared_numbers.append(i*i)
    return squared_numbers

numbers = [2, 5, 8, 9]
results = get_squared_numbers(numbers)
print(results)


#0(1)
def find_first_pe(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe

prices = [12, 8, 9 , 10]
index = 2
eps = [2, 4, 6, 8]
result = find_first_pe(prices,eps, index )
print(result)
