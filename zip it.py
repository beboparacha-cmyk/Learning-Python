numbers = {1, 2, 4, 3, 6, 4}
numbers2 = {7, 8, 9, 10, 11, 12}
S3 = list(zip(numbers, numbers2))
print(S3,"\n")

list1 = [100, 200, 350, 450, 700]
list2 = [150, 250, 300, 400, 750]

for x,y in zip(list1, list2):
    print(x, y)


stocks = ['GOOG', 'AAPL', 'AMZN']
prices = [891.1, 191.1, 1610.1] 

new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)} 
print('\n{}'.format(new_dict)) 