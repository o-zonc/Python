while True:
    try:
        x=input("아무것이나 입력해 봅시다.: ")
    except KeyboardInterrupt:
        print('\n\n\n예외발생, 예외발생!!!\n\n\n')
    else:
        print('이것은 무슨 현상??')
        break