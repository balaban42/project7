import urllib.request


with open('weather.txt', 'r') as f_in:
    line = f_in.readline()

url = urllib.request.urlopen(line)
p_url = url.read()
data = str(p_url)

# Current time
now_time = data.find("time fact__time")
time = data[data.find('>', now_time) + 1:data.find('</time>', now_time)]
lst1 = ['\\', 'xd0', 'xa1', 'xb5', 'xb9', 'x87', 'xb0', 'xd1', 'x81']
for i in lst1:
    time = time.replace(i, ' ')
    time = time.replace('  ', ' ')
time = time.strip()

# Current temperature
now_temp = data.find("temp__value")
temp = data[data.find('>', now_temp) + 1:data.find('<', now_temp)]
lst2 = ['\\', 'xe2', '\\', 'x88', '\\', 'x92']
for i in lst2:
    temp = temp.replace(i, ' ')
    temp = temp.replace('  ', ' ')
temp = temp.strip()
temp = '-' + temp

# Feels like
feels_temp = data.find("term__value")
feels = data[data.find('>', feels_temp) + 45:data.find('</span>', feels_temp)]
for i in lst2:
    feels = feels.replace(i, ' ')
    feels = feels.replace('  ', ' ')
feels = feels.strip()
feels = '-' + feels

# Yesterday at this time
yesterday_temp = data.find("term term_orient_h fact__yesterday")
yesterday = data[data.find('>', yesterday_temp) + 213:data.find('</span>', yesterday_temp)]
for i in lst2:
    yesterday = yesterday.replace(i, ' ')
    yesterday = yesterday.replace('  ', ' ')
yesterday = yesterday.strip()
yesterday = '-' + yesterday

# Sunrise time
sunrise_time = data.find("sunrise-sunset__value")
rise_time = data[data.find('>', sunrise_time) + 1:data.find('</dd>', sunrise_time)]

# Sunset time
sunset_time = data.find("sunrise-sunset__description sunrise-sunset__description_value_sunset")
set_time = data[data.find('>', sunset_time) + 236:data.find('</dd>', sunset_time)]

titles = ['Текущее время', 'Температура сейчас', 'Ощущается как', 'Вчера в это время', 'Восход', 'Закат']
for i in titles:
    print(i, end="  ")
print('\n')
col = '{:>10}{:>16}{:>18}{:>16}{:>14}{:>8}'.format(time, temp, feels, yesterday, rise_time, set_time)
print(col)
