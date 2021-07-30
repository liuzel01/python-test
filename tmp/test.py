

for i in range(1,10):
    for j in range(1,i+1):
        if i*j >= 10:
            print(f"{i} x {j} = {i*j :2d}", end='\t')
        else:
            print(f"{i} x {j} = {i * j :1d}", end='\t')

    print('')