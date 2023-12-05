actor = "Chris Hemsworth"

#  obj.method()
#  function(obj)

a = actor.upper()
print(actor, a)

# actor = "Matt Damon"

print(actor.startswith('Chris'))
print(actor.endswith('Liam'))

print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))

print(actor.find('worth'))

data = "    spam      "
data = data.strip()
print(data)

print(actor.replace('Chris', 'Liam'))

data = "spam;ham;toast"
fields = data.split(';')
print(fields)

words = "wombat 123 porcupine"
fields = words.split()
print(fields)

