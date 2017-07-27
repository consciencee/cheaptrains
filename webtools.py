#! /usr/bin/python
# -*- coding: utf-8 -*-
# coding: utf-8

import requests
from lxml import html
from lxml import etree
import urlparse, re, sys

reload(sys)
sys.setdefaultencoding('utf8')

proxy = {
  'http': '10.10.1.10:3128',
  'https': '10.10.1.10:1080',
}


def getZones(url, stFrom, stTo):

  print 'Receiving zone set...'
  nodes = getNodes(url, stFrom, stTo)

  #dbg
  #nodes = []
  #f = open('bufData', 'r')
  #for line in f:
    #nodes.append(str(line).split(' '))
  #dbg

  tree = etree.parse('data.xml')

  zones = []

  for node in nodes:
    zones.append(str(tree.xpath('//station[name/text()="'+ node[0] +'"]/../@number'))[2:-2])

  return list(set(zones))


def getNodes(url, stFrom, stTo):

  print 'Receiving station set...'

  response = requests.get(getTrackRef(url, stFrom, stTo), headers={'User-Agent': 'jnjjhh'})#, proxies=proxy) 

  parsed_body = html.fromstring(response.text)

  station_names = parsed_body.xpath('//tbody/tr/td[@class="flag"]/a/text()')
  station_refs = parsed_body.xpath('//tbody/*/td[@class="flag"]/a/@href')

  response = requests.get('https://www.tutu.ru/10.php', headers={'User-Agent': 'chchjhh'})
  zones_body = html.fromstring(response.text)

  stations_data = []
  
  for i in range(len(station_refs)):
    station_id = re.search(r'[0-9]{5}', station_refs[i]).group(0)
    if idIsNode(int(station_id), stFrom, stTo):
      stations_data.append((station_names[i], station_id))
  
  #dbg
  f = open('bufData', 'w')
  for data in stations_data:
    f.write(data[0] + ' ' + data[1] + '\n')
  f.close()
  #dbg
  return stations_data


def getTrackRef(url, stFrom, stTo):
  
  print 'Requesting station data...'

  payload = {'st1': stFrom, 'st2': stTo}

  response = requests.get(url, headers={'User-Agent': 'Bjgklu'}, params=payload)#, proxies=proxy)

  parsed_body = html.fromstring(response.text)

  timeLines = parsed_body.xpath('//div[@rel="tooltip"]/a/@href')

  timeLines = [urlparse.urljoin(response.url, url) for url in timeLines]

  return timeLines[0]


def idIsNode(stId, stFrom, stTo):
  return (stId <= max(stFrom, stTo)) & (stId >= min(stFrom, stTo))


def getPrice(url, stFrom, stTo):

  result = ''

  payload = {'st1': stFrom, 'st2': stTo}

  response = requests.get(url, headers={'User-Agent': 'Blu'}, params=payload)#, proxies=proxy)

  parsed_body = html.fromstring(response.text)

  result = parsed_body.xpath('string(//div[@class="e_price"])')

  result = result.replace('\n', '')
  result = result.replace('\t', '')
  result = result.replace(u'\xa0\xa0', ' ')
  result = result.replace(u'\xa0', ' ')

  numericResult = result.replace(' ', '')
  numericResult = re.sub(u'[а-яА-Я]*', '', numericResult)

  print numericResult, stFrom, stTo
  result = "Цена билета " + result

  return float(numericResult)