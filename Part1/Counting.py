def count_url(urls):

    files = [url.split('/')[-1] for url in urls]

    files_dic = dict()
    for file_name in files:
        if file_name not in files_dic:
            files_dic[file_name] = 1
        else: 
            files_dic[file_name] += 1
    
    for file_name in sorted(list(files_dic.keys())[:3]):
        print(file_name, files_dic[file_name])
    
if __name__ == '__main__':

    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]
    count_url(urls)

'''解法2 使用Counter套件

    from collections import Counter
    def count_url(urls):

        files = [url.split('/')[-1] for url in urls]

        files_dic = Counter(files)
        for file_name in sorted(list(files_dic.keys())[:3]):
            print(file_name, files_dic[file_name])
        
    if __name__ == '__main__':

        urls = [
            "http://www.google.com/a.txt",
            "http://www.google.com.tw/a.txt",
            "http://www.google.com/download/c.jpg",
            "http://www.google.co.jp/a.txt",
            "http://www.google.com/b.txt",
            "https://facebook.com/movie/b.txt",
            "http://yahoo.com/123/000/c.jpg",
            "http://gliacloud.com/haha.png",
        ]
        count_url(urls)
        
'''