# -*- coding:utf-8 -*-

import requests

URL = "http://api.github.com"

def construct_url(end_point):
    return '/'.join([URL,end_point])

def basic_auth():
    resp = requests.get(construct_url('user'),auth=('liuhll','*****'))
    print resp.text
    print resp.request.headers


def basic_oauth():
    ''' 通过oauth认证，该方法相当于auth2.0认证当中的第二步
    完整的oauth2.0认证需要两次请求才能完成，第一次请求发送 client_id 和scope (appid和需要获取用户资源的范围)
    服务端返回给客户端access_token，App再次发起请求，根据该access_token获取用户授权的可以访问的资源
    '''
    headers = {'Authorization':'token 6644b5dea4b61135e14f381af74483a4f3191b66'}
    resp = requests.get(construct_url('user/emails'),headers=headers)

    print resp.text
    print resp.request.headers
    print resp.status_code

def oauth_advanced():
    auth = GithubAuth('6644b5dea4b61135e14f381af74483a4f3191b66')
    resp = requests.get(construct_url('user/emails'),auth=auth)
    print resp.text
    print resp.request.headers
    print resp.status_code


from requests.auth import AuthBase

class GithubAuth(AuthBase):
    def __init__(self,token):
        self.token = token


    def __call__(self,req):
        req.headers["Authorization"] = " ".join(['token',self.token])
        return req        
     

if __name__ == "__main__":
    #调用基本认证：Basic  authentication
    # basic_auth()
    #通过 access_token来获取我的邮件
    #basic_oauth()
    oauth_advanced()      
            
