a=[2,3,4]
b=[4,5,6]
def intersection(a,b):
    inter=[]
    for ele1 in a:
        for ele2 in b:
            if ele1 == ele2:
                inter.append(ele1)
    return inter
res = intersection(a,b)
print(res)

def only_in_list1(list1,list2):
    ele_list1 = []
    for ele1 in list1:
        found = False
        for ele2 in list2:
            if ele1 == ele2:
                found = True
                break
        if not found:
            ele_list1.append(ele1)
    return ele_list1
list1 = [2,3,4]
list2 = [4,5,6]
res1 = only_in_list1(list2,list1)
print(res1)
"""
def only_in_list2(list1,list2):
    ele_list2 = []
    for ele2 in list2:
        found = False
        for ele1 in list1:
            if ele2 == ele1:
                found = True
                break
        if not found:
            ele_list2.append(ele2)
    return ele_list2
res2 = only_in_list2(list1,list2)
print(res2)
"""








        
