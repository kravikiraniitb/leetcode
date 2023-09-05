def threeSum(nums):
    l = len(nums)
    fl =[]
    snums = sorted(nums)
    for x in range(l-2):
        for y in range(x+1,l-1):
            for z in range(y+1, l):
                if snums[x]+snums[y]+snums[z] == 0:
                    if [snums[x], snums[y], snums[z]] not in fl:
                        fl.append([snums[x], snums[y], snums[z]])
    return fl


print(threeSum([-1,0,1,2,-1,-4]))