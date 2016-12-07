# -*- coding:utf-8 -*-

import requests

def get_info_key(response,*agrs,**kwagrs):
  print response.headers["Content-Type"]
  print agrs
  print kwagrs

def main():
  requests.get('http://www.baidu.com',hooks={"response":get_info_key})


if __name__ == "__main__":
  main()
