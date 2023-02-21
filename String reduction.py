def StringReduction(str): 
    str = list(str)
    cSet = set(['a','b','c'])
    repeat = True
    while repeat:
      i = 0
      repeat = False
      while i < len(str)-1:
        if str[i] != str[i+1]:
          str[i:i+2] = list(cSet-set([str[i],str[i+1]]))
          repeat = True
        else:
          i += 1
    return len(str)
    
print (StringReduction(input()))
'''
ab->c
bc->a
ca->b
'''
