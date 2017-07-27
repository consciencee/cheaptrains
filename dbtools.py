from lxml import etree, html
import re
import requests

__author__ = 'aliona'


def getSt(zone, branch_node = '45807'):

  tree = etree.parse('data.xml')

  branch = getBranch(branch_node)

  return str(tree.xpath('//zone[@number="'+ zone + '"]/station[contains(branch_tag/text(), "' + branch + '") or contains("' + branch + '", branch_tag/text())][1]/refId/text()'))[2:-2]


def getZone(st):

  tree = etree.parse('data.xml')

  return str(tree.xpath('//station[refId/text()="'+ str(st) +'"]/../@number'))[2:-2]


def getBranch(st):

  tree = etree.parse('data.xml')

  return str(tree.xpath('//station[refId/text()="'+ str(st) +'"]/branch_tag/text()'))[2:-2]


def isSameBranch(station1, station2):

  tree = etree.parse('data.xml')

  branch1 = str(tree.xpath('//station[@name="'+ station1 + '"]/branch_tag/text()'))
  branch2 = str(tree.xpath('//station[@name="'+ station2 + '"]/branch_tag/text()'))

  return (branch1 in branch2) | (branch2 in branch1)


def updateZones():

  response = requests.get('https://www.tutu.ru/10.php', headers={'User-Agent': 'chchjhh'})
  parsed_body = html.fromstring(response.text)

  listNames = []
  listRefs = []

  next_position = 0

  zoneAmount = int(parsed_body.xpath('count(//div[./p[@class="zoneNumber" and text()]])'))


  for i in range(zoneAmount - 1):

    next_position = parsed_body.xpath('count(//div[./p[@class="zoneNumber" and text()="' + str(i+1) + '"]]/preceding-sibling::*)+1')
    zone_position = parsed_body.xpath('count(//div[./p[@class="zoneNumber" and text()="' + str(i) + '"]]/preceding-sibling::*)+1')

    xPatternName = '//div[./p[@class="zoneNumber"] and position() < ' + str(int(next_position)) + ' and position() >= ' + str(int(zone_position)) + ']//a[@class="station-name"]/text()'
    xPatternRef = '//div[./p[@class="zoneNumber"] and position() < ' + str(int(next_position)) + ' and position() >= ' + str(int(zone_position)) + ']//a[@class="station-name"]/@href'

    listNames.append(parsed_body.xpath(xPatternName))
    listRefs.append(parsed_body.xpath(xPatternRef))


  zone_position = parsed_body.xpath('count(//div[./p[@class="zoneNumber" and text()="' + str(zoneAmount - 1) + '"]]/preceding-sibling::*)+1')

  xPatternName = '//div[./p[@class="zoneNumber"] and position() >= ' + str(int(zone_position)) + ']//a[@class="station-name"]/text()'
  xPatternRef = '//div[./p[@class="zoneNumber"] and position() >= ' + str(int(zone_position)) + ']//a[@class="station-name"]/@href'

  listNames.append(parsed_body.xpath(xPatternName))
  listRefs.append(parsed_body.xpath(xPatternRef))


  f = open('data.xml', 'w')
  f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
  f.write('<map>\n')

  for i in range(zoneAmount):
    f.write('<zone number="' + str(i) + '">\n')
    for j in range(len(listNames[i])):
      station_id = re.search(r'[0-9]{5}', listRefs[i][j]).group(0)
      f.write('<station>\n<name>' + listNames[i][j].replace('\t', '').replace('\n', '') + '</name>\n<refId>' + station_id + '</refId>\n</station>\n')

    f.write('</zone>\n')

  f.write('</map>\n')
  f.close()