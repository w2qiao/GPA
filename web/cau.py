#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import urllib
import urllib2
import cookielib
import re
import time

class CAU_GPA_Spider:
	#申明相关属性
	def __init__(self):
		self.loginUrl = 'http://urpjw.cau.edu.cn/loginAction.do'
		self.resultUrl = 'http://urpjw.cau.edu.cn/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001'
		self.cookieJar = cookielib.CookieJar()
		
		self.GPA = None
		self.subjects = [] # 储存科目
		self.weights = [] # 储存学分
		self.points = [] # 储存分数
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))

	def cau_init(self, user, password):
		self.postdata = urllib.urlencode({
			'zjh':user,
    		'mm':password
			})
		#初始化链接并获取cookie
		myRequest = urllib2.Request(url = self.loginUrl, data = self.postdata) # 自定义请求
		result = self.opener.open(myRequest) # 访问登录页面，获取必要cookie
		result = self.opener.open(self.resultUrl) # 访问登录成绩页面，获取必要数据
		self.deal_data(result.read())
		# self.print_data(self.subjects)
		# self.print_data(self.weights)
		# self.print_data(self.points)
		self.calculate_data()

	def deal_data(self,myPage):
		myItems = re.findall(r'<tr class="odd" onMouseOut="this\.className=\'even\';" onMouseOver="this\.className=\'evenfocus\';">.*?<td align="center".*?<td align="center".*?<td align="center">\s+(.*?)\s+</td>.*?<td align="center".*?<td align="center".*?>.*?(\d\.\d|\d).*?</td>.*?<td align="center".*?<td align="center".*?>.*?<p.*?>(\d\d\.\d)&nbsp;</P>.*?</td>.*?</tr>',myPage,re.S)
		for item in myItems:
			self.subjects.append(item[0])
			self.weights.append(item[1])
			self.points.append(item[2])

	def print_data(self,items):
		for item in items:
			print item,

	def get_level(self, point):
		point = string.atof(point)
		if point >= 90 and point <= 100:
			return 4.0
		elif point >=85 and point <= 89:
			return 3.7
		elif point >=82 and point <= 84:
			return 3.3
		elif point >=78 and point <= 81:
			return 3.0
		elif point >=75 and point <= 77:
			return 2.7
		elif point >=72 and point <= 74:
			return 2.3
		elif point >=68 and point <= 71:
			return 2.0
		elif point >=64 and point <= 67:
			return 1.5
		elif point >=60 and point <= 63:
			return 1.0
		else:
			return 0

	def calculate_data(self):
		points = 0.0
		weights = 0.0
		for i in range(len(self.points)):
			pattern = re.compile('\d\d\.\d')
			match = pattern.match(self.points[i])
			if match:
				points += self.get_level(self.points[i]) * string.atof(self.weights[i])
				weights += string.atof(self.weights[i])
		if weights != 0:
			self.GPA = points/weights

if __name__ == '__main__':
	start = time.time()
	mySpider = CAU_GPA_Spider()
	mySpider.cau_init('1211250521','19940924')
	end = time.time()
	print 'your GPA:', mySpider.GPA
	print 'run time:', end-start, 's'
