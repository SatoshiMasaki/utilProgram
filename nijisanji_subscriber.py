import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://wikiwiki.jp/nijisanji/' \
          '%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF%E4%B8%80%E8%A6%A7/' \
          '%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB%E7%99%BB%E9%8C%B2%E8%80%85%E6%95%B0'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    sub_table = soup.find("div", class_="h-scrollable")
    sub_table = sub_table.find("tbody")
    trs = sub_table.find_all("tr")
    subscribe_data = []

    for tr in trs:
        liver_name = tr.find("th").get_text()
        sub_date = tr.find_all("td")[1].get_text()
        sub_year = None
        sub_month = None
        sub_day = None

        if sub_date != "-":
            sub_year = int(sub_date[0:2])
            sub_month = int(sub_date[3:5])
            sub_day = int(sub_date[6:8])
        subscribe_data.append((liver_name, sub_year, sub_month, sub_day))

    container = []
    another_container = []
    counter = [0, 0, 0, 0]
    for i in range(4):
        for j, data in enumerate(subscribe_data):
            if data[1] == 18 + i:
                container.append(data)
                counter[i] += 1

    start_index = 0
    for i in range(4):
        change = True
        while change:
            change = False
            for j in range(start_index, start_index + counter[i] - 1):
                if container[j][2] > container[j + 1][2]:
                    container[j], container[j + 1] = container[j + 1], container[j]
                    print("{}と{}を入れ替えました".format(container[j][0], container[j + 1][0]))
                    change = True

        for data in container:
            print(data)

        start_index += counter[i]

    for data in container:
        print(data)
