a=[13,2,41,5,6,7,34,74,15623,4,236,4]
maxs=0
for i in range (1,len(a)):
    for j in range (i+1, len(a)):
        for k in range (j+1, len(a)):
            if (a[i]+a[j]>a[k]) and (a[i]+a[k]>a[j]) and (a[j]+a[k]>a[i]) and (a[i]>0) and (a[j]>0) and (a[k]>0):
                p = (a[i] + a[j] + a[k]) / 2
                s = (p * (p - a[i]) * (p - a[j]) * (p - a[k])) ** 0.5
                if s>maxs:
                    maxs=s
        i+=1
print(maxs)