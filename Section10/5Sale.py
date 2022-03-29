class Sale:
    def __init__(self, amount):
        self.amount = amount


def find_total(sales_list):
    total = 0

    for sale in sales_list:
        print("new sales....")
        print(sale.amount)

        total += sale.amount
    return total


january_sales = [Sale(400), Sale(342), Sale(500)]
print(find_total(january_sales))
