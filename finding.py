#! /usr/bin/python
# -*- coding: utf-8 -*-
import dbtools, webtools

from collections import defaultdict

infinity = 5000

def findCheapestWay(st1, st2):

  nodes = sorted(webtools.getZones('https://www.tutu.ru/rasp.php', st1, st2))

  distances = dict.fromkeys((node for node in nodes), infinity)

  distances[min(dbtools.getZone(st1), dbtools.getZone(st2))] = 0

  path = defaultdict(list)

  for node in nodes:
    path[node] = []

  for i in range(len(nodes) - 1):
    for node in nodes[i+1:]:
      if node != nodes[i]:
        price = webtools.getPrice('https://www.tutu.ru/rasp.php', dbtools.getSt(min(nodes[i], node), dbtools.getSt(max(node, nodes[i]))), dbtools.getSt(max(node, nodes[i])))
        if distances[node] > distances[nodes[i]] + price:
          distances[node] = distances[nodes[i]] + price
          path[node] = path[nodes[i]] + list(nodes[i])
          #path[node].append(nodes[i])

  fullPrice = webtools.getPrice('https://www.tutu.ru/rasp.php', st1, st2)

  print 'Цена билета ', distances[max(dbtools.getZone(st1), dbtools.getZone(st2))]
  print 'Полная цена ', fullPrice
  print 'Экономия ', fullPrice - distances[max(dbtools.getZone(st1), dbtools.getZone(st2))]

  print 'Купить билет необходимо в зонах: ', [node for node in path[max(dbtools.getZone(st1), dbtools.getZone(st2))] if (node != dbtools.getZone(st2)) and (node != dbtools.getZone(st1))]