def satr_2(a,b):
    return all([char in a.lower() for char in b.lower()])
    #   ### """ESLATMA""" ### bu yerda all xammasiga bitta javob qaytaryapti!
print(satr_2("python","ypth"))
print(satr_2("python", "ypths"))
