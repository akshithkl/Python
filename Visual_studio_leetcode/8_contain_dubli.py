nums = [1, 2, 3, 4, 1]
seen = set()
for num in nums:
    if num in seen:
        print(True)
        break  
    seen.add(num)
else:
   
    print(False)
