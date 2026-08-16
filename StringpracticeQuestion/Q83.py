'''83 Create a string from a byte array. Byte[] = {72, 101, 108} (ASCII for H, e, l) "Hel"'''

Byte=[72,101,108]
result=""
for x in Byte:
    result+=chr(x)
print("Ascii for ",result)