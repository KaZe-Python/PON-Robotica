def arithmetich_avarage(x):
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
  m_ar = arithmetich_avarage(x)
  for i in range(0, len(x)):
    s += (x[i] - m_ar) **2
  return (s/(len(x)-1)) ** (1/2)