import time
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import re


# def crawler():
#     rank_1 = 0
#     rank_2 = 0
#     rank_3 = 0
#     player_name = "南極ラーメン"
#     log_url = "https://nodocchi.moe/tenhoulog/#!&name={}".format(player_name)
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#
#     driver = webdriver.Chrome(executable_path="chromedriver.exe")
#     driver.get(log_url)
#     time.sleep(5)
#
#     html = driver.page_source.encode('utf-8')
#     page_data = BeautifulSoup(html, "html.parser")
#
#     score_table = page_data.find("tbody")
#     # score_table = page_data.find(class_="tbl_list")
#     score_datas = score_table.find_all("tr")
#
#     print(score_datas)
#     print(len(score_datas))
#     for data in score_datas:
#         print(data)


def main():
    top_count = 0
    middle_count = 0
    buttom_count = 0
    player_name = "南極ラーメン"
    log_url = "https://nodocchi.moe/tenhoulog/#!&name={}".format(player_name)

    with open("tenhoudata.txt", "rt", encoding="utf-8")as f:
        container = f.readlines()

        for i, data in enumerate(container):
            if not (i + 1) % 3 == 1:
                continue

            if data[0] == "1":
                top_count += 1
            if data[0] == "2":
                middle_count += 1
            if data[0] == "3":
                buttom_count += 1

        # 期待値
        expected_value = ((105 * top_count) - (120 * buttom_count)) // (top_count + middle_count + buttom_count)

        print("【三麻の順位】")
        print("1位 : {}".format(str(top_count)))
        print("2位 : {}".format(str(middle_count)))
        print("3位 : {}".format(str(buttom_count)))
        print("【6段レートでの期待値】")
        if expected_value > 0:
            print("+{}".format(expected_value))
        else:
            print(expected_value)
        time.sleep(10)


if __name__ == '__main__':
    main()