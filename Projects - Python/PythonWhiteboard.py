seq = [1,1,2]
print(seq)
#def find_it(seq):
count = 0
index = seq[count]
for index in seq:
    if index in seq:
        count+=1
        print(count)
    count = 0
    if count % 2 != 0:
        print(index)
    index = seq[count+1]
