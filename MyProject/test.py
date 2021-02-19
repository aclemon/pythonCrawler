def asd(a):
    i = 10
    print(i, a)
    return i


def testArr():
    # user_list = [{'phone': 15597108573, 'custNo': ''}, {'phone': 17708491543, 'custNo': ''}]
    # print(user_list)
    # print(user_list[0]['phone'])
    user = {'phone': 17708491543, 'custNo': ''}
    # findInfo = {}
    # user['findInfo'] = findInfo

    print(user[0])


def testDict():
    game_data = {'boats': [], }
    game_data['boats'].append({'name': None})
    print(game_data)


if __name__ == '__main__':
    testArr()
    # testDict()
