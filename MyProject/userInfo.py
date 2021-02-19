import xlwt
import xlrd
from selenium import webdriver
from time import sleep


def read_file():
    print('开始执行函数')
    # 读取数据
    book = xlrd.open_workbook('userInfo.xls')
    sheet = book.sheet_by_index(0)  # 打开第一个页面，一个Excel里面可能有多个页面，在左下角那里
    nrows = sheet.nrows  # 行数
    ncols = sheet.ncols  # 列数
    # 写入数据
    workbook = xlwt.Workbook(encoding='utf-8')
    user_info_list = []
    worksheet = workbook.add_sheet('预告数据')  # 在Excel里面创建一个页面
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


def login(bro):
    username_input = bro.find_element_by_xpath('//*[@id="uname"]')
    password_input = bro.find_element_by_xpath('//*[@id="pwd"]')
    username_input.send_keys('s00990')
    password_input.send_keys('Wuzx4836735')
    login_button = bro.find_element_by_xpath('//*[@id="login_button"]')
    login_button.click()
    print('login')


def ini_selenium():
    print('开始执行函数')

    return bro


if __name__ == '__main__':
    user_info_list = read_file()

    bro = webdriver.Chrome(executable_path=r".\chromedriver.exe")
    bro.get('https://oms.smyoa.com/aut-oms/main#sys=OMSSYSROOT&tab=CIFP000001')

    login(bro)

    sleep(5)
    user_frame = bro.find_element_by_xpath('//*[@id="frame_con"]/iframe')
    bro.switch_to.frame(user_frame)
    # 标签定位
    search_input = bro.find_element_by_xpath('//*[@id="query"]/span[3]/input[1]')

    # print(user_info_list[0]['phone'])
    search_input.send_keys(user_info_list[0]['phone'])
    search_button = bro.find_element_by_xpath('//*[@id="btn"]')
    search_button.click()
    sleep(7)
    custNo_input = bro.find_element_by_xpath('//*[@id="custNo"]')
    # print(custNo_input, 'custNo_input')
    # print(custNo_input, 'custNo_input.text')
    print(custNo_input.get_attribute("value"), 'custNo_input.text')
    # bro.quit()
