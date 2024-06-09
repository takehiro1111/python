while 1 == 1:
    command = int(input('Select 1 or 2 or 3 (0:Exit)'))
    match command:
        case 1:
            print('1から10')
        case 2:
            print('11から20')
        case 3:
            print('21から30')
        case 0:
            break
        case _:
            print('Invalid Command Try Again')
            continue
    print('Menu Processed Correctly')
