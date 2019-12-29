#!/usr/bin/env python
# coding: utf-8

# # アカウント登録し、API KEYを取得してください
# https://openweathermap.org/

# In[ ]:


import pandas as pd
import requests

def get_weather_api():
    df = pd.read_json("../credentials.json")
    weather_api = df["weather"]["api_key"]
    return weather_api


# In[ ]:


def get_weather():
    city_name = "Tokyo"
    API_KEY = get_weather_api()

    url = f'http://api.openweathermap.org/data/2.5/weather?units=metric&q={city_name}&APPID={API_KEY}'
    response = requests.get(url)
    data = response.json()
    weather = {}
    weather['天気'] = data["weather"][0]["icon"]
    weather['気温'] = f'{data["main"]["temp"]}度'
    weather['最低気温'] = f'{data["main"]["temp_min"]}度'
    weather['最高気温'] = f'{data["main"]["temp_max"]}度'

    if weather['天気'] == '01n' or weather['天気'] == '01d':
        weather['天気'] = '快晴'
    elif weather['天気'] == '02n' or weather['天気'] == '02d':
        weather['天気'] = '晴れ'
    elif weather['天気'] == '03n' or weather['天気'] == '03d':
        weather['天気'] = '曇り'
    elif weather['天気'] == '04n' or weather['天気'] == '04d':
        weather['天気'] = '曇り'
    elif weather['天気'] == '09n' or weather['天気'] == '09d':
        weather['天気'] = '小雨'
    elif weather['天気'] == '10n' or weather['天気'] == '10d':
        weather['天気'] = '雨'
    elif weather['天気'] == '11n' or weather['天気'] == '11d':
        weather['天気'] = '雷雨'
    elif weather['天気'] == '13n' or weather['天気'] == '13d':
        weather['天気'] = '雪'
    elif weather['天気'] == '50n' or weather['天気']['天気'] == '50d':
        weather['天気'] = '霧'

    return f'天気: {weather["天気"]}\n気温: {weather["気温"]}\n最低気温: {weather["最低気温"]}\n最高気温: {weather["最高気温"]}'


# In[ ]:




