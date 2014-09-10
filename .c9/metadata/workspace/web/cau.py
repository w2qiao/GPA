{"filter":false,"title":"cau.py","tooltip":"/web/cau.py","undoManager":{"mark":33,"position":33,"stack":[[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":0,"column":22}},"text":"#!/usr/bin/env python3"},{"action":"insertText","range":{"start":{"row":0,"column":22},"end":{"row":1,"column":0}},"text":"\n"},{"action":"insertLines","range":{"start":{"row":1,"column":0},"end":{"row":90,"column":0}},"lines":["# -*- coding: utf-8 -*-","import string","import urllib","import urllib2","import cookielib","import re","import time","","class CAU_GPA_Spider:","\t#申明相关属性","\tdef __init__(self):","\t\tself.loginUrl = 'http://urpjw.cau.edu.cn/loginAction.do'","\t\tself.resultUrl = 'http://urpjw.cau.edu.cn/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001'","\t\tself.cookieJar = cookielib.CookieJar()","\t\t","\t\tself.GPA = None","\t\tself.subjects = [] # 储存科目","\t\tself.weights = [] # 储存学分","\t\tself.points = [] # 储存分数","\t\tself.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))","","\tdef cau_init(self, user, password):","\t\tself.postdata = urllib.urlencode({","\t\t\t'zjh':user,","    \t\t'mm':password","\t\t\t})","\t\t#初始化链接并获取cookie","\t\tmyRequest = urllib2.Request(url = self.loginUrl, data = self.postdata) # 自定义请求","\t\tresult = self.opener.open(myRequest) # 访问登录页面，获取必要cookie","\t\tresult = self.opener.open(self.resultUrl) # 访问登录成绩页面，获取必要数据","\t\tself.deal_data(result.read())","\t\t# self.print_data(self.subjects)","\t\t# self.print_data(self.weights)","\t\t# self.print_data(self.points)","\t\tself.calculate_data()","","\tdef deal_data(self,myPage):","\t\tmyItems = re.findall(r'<tr class=\"odd\" onMouseOut=\"this\\.className=\\'even\\';\" onMouseOver=\"this\\.className=\\'evenfocus\\';\">.*?<td align=\"center\".*?<td align=\"center\".*?<td align=\"center\">\\s+(.*?)\\s+</td>.*?<td align=\"center\".*?<td align=\"center\".*?>.*?(\\d\\.\\d|\\d).*?</td>.*?<td align=\"center\".*?<td align=\"center\".*?>.*?<p.*?>(\\d\\d\\.\\d)&nbsp;</P>.*?</td>.*?</tr>',myPage,re.S)","\t\tfor item in myItems:","\t\t\tself.subjects.append(item[0])","\t\t\tself.weights.append(item[1])","\t\t\tself.points.append(item[2])","","\tdef print_data(self,items):","\t\tfor item in items:","\t\t\tprint item,","","\tdef get_level(self, point):","\t\tpoint = string.atof(point)","\t\tif point >= 90 and point <= 100:","\t\t\treturn 4.0","\t\telif point >=85 and point <= 89:","\t\t\treturn 3.7","\t\telif point >=82 and point <= 84:","\t\t\treturn 3.3","\t\telif point >=78 and point <= 81:","\t\t\treturn 3.0","\t\telif point >=75 and point <= 77:","\t\t\treturn 2.7","\t\telif point >=72 and point <= 74:","\t\t\treturn 2.3","\t\telif point >=68 and point <= 71:","\t\t\treturn 2.0","\t\telif point >=64 and point <= 67:","\t\t\treturn 1.5","\t\telif point >=60 and point <= 63:","\t\t\treturn 1.0","\t\telse:","\t\t\treturn 0","","\tdef calculate_data(self):","\t\tpoints = 0.0","\t\tweights = 0.0","\t\tfor i in range(len(self.points)):","\t\t\tpattern = re.compile('\\d\\d\\.\\d')","\t\t\tmatch = pattern.match(self.points[i])","\t\t\tif match:","\t\t\t\tpoints += self.get_level(self.points[i]) * string.atof(self.weights[i])","\t\t\t\tweights += string.atof(self.weights[i])","\t\tif weights != 0:","\t\t\tself.GPA = points/weights","","if __name__ == '__main__':","\tstart = time.time()","\tmySpider = CAU_GPA_Spider()","\tmySpider.cau_init()","\tend = time.time()","\tprint 'your GPA:', mySpider.GPA","\tprint 'run time:', end-start, 's'"]}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":19},"end":{"row":86,"column":20}},"text":"'"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":20},"end":{"row":86,"column":21}},"text":"'"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":20},"end":{"row":86,"column":21}},"text":"1"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":21},"end":{"row":86,"column":22}},"text":"2"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":22},"end":{"row":86,"column":23}},"text":"1"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":23},"end":{"row":86,"column":24}},"text":"1"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":24},"end":{"row":86,"column":25}},"text":"2"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":25},"end":{"row":86,"column":26}},"text":"2"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":26},"end":{"row":86,"column":27}},"text":"0"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":86,"column":26},"end":{"row":86,"column":27}},"text":"0"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":26},"end":{"row":86,"column":27}},"text":"2"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":27},"end":{"row":86,"column":28}},"text":"0"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":86,"column":27},"end":{"row":86,"column":28}},"text":"0"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":86,"column":26},"end":{"row":86,"column":27}},"text":"2"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":26},"end":{"row":86,"column":27}},"text":"5"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":27},"end":{"row":86,"column":28}},"text":"0"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":28},"end":{"row":86,"column":29}},"text":"5"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":29},"end":{"row":86,"column":30}},"text":"2"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":30},"end":{"row":86,"column":31}},"text":"1"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":32},"end":{"row":86,"column":33}},"text":","}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":33},"end":{"row":86,"column":34}},"text":"'"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":34},"end":{"row":86,"column":35}},"text":"'"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":34},"end":{"row":86,"column":35}},"text":"1"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":35},"end":{"row":86,"column":36}},"text":"9"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":36},"end":{"row":86,"column":37}},"text":"9"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":37},"end":{"row":86,"column":38}},"text":"4"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":38},"end":{"row":86,"column":39}},"text":"0"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":39},"end":{"row":86,"column":40}},"text":"9"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":40},"end":{"row":86,"column":41}},"text":"2"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":41},"end":{"row":86,"column":42}},"text":"4"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":86,"column":25},"end":{"row":86,"column":26}},"text":"\\"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":86,"column":25},"end":{"row":86,"column":26}},"text":"\\"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":86,"column":24},"end":{"row":86,"column":25}},"text":"2"}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":86,"column":24},"end":{"row":86,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1410353491785,"hash":"f642ded718fb1b9a4cb0dfa5ac4c2cde51535346"}