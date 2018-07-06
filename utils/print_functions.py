def print_columns(cols, selected):

    for c in range(0, len(cols) - 4, 4):
        for i in range(4):
            if cols[c + i] in selected:
                print('\x1b[1;31m{:30}\x1b[0m'.format(cols[c + i]), end='')
            else:
                print('{:30}'.format(cols[c + i]), end='')
        print()
