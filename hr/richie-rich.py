#!/bin/python
import sys



def rechieRich(nums, n, k ):
    i = 0
    j = n-1
    df = 0
    result = ['' for ii in range(n)]
    while i < j:
        if nums[i] != nums[j]: df += 1
        i += 1
        j -= 1

    extra = k - df
    if k < df:
        return None
    else:
        i = 0
        j = n-1
        while i <= j:
            if nums[i] != nums[j]:
                if nums[i] != '9' and nums[j] != '9' and extra >= 1:
                    result[i] = '9'
                    result[j] = '9'
                    extra -= 1
                else:
                    bigger = max(nums[i], nums[j])
                    result[i] = bigger
                    result[j] = bigger
            else:
                if nums[i] != '9' and extra >= 2:
                    result[i] = '9'
                    result[j] = '9'
                    extra -= 2
                else:
                    result[i] = nums[i]
                    result[j] = nums[j]
            if i == j:
                result[i] = '9' if extra > 0 else nums[i]
            i += 1
            j -= 1
        return "".join(result)

def hr():
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    number = raw_input().strip()

    r = rechieRich(number, n, k)
    if r is not None:
        print r
    else:
        print -1

case1 = "128392759430124"
print case1
print  rechieRich(case1,len(case1),8)

case2 = "123"
print case2
print rechieRich(case2,len(case2),2)

case3 = "11119111"
print case3
print rechieRich(case3,len(case3),4)

case4 = "3943"
print case4
print rechieRich(case4,len(case4),1)

case5 = "111149111"
print case5
print rechieRich(case5,len(case5),4)



