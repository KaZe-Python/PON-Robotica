def arithmetic_avarage(x):
  s=0
  for i in range(0, len(x)):
    s += x[i]
  return s/len(x)

def weighted_avarage(x, w):
  sum_n = 0
  sum_d = 0
  for i in range(0, len(x)):
    sum_n += x[i] * w[i]
    sum_d += w[i]
  return sum_n/sum_d

def variation_field(x):
  return max(x) - min(x)

def standard_deviation(x):
  s = 0
  m_ar = arithmetic_avarage(x)
  for i in range(0, len(x)):
    s += (x[i] - m_ar) **2
  return (s/(len(x)-1)) ** (1/2)


#Necessaria per definire l'indice di correlazione
def covarianza(x, y):
  s, n = 0, len(x)
  mx = arithmetic_avarage(x)
  my = arithmetic_avarage(y)
  for i in range(0, n):
    s += (x[i]-mx)*(y[i]-my)
  return s/(n-1)

def correlation_index(x,y):
  return covarianza(x,y) / (standard_deviation(x)*standard_deviation(y))

def slope(x,y):
  return covarianza(x,y) / standard_deviation(x)**2

def line(x_p, y_p, m, x):
  return (y_p + m*(x-x_p))
