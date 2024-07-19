#seq is a list having some numbers
for i in range(1,len(seq)):
    key = seq[i]
    # invariant : seq [:i] is sorted
    # find the least 'low' such that seq [low] is not less than key.
    low, up =0,i
    while up >low:
        middle = (low+up) // 2
        if seq[middle] < key :
               low = middle + 1
        else:
                   up = middle
                   # insertion key at position low
                   seq[:] = seq[:low] + [key] + seq[low:i]  + seq[i+1:]
