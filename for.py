

exp=[1200,1300,1400,1500,1600]
total=0

for i in range(len(exp)):
    print('Month no. ',i+1,' expense is: ',exp[i])
    total=total+exp[i]

print('Total expense is ',total)