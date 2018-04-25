#Ejercicio4
def vocal(a):
    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
        return True
    else:
        return False

print(vocal("z"))
print(vocal("i"))

assert vocal("z") == False
assert  vocal ("i") == True

