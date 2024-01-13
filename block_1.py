# Module for time sleeping
import time

# [Wires in] dictionary (user)
wires_in = {'red': 'a1',
            'blue': 'a2',
            'black': 'a3',
            'purple': 'a4',
            'yellow': 'a5',
            'green': 'a6'}

# [Wires out] dictionary (user)
wires_out = {'red': 'b1',
             'blue': 'b2',
             'black': 'b3',
             'purple': 'b4',
             'yellow': 'b5',
             'green': 'b6'}

# Wires list (default)
list_wires = ['red', 'blue', 'black', 'purple', 'yellow', 'green']

# Iteration function (sorts through the items in the list above)
for i in list_wires:

    # Condition: if an item is in list, print it
    if i in wires_out:
        print(f'Analyzing {i} wire...')
        time.sleep(3)
        print(f'Comes in of connector {wires_in[i]}')
        time.sleep(2)
        print(f'Comes out of connector {wires_out[i]}')
        time.sleep(2)

print(f'The wire road starts in block A and ends in block B. \nTotal length: 50 m.')