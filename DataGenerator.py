import random
first_name = ["Habib", "Made", "Naufal", "Adit", "Bambang", "Lucy", "Mawar"]
last_name = ["Siregar", "Lail", "Connor", "Majeed", "Schmidt", "Permana","Eka"]
random_name = [f"{random.choice(first_name)} {random.choice(last_name)}" for _ in range(100)]
print(random_name)

amount = [random.randint(1, 10000000) for i in range(100)]
amount_in_rupiah = []
for x in amount:
  y = x*1000
  amount_in_rupiah.append(y)

print(amount_in_rupiah)

set_name = set(random_name)
len(set_name)

order = []
i= 0
for x in random_name:
  i = i + 1
  order.append(i)

print(order)
from datetime import datetime, timedelta

def random_date_time(start, end):
  delta = end - start
  random_sec = random.randint(0, int(delta.total_seconds()))
  return start + timedelta(seconds=random_sec)
start_date = datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime(2025, 12, 31, 23, 59, 59)
random_dt = [random_date_time(start_date,end_date) for x in range(100)]
Random_dt_final = []
for x in random_dt:
  convert_dt = x.strftime("%Y-%m-%d %H:%M:%S")
  Random_dt_final.append(convert_dt)
print(Random_dt_final)

order_id = order
customer_name = random_name
order_date = Random_dt_final
total_amount = amount_in_rupiah
tax_rate = []
for x in total_amount:
  if x >30000000:
    tax_rate.append(0.12)
  else:
    tax_rate.append(0.11)
print(tax_rate)
len(tax_rate)
