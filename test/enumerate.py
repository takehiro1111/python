prices = [100,200,300]

# for price in prices:
#     print(price * 1.1)

for index,price in enumerate(prices):
    print(f'{index}: {price * 1.1:,.2f}')
