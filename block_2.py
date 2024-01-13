# Module for time sleeping
import time

# [Wires in] dictionary (user)
wires_in = {'red': 'c1',
            'blue': 'c2',
            'black': 'c3',
            'purple': 'c4',
            'yellow': 'c5',
            'green': 'c6'}

# [Wires out] dictionary (user)
wires_out = {'red': 'd1',
             'blue': 'd2',
             'black': 'd3',
             'purple': 'd4',
             'yellow': 'd5',
             'green': 'd6'}

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