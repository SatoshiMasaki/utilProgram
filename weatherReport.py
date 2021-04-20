from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
from sound import sound

"""
時間：weatherpoint-data_item_time
気温：weatherpoint-data_item_temp
気圧：weatherpoint-data_item_pressure

weatherpoint-data_item_weather
晴れ：img/weatherpoint/tenki_100.png
曇り：img/weatherpoint/tenki_200.png

weatherpoint-data_item_level
通常：img/weatherpoint/map_kiatu_icon_lv1.png
やや注意：img/weatherpoint/map_kiatu_icon_lv2.png
注意：img/weatherpoint/map_kiatu_icon_lv3.png
警戒：img/weatherpoint/map_kiatu_icon_lv4.png
"""


def getTomorrowWeather():
    """
    夜10時の時報。
    ・夜中の気温
    ・明日の気圧
    ・明日の天気
    ・明日の最高気温と最低気温
    これらを知らせる。
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    pattern_lv1 = re.compile(".*map_kiatu_icon_lv1.png.*")
    pattern_lv2 = re.compile(".*map_kiatu_icon_lv2.png.*")
    pattern_lv3 = re.compile(".*map_kiatu_icon_lv3.png.*")
    pattern_lv4 = re.compile(".*map_kiatu_icon_lv4.png.*")
    pattern_sunny = re.compile(".*tenki_100.png.*")
    pattern_cloudy = re.compile(".*tenki_200.png.*")
    pattern_rainy = re.compile(".*tenki_300.png.*")
    careful_lv1 = 0
    careful_lv2 = 0
    careful_lv3 = 0
    careful_lv4 = 0
    sunny, cloudy, rainy = 0, 0, 0

    url_test = "https://zutool.jp/"
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
    driver.get(url_test)
    time.sleep(5)

    html = driver.page_source.encode('utf-8')
    page_data = BeautifulSoup(html, "html.parser")
    tomorrow_temp = page_data.find(class_="weatherpoint-data_item_tomorrow")
    hour_data = tomorrow_temp.find_all(class_="weatherpoint-data_item")

    # TODO: 気圧の注意警報のラインを再考する。
    for data in hour_data[5:18]:
        container = str(data.find(class_="weatherpoint-data_item_level"))

        if pattern_lv3.match(container):
            careful_lv3 += 1
        elif pattern_lv4.match(container):
            careful_lv4 += 1

    if careful_lv4 >= 4:
        sound(filename="soundFile/strongWind.mp3", playback_time=10)
    elif careful_lv3 >= 4:
        sound(filename="soundFile/wind.mp3", playback_time=10)

    # 天気に関する記述
    for data in hour_data[9:22]:
        container = data.find(class_="weatherpoint-data_item_weather")

        if pattern_rainy.match(str(container)):
            sound(filename="soundFile/rain.mp3", playback_time=10)
            break

    sound()


if __name__ == '__main__':
    getTomorrowWeather()
