
animal = 'wombat'  # global (file) scope

def spam():
    country = "Bulgaria"  # LOCAL variable -- only visible inside spam()
    print(f"animal: {animal}")


spam()

print(f"country: {country}")

# scope search in this order:
# local
# nested (nonlocal)
# global
# builtin

