brukeralder = int(input("Skriv inn alderen din: "))

if brukeralder < 12:
    print("80Kr")
elif brukeralder >= 18:
    print("140Kr")
else:
    print("100Kr")

