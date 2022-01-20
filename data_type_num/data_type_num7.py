import sys
import math

a = 7.21
b = 7.12
c = a - b

print(c) # 0.08999999999999986
print(round(c, 2)) # 0.09
print(c == 0.09) # False

print(abs(c - 0.09) <= 1e-10) # True
print(abs(c - 0.09) <= sys.float_info.epsilon) # True
print(math.isclose(c, 0.09)) # True
