#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest, webtools, finding, dbtools

class webMethodstesting(unittest.TestCase):
  
  def test_result(self):
    st1=51107


class localDbMethodsTesting(unittest.TestCase):

  def test_getBranch(self):
    st = 45807
    self.assertEqual(dbtools.getBranch(st), 'a')

    st = 46607
    self.assertEqual(dbtools.getBranch(st), 'a')

    st = 48707
    self.assertEqual(dbtools.getBranch(st), 'ab')

    st = 51107
    self.assertEqual(dbtools.getBranch(st), 'achj')
  
  def test_getAnyStationFromZone(self):
    zone = '0'
    self.assertEqual(dbtools.getSt(zone), '45807')

    zone = '3'
    self.assertEqual(dbtools.getSt(zone), '46507')

  def test_getConditionalStationFromZone(self):
    zone = '0'
    st = '49307'
    self.assertEqual(dbtools.getSt(zone, st), '45807')

    zone = '5'
    st = '49807'
    self.assertEqual(dbtools.getSt(zone, st), '49307')

    zone = '5'
    st = '48407'
    self.assertEqual(dbtools.getSt(zone, st), '47507')



if __name__ == '__main__':
    unittest.main()

