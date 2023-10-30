# 課題　関数をつかいこなそう

def get_tax( price, rate=0.1 ):

  tax = price * rate
  total = price + tax

  return total,tax

price =100

pri, tax = get_tax(price)
print(pri)
