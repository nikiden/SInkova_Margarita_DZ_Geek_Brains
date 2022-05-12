
price_list = [57.8, 46.51, 97, 54.25, 41.98, 47.61, 82.82, 71.50,90.10]
for price in price_list:
    print(f'{int(price)} руб. {int(price * 100 / 100):02d} коп.', end=', ')

print('\n',id(price_list))
price_list.sort()
print(price_list)
print('\n', id(price_list))

rev_list = sorted(price_list, reverse=True)
print(rev_list)
print(rev_list[0:6])

