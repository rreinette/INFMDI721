def median(lis):
  lis.sort()
  if len(lis)%2==0:
    sum=0
    median_even=0
    for index,i in enumerate(lis):
      if index == len(lis)/2 or index == (len(lis)/2-1):
        sum+=i
    median_even=float(sum)/len(lis)
    return median_even
  elif len(lis)==1:
    return lis[0]
  else:
    for i,val in enumerate(lis):
      if i >= len(lis)/2:
        return val
print(median([2, 1, 6, 0]))