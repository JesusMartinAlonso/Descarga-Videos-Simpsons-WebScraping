#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Jesus Martin Alonso
Script que descarga los mas de 400 videos de los simpsons de facebook enlazados desde la página foreverdai.com

Dependencias:
-Python
-Lxml python module  #sudo pip install lxml
-requests python module #sudo pip install requests
-https://github.com/soimort/you-get


#sudo pip install lxml
#sudo pip install requests
#Download and install you-get (https://github.com/soimort/you-get)
#Execute python simpsonsWebScraping-mac.py
'''


from lxml import html
import requests
import os
page = requests.get('http://foreverdai.com/videossimpson')
tree = html.fromstring(page.content)

#Enlaces de los videos
enlaces = tree.xpath('//p[@style="-webkit-font-smoothing: antialiased; outline: none 0px; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); margin: 15px 0px; padding: 0px; border: 0px; font-stretch: inherit; line-height: 21px; vertical-align: baseline; box-sizing: border-box;"]/a/@href')
#Titulos de los videos
titulos = tree.xpath('//p[@style="-webkit-font-smoothing: antialiased; outline: none 0px; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); margin: 15px 0px; padding: 0px; border: 0px; font-stretch: inherit; line-height: 21px; vertical-align: baseline; box-sizing: border-box;"]/a/text()')

#Descarga de videos
for enlace, titulo in zip(enlaces, titulos):
	os.system("you-get" + " -o videosDescargados -O " + (titulo.encode('utf-8')).replace(' ', '_') + ".mp4 " + enlace )