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


  def test_isSameBranch(self):
    st1 = 45807
    st2 = 46607
    self.assertTrue(dbtools.isSameBranch(st1, st2))

    st1 = 45807
    st2 = 48707
    self.assertTrue(dbtools.isSameBranch(st1, st2))

    st1 = 48707
    st2 = 51107
    self.assertFalse(dbtools.isSameBranch(st1, st2))


  def test_getSt_Any(self):
    zone = '0'
    self.assertEqual(dbtools.getSt(zone), '45807')

    zone = '3'
    self.assertEqual(dbtools.getSt(zone), '46507')


  def test_getSt_Conditional(self):
    zone = '0'
    st = '49307'
    self.assertEqual(dbtools.getSt(zone, st), '45807')

    zone = '5'
    st = '49807'
    self.assertEqual(dbtools.getSt(zone, st), '49307')

    zone = '5'
    st = '48407'
    self.assertEqual(dbtools.getSt(zone, st), '47507')


  def test_getZone(self):
    st = '47507'
    self.assertEqual(dbtools.getZone(st), '5')

    st = '45807'
    self.assertEqual(dbtools.getZone(st), '0')


class systemMethodsTesting(unittest.TestCase):

  def test_findCheapestWay(self):

    finding.findCheapestWay(51107, 45807)


if __name__ == '__main__':
    unittest.main()

