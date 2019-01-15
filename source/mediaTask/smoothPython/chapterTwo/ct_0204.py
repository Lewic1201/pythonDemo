invoice = """
    0.....6................................40........52...55........
    1909  Pimoroni PiBrella                    $17.50    3    $52.50
    1489  6mm Tactile Switch x20 $4.95 2 $9.90
    1510  Panavise Jr. - PV-201 $28.00 1 $28.00
    1601  PiTFT Mini Kit          k320x240 $34.95 1 $34.95
    """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])
print('-' * 100)

try:
    t = (1, 2, [30, 40])
    print(t)
    # t[2] 被改动了，但是也有异常抛出
    t[2] += [50, 60]
except Exception as err:
    print(err)
    print(t)

print('-' * 100)

from array import array
from random import random

# floats = array('d', (random() for i in range(10 ** 7)))
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()
# floats2 = array('d')
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10 ** 7)
# fp.close()
# print(floats2[-1])
# print(floats2 == floats)
# print('-' * 100)

tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, [30, 40])
# print(hash(tl))
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))
print('-' * 100)

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]
country_code = {country: code for code, country in DIAL_CODES}
country_code2 = {code: country.upper() for country, code in country_code.items() if code < 66}
print(country_code)
print(country_code2)
print('-' * 100)

ss = set('afds')
sd = set('afd341')
print(ss & sd)
print(ss | sd)
print(ss - sd)
print(ss ^ sd)
