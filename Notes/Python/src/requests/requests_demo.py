# -*- coding: utf-8 -*-
import requests

URL_IP = 'http://192.168.0.160:8001/ip'
URL_GET = 'http://192.168.0.160:8001/get'

def use_simple_requests():
  response = requests.get(URL_IP)
  print '>>>>Response Headers:'
  print response.headers
  print '>>>>Response Body:'
  print response.text


def use_params_requests():
  params = {'param1':'hellp','param2':'world'}
  print '>>>>Request Params:'
  print params

  resp = requests.get(URL_GET,params=params)

  print '>>>>Response Headers:'
  print resp.headers
  print '>>>>Status Code:'
  print resp.status_code
  print '>>>>Response Body:'
  print resp.json()


if __name__ == '__main__':
  print 'Use simple urllib2:'
  use_simple_requests()

  print "--------------------------"

  print 'Use params urllib2:'
  use_params_requests()

