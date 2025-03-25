from re import L
class Order:
  def __init__(self, order_id, customer_name, order_date, total_amount):
    self.order_id = order_id
    self.customer_name = customer_name
    self.order_date = order_date
    self.total_amount = total_amount
  def calculate_tax_rate(self):
    if self.total_amount > 30000000:
      return f"The total tax is {self.total_amount * 0.12}"
      print("/"*35)

    else:
      return f"The total tax is {self.total_amount * 0.11}"
      print("/"*35)


  def display_order(self):
    if self.total_amount > 30000000:
      tax_amount = self.total_amount * 0.12
    else:
      tax_amount = self.total_amount * 0.11
    print(f"ID: {self.order_id}")
    print(f"Name: {self.customer_name}")
    print(f"Order Date Time: {self.order_date}")
    print(f"Amount: {self.total_amount}")
    print(f"Tax Amount: {tax_amount}")
    print("-"*35)
class Add_Order:
  def __init__(self,order_id, customer_name, order_date,total_amount):
    self.orders = [Order(order_id, customer_name, order_date,total_amount)
    for order_id, customer_name, order_date,total_amount in zip(order_id, customer_name, order_date,total_amount)]
    self.total_amounts = total_amount
  def display_all_order(self):
    for order in self.orders:
      order.display_order()

  def calculate_total_amount(self):
    print(f"The Total Amount Is {sum(self.total_amounts)}")
    print("="*35)

  def calculate_total_tax(self):
    total_tax =[]
    for i in self.total_amounts:
      if i >30000000:
        total_tax.append(i*0.12)
      else:
        total_tax.append(i*0.11)
    print(f"The Total Tax Is {sum(total_tax)}")
    print("="*35)

  def calculate_total_revenue(self):
    total_rev =[]
    for i in self.total_amounts:
      if i >30000000:
        total_rev.append(i-(i*0.12))
      else:
        total_rev.append(i-(i*0.11))
    print(f"The Total Revenue Is {sum(total_rev)}")
    print("="*35)
  def count_order(self):
    print(f"The Total Order Is {len(self.total_amounts)}")
    print("="*35)
#Adjust Single Order
X = 9
order1 = Order(order_id[X], customer_name[X], order_date[X], total_amount[X])
order1.calculate_tax_rate()
order1.display_order()

Y = 10
order2 = Order(order_id[Y], customer_name[Y], order_date[Y], total_amount[Y])

#Add Multiple orders by modified the variable L & K
L = 65
K = 70
order3 = Add_Order(order_id[L:K], customer_name[L:K], order_date[L:K],total_amount[L:K])
order3.display_all_order()
order3.calculate_total_amount()
order3.calculate_total_tax()
order3.calculate_total_revenue()
order3.count_order()
