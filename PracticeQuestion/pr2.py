marks=[90,77,33,44]
result=list(map(lambda x:"A" if x>90 else "B" if  x>80 else "C" if x>70 else "Fail",marks))
print(result)




