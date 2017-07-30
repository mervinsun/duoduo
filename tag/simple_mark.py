import sys
import re
from utils import *

print('<html><head><title>...</title></head><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub('\*(.+?)\*', '<em>\1<em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')
