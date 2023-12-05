
states = (
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
)

with open("states.txt", "x") as states_out: # "w" opens for writing, "a" for append
    for state in states:
        states_out.write(state + "\n")  # write() does not automatically add newline

# file modes:  r w a x  