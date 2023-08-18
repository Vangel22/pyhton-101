sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]

new_day_w2 = input("Enter amount in $ for lemonade sold: ")

sales_w2.append(int(new_day_w2))

sales = []

sales.extend(sales_w1)
sales.extend(sales_w2)
# sales = sales_w1 + sales_w2

# sales.sort()  # this step will be skipped with min max but its not more efficient
best_day = max(sales) * 1.5  # [-1]
worst_day = min(sales) * 1.5  # [0]

sales_w1.sort()
sales_w2.sort()


best_day_w1 = sales_w1[-1]
worst_day_w1 = sales_w1[0]
best_day_w2 = sales_w2[-1]
worst_day_w2 = sales_w2[0]


print(f'Best day of week 1 earned ${best_day_w1}, and worst ${worst_day_w1}')
print(f'Best day of week 2 earned ${best_day_w2}, and worst ${worst_day_w2}')


print(
    f'Total best day earnings are ${best_day}, and worst day earnings are ${worst_day}')
