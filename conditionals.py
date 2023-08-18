is_raining = True
is_cold = False
print("Good morning")

# or, and
if is_raining and is_cold:
    print("Bring umbrella or jacket or both")
elif is_raining and not (is_cold):
    print("Bring umbrella")
elif is_cold and not (is_raining):
    print("Bring jacket")
else:
    print("Shirt is fine")
