leaps=[]
for year in range(1900,1940):
    if (year%4==0 and year%100!=0)or(year%400==0):
        leaps.append(year)
print(leaps)

                #  ( or )

#leaps=[y for y in range(1900,1940)if (y%4==0 and y%100!=0)or(y%400==0)]
#print(leaps)
