

input_string = "Salutare, ce mai faci?"
vocale = "aeiouAEIOU"

# Varianta 1
def eliminare_vocala(ch):
    return ch not in vocale

print("".join(filter(eliminare_vocala, input_string)))

# Varianta 2
print("".join((filter(lambda x: x not in vocale, input_string))))

# Varianta 3
print("".join([ch for ch in input_string if ch not in vocale]))
