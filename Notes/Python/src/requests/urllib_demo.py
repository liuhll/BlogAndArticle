# -*- coding: utf-8 -*-

import urllib
import urllib2

URL_IP = 'http://192.168.0.160:8001/ip'
URL_GET = 'http://192.168.0.160:8001/get'

def use_simple_urllib2():
  response = urllib2.urlopen(URL_IP)
  print '>>>>Response Headers:'
  print response.info()
  print '>>>>Response Body:'
  print ''.join([line for line in response.readlines()])

def use_params_urllib2():
  params = urllib.urlencode({'param1':'hellp','param2':'world'})
  print '>>>>Request Params:'
  print params

  resp = urllib2.urlopen('?'.join([URL_GET,'%s']) %params)

  print '>>>>Response Headers:'
  print resp.info()
  print '>>>>Status Code:'
  print resp.getcode()
  print '>>>>Response Body:'
  print ''.join([line for line in resp.readlines()])


if __name__ == '__main__':
  print 'Use simple urllib2:'
  use_simple_urllib2()
  print
  print 'Use params urllib2:'
  use_params_urllib2()

