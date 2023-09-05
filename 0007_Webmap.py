# 0007 - Webmap. In this one, you put an address you want and it opens your browser and it googles it for you.

import webbrowser
import sys

if len(sys.argv) > 1:
    endereco = ' '.join(sys.argv[1:])
webbrowser.open('https://www.google.com/maps/place/'+endereco)
