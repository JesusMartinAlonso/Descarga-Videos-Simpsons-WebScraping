#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Script que descarga los mas de 400 videos de los simpsons de facebook enlazados desde la página foreverdai
#https://github.com/soimort/you-get
'''
Author: Jesus Martin Alonso

Dependecias:
-Python
-lxml
-requests
-you-get

Pasos para ejecucion manual:
1.- Descargar e instalar Python 3.4 (https://www.python.org/ftp/python/3.4.4/python-3.4.4rc1.msi)
2.- Instalar lxml (C:\Python34\python.exe -m pip install lxml-3.4.4-cp34-none-win32.whl)
3.- Instalar requests (C:\Python34\python.exe -m pip install requests) 
4.- Ejecutar script para descargar videos (C:\Python34\python.exe simpsonsWebScrapping-windows.py)
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

#Descarga de los videos
for enlace, titulo in zip(enlaces, titulos):
	nuevo_titulo = bytes(titulo.replace(' ', '_'), 'utf-8')
	os.system("you-get" + " -o videosDescargados  -O " + nuevo_titulo.decode('utf-8') + ".mp4 " + enlace )
