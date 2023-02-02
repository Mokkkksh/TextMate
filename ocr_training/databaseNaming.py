import os

for x in os.listdir('database/Test'):
    print(x)
    count = 0
    if x != ".DS_Store":
        for y in os.listdir('database/Test/'+x):
            count += 1
            dst = f"database/Test/{x}/{x}_{count}.jpg"
            src = f"database/Test/{x}/{y}"
            os.rename(src, dst)