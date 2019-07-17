import requests
from bs4 import BeautifulSoup

import sys



class spideDlist(object):

    def __init__ (self):
        
        self.url="http://dota.uuu9.com/List_987_{}.shtml"
        #self.url="https://www.baidu.com"

    def geturl(self,url):
        #url=self.url
        response=requests.get(url)

        response.encoding='gb2312'

        response1=response.text

        return response1
    def parseurl(self,inputparse):
        


        soup=BeautifulSoup(inputparse,'lxml')

        bs4html=soup.select('.w680')

        bs4html=bs4html[0]    #继续转成bs4对象待用

        bs4html=bs4html.select('a[target="_blank"]')   #取到以a标签里面带target的bs4对象

        return bs4html
    def append_list(self,inputlist):
        list_title=[]
        list_href=[]

        bs4html=inputlist

        for i in bs4html:
            list_title.append(i.attrs['title'])#遍历返回的列表取里面属性名为title和href的参数加入列表
            list_href.append(i.attrs['href'])
            
    
        return list_title,list_href

    def save_data(self,list1,list2):

        with open("data.txt","a",encoding="utf-8")as f:
            for li1 in list1:
                for li11 in li1:
                    f.write(li11)
                    print("正在写入%s",li11)
                    f.write("\n")

                
            for li2 in list2:
                for li22 in li2:
                    f.write(li22)
                    print("正在写入%s",li22)
                    f.write("\n") 

                
  

    def run(self):
        soup_reslist1=[]
        soup_reslist2=[]
        #soup_reslist=[]
        num=1
        while(num<11):
            start_url=self.url.format(num)#定义URL
            response_html=self.geturl(start_url)#从网站获取数据
            result_html=self.parseurl(response_html)#解析数据
            soup_result1,soup_result2=self.append_list(result_html)#BS4解析数据存到列表
            soup_reslist1.append(soup_result1)
            soup_reslist2.append(soup_result2)
            #soup_reslist.append(soup_result)

            num+=1
        self.save_data(soup_reslist1,soup_reslist2)    
        #return soup_reslist1,soup_reslist2


if __name__ == '__main__':

    spided=spideDlist()
    spided.run()

  
    #dicting=dict(zip(soup1, soup2))   #把两个列表用字典对应
    #for i in dicting.items():
        #print("%s,%s"%(i,dicting[i]))
        #print(i)
        
    #print(dicting)




