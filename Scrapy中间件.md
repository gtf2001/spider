# 大规模数据采集的问题

~~~markdown
1. 爬虫一定会遇到异常（有一些请求会挂掉）
	1. 频率过快，当前请求有可能会被挂掉---加大请求的间隔、一直换身份
	2. 服务器的并发量有限
		1. 降低访问频率
		2. 把挂掉的请求重新进行调度，通过响应是否有期望的数据来判断请求是否挂掉
~~~

# Scrapy的中间件

~~~markdown
中间件：解耦合
~~~

~~~markdown
1. 爬虫中间件：爬虫和引擎之间
2. 下载器中间件：下载器和引擎之间
3. 调度器中间件：调度器和引擎之间---内置的，不能动
~~~

## 爬虫中间件

- spider中间件   

![Spider中间件](https://user-images.githubusercontent.com/108125193/197500089-a9f90e98-4b80-4b7f-9ff8-63c180047a3a.png)


- downloader中间件

![Downloader中间件](https://user-images.githubusercontent.com/108125193/197500104-d06d5ec1-ba6c-4677-bd55-7bc7c89bb3a3.png)


### 学会ImagesPipeline

