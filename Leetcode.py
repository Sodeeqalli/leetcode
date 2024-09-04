nums = [1,2,3,4]
newarray = [1] * len(nums)
print(newarray)
for i in range(len(nums)):
    print(nums[i])
    newarray = [ number for number in newarray if newarray.index(number) != i ]

print(newarray)