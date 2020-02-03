import os

dirs = os.listdir(".")
print("\n".join(dirs))

print("dirs ^^^")

s = 0
for i in range(10):
    s+=i
print(s)
