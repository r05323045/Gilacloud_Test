# crawl_ptt
`crawl_ptt`是為了本次測驗所製作的爬蟲模組，能夠爬取PTT文章資訊，可選擇所需文章的數量
## 使用方式
1.  複製到本地端
    ```
    $git clone https://github.com/r05323045/Gilacloud_Test.git
    $cd Gilacloud_Test
    ```
    輸入下列指令直接執行，會輸出`crawl_data.json`, `crawl_data.txt`, `crawl_content.txt`三個檔案
    ``` 
    $python crawl_ptt.py
    ```
    其中，`crawl_data.txt`內為文章列表，`crawl_content.txt`為文章內容，而`crawl_data.json`使用方式如下
    ```python
    import json
    with open('crawl_data.json', 'r') as f:
        data = json.load(f)
    ```

    *註：預設爬取 `八卦版` 最新 `10` 篇文章(包含公告)

2. 在jupyter notebook環境中，引入該模組
    ```python
    from crawl_ptt import ptt_crawler
    #ptt_crawler('看板名稱').get_data(文章數量)，範例如下
    ptt_crawler（'gossiping'）.get_data(10)
    ```
