# encoding=utf-8

import requests
from bs4 import BeautifulSoup as bs

DOWNLOAD_URL = 'http://lib.cqvip.com/Search/SearchList'
header = {'Connection': 'keep-alive',
          'X-Requested-With': 'XMLHttpRequest',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies_UF = '_qddaz=QD.dvg5o9.qzku28.jtzlxy2x; user_behavior_flag=d27ac7e2-dc23-42f1-8e26-3c78c4ef900f; Hm_lvt_69fff6aaf37627a0e2ac81d849c2d313=1554198939,1554257648; __utmt=1; __utmt_vip2=1; __utma=164835757.1762443098.1554257892.1554257892.1554257892.1; __utmc=164835757; __utmz=164835757.1554257892.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=164835757.1.10.1554257892; Hm_lpvt_69fff6aaf37627a0e2ac81d849c2d313=1554257892; ASP.NET_SessionId=jpspjxk3f2lg04yudf1xzpxo; skybug=c9d1538376cacc113f615e4718350312; search_isEnable=1'
cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookies_UF.split("; ")}
searchParamModel = '''searchParamModel={"ObjectType":1,"SearchKeyList":[],"SearchExpression":null,"BeginYear":null,"EndYear":null,"UpdateTimeType":null,"JournalRange":null,"DomainRange":null,"ClusterFilter":"ZY=21#自动化与计算机技术","ClusterLimit":0,"ClusterUseType":"Article","UrlParam":"A=蔡庆生","Sort":"0","SortField":null,"UserID":"0","PageNum":1,"PageSize":'20',"SType":"","StrIds":"","IsRefOrBy":'0',"ShowRules":"  作者=蔡庆生  ","IsNoteHistory":'0',"AdvShowTitle":null,"ObjectId":null,"ObjectSearchType":'0',"ChineseEnglishExtend":'0',"SynonymExtend":'0',"ShowTotalCount":'0',"AdvTabGuid":""}'''

def main():
    url = DOWNLOAD_URL
    page = requests.post(url, headers=header, cookies=cookie_dict, data=searchParamModel.encode('utf-8'))
    soup = bs(page.content, 'lxml')
    # 获取总页面数
    total_page_num = soup.select_one(".layui-laypage-last").text
    # 获取文章名、期刊名、关键词、作者信息
    paper_list = soup.find_all("dl")
    for i in paper_list:
        paper_title = i.select("a[index]")
        if paper_title:
            paper_title = paper_title[0].text
            author = [j.text for j in i.select("span[class='author'] a")]
            journal = i.select("span[class='from'] a")[0].text
            key_word = [j.text for j in i.select("span[class='subject'] a")]
            print(paper_title, author, journal, key_word)
    # paper_title = paper_list.select("a[index=0]")
    # for i in paper_title:
    #     print(i.text)

    print(total_page_num)
    print(soup)

if __name__ == '__main__':
    main()