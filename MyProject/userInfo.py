from time import sleep

import xlrd
import xlwt
from selenium import webdriver


def read_file():
    print('开始执行函数')
    # 读取数据
    book = xlrd.open_workbook('userInfo.xls')
    sheet = book.sheet_by_index(0)  # 打开第一个页面，一个Excel里面可能有多个页面，在左下角那里
    nrows = sheet.nrows  # 行数
    ncols = sheet.ncols  # 列数
    user_info_list = []
    for j in range(1, int(nrows)):
        user_info = {'phone': int(sheet.row_values(j)[0]), 'custNo': str(sheet.row_values(j)[1])}
        user_info_list.append(user_info)
        # print(j,  sheet.row_values(j))
        # for i in range(ncols):
    print(user_info_list)
    return user_info_list

    #     #     if i == 1 and j != 0:
    #     worksheet.write(j, i, random.randrange(0, 9))
    #     else:
    #         worksheet.write(j, i, sheet.row_values(j)[i])
    # workbook.save('file2.xlsx')  # 生成文件


def saveFile(user_info_list):
    # 写入数据
    workbook = xlwt.Workbook(encoding='utf-8')
    # 在Excel里面创建一个页面
    worksheet = workbook.add_sheet('查询数据')
    worksheet.write(0, 0, '手机号')
    worksheet.write(0, 1, '客户号')
    worksheet.write(0, 2, '查询信息')
    for index, user_info in enumerate(user_info_list):
        saveRow = index + 1
        worksheet.write(saveRow, 0, user_info['phone'])
        worksheet.write(saveRow, 1, user_info['custNo'])
        worksheet.write(saveRow, 2, str(user_info['findInfo_list']))
    workbook.save('file.xlsx')  # 生成文件


def login(bro):
    username_input = bro.find_element_by_xpath('//*[@id="uname"]')
    password_input = bro.find_element_by_xpath('//*[@id="pwd"]')
    username_input.send_keys('s00990')
    password_input.send_keys('Wuzx4836735')
    login_button = bro.find_element_by_xpath('//*[@id="login_button"]')
    login_button.click()
    print('login')


def searchInfo(bro, user_info):
    # bro.get
    return user_info


def ini_selenium():
    print('开始执行函数')

    return bro


if __name__ == '__main__':
    user_info_list = read_file()

    bro = webdriver.Chrome(executable_path=r".\chromedriver.exe")
    bro.get('https://oms.smyoa.com/aut-oms/main#sys=OMSSYSROOT&tab=CIFP000001')

    login(bro)
    sleep(2)
    user_frame = bro.find_element_by_xpath('//*[@id="frame_con"]/iframe')
    bro.switch_to.frame(user_frame)

    # 标签定位
    search_input = bro.find_element_by_xpath('//*[@id="query"]/span[3]/input[1]')

    for index, user_info in enumerate(user_info_list):
        # print(user_info_list[0]['phone'])
        search_input.clear()
        search_input.send_keys(user_info['phone'])
        search_button = bro.find_element_by_xpath('//*[@id="btn"]')
        search_button.click()
        custNo_input = bro.find_element_by_xpath('//*[@id="custNo"]')
        # 加载
        sleep(2)
        user_info['custNo'] = custNo_input.get_attribute("value")
        print(user_info, 'user_info')
        user_info_list[index] = user_info

    # 跳出
    bro.switch_to.default_content()
    bro.find_element_by_xpath('//*[@id="tree_OMSSYSROOT"]/div/div/ul/li[10]/a').click()
    sleep(1)
    bro.find_element_by_xpath('//*[@id="tree_OMSSYSROOT"]/div/div/ul/li[10]/ul/li[4]/a').click()
    sleep(1)
    bro.find_element_by_xpath('//*[@id="tree_OMSSYSROOT"]/div/div/ul/li[10]/ul/li[4]/ul/li[7]/a').click()
    sleep(1)
    validateFrame = bro.find_element_by_xpath('//*[@id="frame_con"]/iframe[2]')
    bro.switch_to.frame(validateFrame)

    # 标签定位
    search_input = bro.find_element_by_xpath('//*[@id="custNo"]')
    search_button = bro.find_element_by_xpath('//*[@id="searchBtn"]')

    for index, user_info in enumerate(user_info_list):
        findInfo = {}
        findInfo_list = []
        # print(user_info_list[0]['phone'])
        search_input.clear()
        search_input.send_keys(user_info['custNo'])
        search_button.click()
        # 加载
        sleep(2)
        try:
            # 存在时
            bank_info = bro.find_element_by_xpath('//*[@id="cardValidateResultTable"]/tbody/tr/td[9]')
            channel_info = bro.find_element_by_xpath('//*[@id="cardValidateResultTable"]/tbody/tr/td[10]')
        except:
            print("NoSuchElementException")
        else:
            findInfo['bank_info'] = bank_info.text
            findInfo['channel_info'] = channel_info.text

        findInfo_list.append(findInfo)
        user_info['findInfo_list'] = findInfo_list
        print(user_info, 'user_info')
        user_info_list[index] = user_info

    saveFile(user_info_list)

    print(user_info_list)

    bro.quit()
