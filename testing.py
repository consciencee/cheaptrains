#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest, webtools, finding

class getPriceTesting(unittest.TestCase):
  
  def test_result(self):
    st1=51107
    st2=45807
    #self.assertEqual(getPrice.getPrice('https://www.tutu.ru/rasp.php', st1, st2), 61.5)

    st1=48707
    st2=48807
    #self.assertEqual(getPrice.getPrice('https://www.tutu.ru/rasp.php', st1, st2), 20.5)


class getNodesTesting(unittest.TestCase):
  
  def test_amount_of_nodes(self):
    #getNodes.updateZones()
    st1=58308
    st2=45807
    finding.findCheapestWay(st1, st2)
    #getNodes.getZones('https://www.tutu.ru/rasp.php', st1, st2)
    #nodes = getNodes.getNodes('https://www.tutu.ru/rasp.php', st1, st2)
    #self.assertEqual(len(nodes), 10)

  def test_zero_nodes(self):
    st1=48707
    st2=48807
    #nodes = getNodes.getNodes('https://www.tutu.ru/rasp.php', st1, st2)
    #self.assertEqual(len(nodes), 0)


if __name__ == '__main__':
    unittest.main()

