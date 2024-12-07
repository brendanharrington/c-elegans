import graph_tool.all as gt

def run_loop(g):
    while True:
        print('\n========= OPTIONS =========')
        print('[0]: Print graph')
        print('[1]: Print blockmodel graph')
        print('[q]: Quit')
        
        choice = input('\nEnter the number of what you\'d like to do: ')

        match choice:
            case '0':
                gt.graph_draw(g)
            case '1':
                state = gt.minimize_blockmodel_dl(g)
                state.draw()
            case 'q':
                print('\nQuitting...')
                break
            case _:
                print('\nInvalid entry, try again.')

def print_statistics():
    print('statistics')

