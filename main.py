import os
import matplotlib.pyplot as plt
import scipy as sc

dirs = os.listdir(".")
print("\n".join(dirs))

print("dirs ^^^")

s = 0
for i in range(10):
    s+=i
print(s)
