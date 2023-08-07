def past(h, m, s):
    return (h*3600000)+(m*60000)+(s*1000)
#    return (3600*h + 60*m + s) * 1000
print(past(0,1,1))