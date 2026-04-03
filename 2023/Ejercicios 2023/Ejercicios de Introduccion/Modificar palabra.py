palabra1 = "   Uruguay   "
palabra2 = "   Uruguay   "
palabra3 = "   Uru  guay   "
palabra4 = "uRUguay"
palabra5 = "uRUguay"
palabra6 = "uRUguay"
palabra1 = palabra1.lstrip()
print(palabra1, len(palabra1), "con LSTRIP")
palabra2 = palabra2.rstrip()
print(palabra2, len(palabra2), "con RSTRIP")
palabra3 = palabra3.strip()
print(palabra3, len(palabra3), "con STRIP \n")

palabra4 = palabra4.lower()
print(palabra4, len(palabra4), "con LOWER")
palabra5 = palabra5.upper()
print(palabra5, len(palabra5), "con UPPER")
palabra6 = palabra6.capitalize()
print(palabra6, len(palabra6), "con CAPITALIZE")
