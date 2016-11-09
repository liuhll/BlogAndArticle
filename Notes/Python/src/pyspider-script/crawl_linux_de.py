#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-11-09 22:06:30
# Project: linux_cmd

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://man.linuxde.net/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.index_box_bd a').items():
            self.crawl(each.attr.href, callback=self.linux_shell_cmd)

    @config(priority=2)
    def linux_shell_cmd(self, response):
        for each in response.doc('.name a').items():
            self.crawl(each.attr.href,callback=self.linux_shell_cmd_detail)
    
    
    @config(age=10 * 24 * 60 * 60)
    def linux_shell_cmd_detail(self,response):
        result = {
           "title":response.doc('title').text(),
           "url":response.url,
        }
       # get_context(response)
        result['context'] = self._get_context(response)
        
        return result
    
    #$($('h3')[1]).nextAll().not($($('h3')[2]))
    def _get_context(self,resp):
        
        result,items ={},resp.doc('.post h3').items()
        result['brief_intro'] = resp.doc('.post_bd.post > p').text()
        for each_item in items:
            result[each_item.text()] = each_item.next().text()
        return result