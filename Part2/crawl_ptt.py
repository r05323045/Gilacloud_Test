import json
import re
import requests
from bs4 import BeautifulSoup
import time

class ptt_crawler:
    
    def __init__(self, board_name):
        self.board_name = board_name
        self.board_url = 'https://www.ptt.cc/bbs/{board_name}/index.html'.format(board_name = self.board_name)
        #利用上一頁按鈕的連結尋找最新頁面的編號
        self.last_page_url = 'https://www.ptt.cc' + self.get_soup(self.board_url).find(class_ = 'btn-group-paging').find_all('a')[1]['href']
        self.newest_page_num = int(''.join(re.findall("[0-9]", self.last_page_url))) + 1
    
    def get_soup(self, url):
        req = requests.get(
            url = url,
            cookies = {'over18': '1'})
        return BeautifulSoup(req.text, 'html.parser')
    
    def get_page_article(self, url): #爬取該頁所有文章
        article_list = []
        for element in self.get_soup(url).find_all('div', class_ = 'r-ent'):
            article = {'author' : '', 'date': '', 'title' : '', 'url' : '', 'content' : ''}
            article['author'] = element.find('div', class_ = 'meta').find('div', class_ = 'author').text.strip()
            article['date'] = element.find('div', class_ = 'meta').find('div', class_ = 'date').text.strip()
            article['title'] =  element.find('div', class_ = 'title').text.strip()
            if '本文已被刪除' not in article['title'] : #文章被刪除時，有些tag會不存在
                article['url'] = 'https://www.ptt.cc' + element.find('div', class_ = 'title').find('a')['href'].strip()
                article['content'] = self.get_soup(article['url']).find(id = 'main-container') .text
            article_list.append(article)
        return article_list
    
    def get_data(self, num_article): #num_article 爬取文章的數量
        data = {'result': []}
        for page_num in range(self.newest_page_num - num_article//20, self.newest_page_num + 1): #一頁有20篇文章
            url = 'https://www.ptt.cc/bbs/{board_name}/index{page_num}.html'.format(board_name = self.board_name, page_num = page_num)
            data['result'] += self.get_page_article(url)
        data['result'] = data['result'][len(data['result']) - num_article: len(data['result'])]
        return data
    
if __name__ == '__main__':
    board_name = 'gossiping'
    crawler = ptt_crawler(board_name)
    start = time.time()
    data = crawler.get_data(10)
    #輸出JSON檔
    with open('crawl_data.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(data, ensure_ascii=False))
    #輸出文章列表txt檔
    with open('crawl_data.txt', 'w', encoding='utf8') as f:
        f.write('看板名稱 : {} \n'.format(data['result'][0]['url'].split('/')[-2]))
        f.write('|--日期--|--作者--|--標題--|--內文連結--|\n')
        for article in data['result']:
            f.write('{} {} {} {} \n'.format(article['date'], article['author'], article['title'], article['url']))
    #輸出文章內容txt檔
    with open('crawl_content.txt', 'w', encoding='utf8') as f:
        f.write('看板名稱 : {} \n'.format(article['url'].split('/')[-2]))
        for article in data['result']:
            f.write('{} \n'.format(article['content']))
            if '本文已被刪除' in article['title']:
                f.write('{} \n \n'.format(article['title']))
            f.write('===================================文章分隔線===================================\n')
    print('輸出完畢，共花費{time}秒'.format(time = time.time() - start))