# pip install pyaztro
from pyaztro import Aztro
# Огненные знаки: Aries, Leo, Sagittarius / Овен, Лев, Стрелец.
# Знаки Земли: Taurus, Virgo, Capricorn / Телец, Дева, Козерог.
# Воздушные знаки: Gemini, Libra, Aquarius / Близнецы, Весы, Водолей.
# Водные знаки: Cancer, Scorpio, Pisces / Рак, Скорпион и Рыбы.

horoscope = Aztro('Sagittarius', day = 'today')

print(horoscope.sign)
print(horoscope.mood)
print(horoscope.color)
print(horoscope.compatibility)
print(horoscope.lucky_number)
print(horoscope.lucky_time)
print(horoscope.date_range)
print(horoscope.description)
