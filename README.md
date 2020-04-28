# Bollywood_Celebs_Info_Scraper
1. To start a Scrapy project: scrapy startproject postscrape
2. Run the Celeb_Spider.py file by giving appropriate locations.
-->scrapy runspider C:\Users\rohit\PycharmProjects\Bollywood_Celebs\bollywood\bollywood\spiders\celeb_spider.py -o celeb-names.csv
3. The above program will create a CSV file with the names of the celebrities and it also has the links to their images.
4. In the pipelines.py file, create a MongoDB connection and create a collection to store the below data.
5. Now run the Bio_Spider.py by giving the below command in the terminal. (With your path, ofcourse) 
-->scrapy runspider C:\Users\rohit\PycharmProjects\Bollywood_Celebs\bollywood\bollywood\spiders\Bio_Spider.py
6. The above program collects information about celebrities and stores them all in the MongoDB database. Each document in the collection has Full_Name, Image_Link and Biography.
7. If you want the images of celebrities to be downloaded to your local memory, you can run the Images_Download.py just like any other Python file. 
