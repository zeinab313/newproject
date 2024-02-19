from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
import psycopg2

from selenium import webdriver
from ...models import Post
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

from jdatetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .views import NewsViewset


def connection_to_database():
    '''برقراری ارتباط'''
    conn = psycopg2.connect(database="crawlnews", user='postgres',
                            password='z13681368', host='127.0.0.1', port='5432')
    conn.autocommit = True
    # اتصال به پایگاه داده postgress
    return conn


class CrawlViewset(viewsets.ViewSet):
    # تعریف متغیرهای ثابت
    publisher = "crawler@gmail.com"
    author = "crawler"
    supervisor_to_confirm = "crawler@gmail.com"
    type_of_news = "crawl"
    
    # def get_object(self, queryset=None):
    #     folder_name = self.request.user
    #     return folder_name

    def isnacrawl(self, i, wait, folder_name):
        title = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='search_results_wrapper']/div["+str(i)+"]/div[1]/div[2]/div[1]/h2/a"))).text
        news = Post.objects.filter(title=title).first()
        if not (news):
            Driver = webdriver.Chrome()
            # باز کردن پایگاه خبری
            Driver.get("https://www.isna.ir/")
            wait1 = WebDriverWait(Driver, 3)
            # #جستجوی عنوان خبر دریافت شده
            search = wait1.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/header[1]/div[1]/div/div[2]/div/div[2]/div/div/form/input")))
            search.send_keys(title)
            search.send_keys(Keys.ENTER)
            for j in range(1, 10, 1):
                pathtitle = '//*[@id="search"]/section[2]/div/ul/li[' + \
                    str(j)+']/div/h3'
                # جستجوی عنوان خبر و چک کردن عنوان به دست امده با عنوان قبلی
                titlenews = wait1.until(
                    EC.presence_of_element_located((By.XPATH, pathtitle))).text
                if titlenews[0:15] == title[0:15]:
                    # استخراج چکیده خبر
                    snippet = wait1.until(EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='search']/section[2]/div/ul/li["+str(j)+"]/div/p[1]"))).text
                    press_link = wait1.until(EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='search']/section[2]/div/ul/li["+str(j)+"]/div/h3/a"))).get_attribute('href')
                    Drivers = webdriver.Chrome()
                    Drivers.get(press_link)
                    wait3 = WebDriverWait(Drivers, 3)
                    # استخراج عکس و محتوای خبر
                    image_url = wait3.until(EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='item']/div[2]/div[1]/div[1]/figure/img"))).get_attribute('src')
                    content = wait3.until(EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='item']/div[2]/div[1]/div[1]/div"))).text
                    # استخراج ادرس خبر
                    # url = Drivers.current_url
                    source_website = "ایسنا"
                    published_date = datetime.now()
                    # اتصال به پایگاه داده
                    conn = connection_to_database()
                    cursor = conn.cursor()
                    # اضافه کردن داده ی کرول شده به پایگاه داده
                    cursor.execute('''INSERT INTO newsel_post(folder_name, publisher,author,h1,title,snippet,image_url,content,source_website, tags,supervisor_to_confirm,type_of_news,published_date) 
                                    VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)''',
                                   (folder_name, self.publisher, self.author,title, title, snippet, image_url,  content, source_website, folder_name, self.supervisor_to_confirm, self.type_of_news, str(published_date)))
                    conn.close()
                    Drivers.close()
        else:
            print("This content is duplicated")

    def tasnimcrawl(self,i, wait, folder_name):
        title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='search_results_wrapper']/div["+str(i)+"]/div[1]/div[2]/div[1]/h2/a"))).text
        news = Post.objects.filter(title=title).first()
        if not(news):
            Driver = webdriver.Chrome()
            Driver.maximize_window()
            #باز کردن پایگاه خبری
            Driver.get("https://www.tasnimnews.com/")
            wait1 = WebDriverWait( Driver, 3)
            #جستجوی عنوان خبر دریافت شده
            searchclick=wait1.until(EC.presence_of_element_located((By.XPATH,"/html/body/header[1]/nav/ul/li[2]/a")))
            searchclick.click()
            search=wait1.until(EC.presence_of_element_located((By.XPATH,"/html/body/header[1]/nav/ul/li[2]/div/form/div/input")))
            search.send_keys(title)
            search.send_keys(Keys.ENTER)
            titlenews=wait1.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/section[1]/div/section[1]/section/section/article/a/div[2]/h2"))).text
            # for j in range(1,10,1):
                # pathtitle=' /html/body/main/div/div/div/section[2]/div/ul/li[1]/div/h3/a'
                # جستجوی عنوان خبر و چک کردن عنوان به دست امده با عنوان قبلی
            titlenews=wait1.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/section[1]/div/section[1]/section/section/article/a/div[2]/h2'))).text
            if titlenews[0:15]==title[0:15]:
                #استخراج چکیده خبر
                snippet=wait1.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/section[1]/div/section[1]/section/section/article/a/div[2]/h4"))).text
                press_link=wait1.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/section[1]/div/section[1]/section/section/article/a"))).get_attribute('href')
                Drivers = webdriver.Chrome()
                Drivers.maximize_window()
                Driver.close()
                Drivers.get(press_link)
                wait3 = WebDriverWait( Drivers, 3)
                #استخراج عکس و محتوای خبر
                image_url=wait3.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/main/div/section[1]/div/section[1]/article/div[2]/figure/a/img"))).get_attribute('src')
                content=wait3.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/section[1]/div/section[1]/article/div[3]"))).text
                # url = Drivers.current_url
                source_website = "تسنیم"
                published_date = datetime.now()
                # اتصال به پایگاه داده
                conn = connection_to_database()
                cursor = conn.cursor()
                # اضافه کردن داده ی کرول شده به پایگاه داده
                cursor.execute('''INSERT INTO newsel_post(folder_name, publisher,author,h1,title,snippet,image_url,content,source_website, tags,supervisor_to_confirm,type_of_news,published_date) 
                                    VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)''',
                                   (folder_name, self.publisher, self.author,title, title, snippet, image_url,  content, source_website, folder_name, self.supervisor_to_confirm, self.type_of_news, str(published_date)))
                conn.close()
                Drivers.close()
        else:
            print("This content is duplicated")

    def mehrcrawl(self,i, wait, folder_name):
        title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='search_results_wrapper']/div["+str(i)+"]/div[1]/div[2]/div[1]/h2/a"))).text
        news = Post.objects.filter(title=title).first()
        if not(news):
            Driver = webdriver.Chrome()
            #باز کردن پایگاه خبری
            Driver.get("https://www.mehrnews.com/")
            wait1 = WebDriverWait( Driver, 3)
            #جستجوی عنوان خبر دریافت شده
            search=wait1.until(EC.presence_of_element_located((By.XPATH,"/html/body/header/div[1]/div/div/div[2]/div/form/div/input")))
            search.send_keys(title)
            search.send_keys(Keys.ENTER)
            #استخراج چکیده خبر
            snippet=wait1.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/section[2]/div/ul/li[1]/div/p[1]"))).text
            press_link=wait1.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/section[2]/div/ul/li[1]/div/h3/a"))).get_attribute('href')
            Drivers = webdriver.Chrome()
            Driver.close()
            Drivers.get(press_link)
            wait3 = WebDriverWait( Drivers, 3)
            #استخراج عکس و محتوای خبر
            image_url=wait3.until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div/div/div/div/div[1]/article/div[3]/figure/img"))).get_attribute('src')
            content=wait3.until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div/div/div[1]/article/div[4]/div[1]"))).text
            # استخراج ادرس خبر
            # url = Drivers.current_url
            source_website = "مهر"
            published_date = datetime.now()
            # اتصال به پایگاه داده
            conn = connection_to_database()
            cursor = conn.cursor()
            # اضافه کردن داده ی کرول شده به پایگاه داده
            cursor.execute('''INSERT INTO newsel_post(folder_name, publisher,author,h1,title,snippet,image_url,content,source_website, tags,supervisor_to_confirm,type_of_news,published_date) 
                                VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s)''',
                               (folder_name, self.publisher, self.author,title, title, snippet, image_url,  content, source_website, folder_name, self.supervisor_to_confirm, self.type_of_news, str(published_date)))
            conn.close()
            Drivers.close()
        else:
            print("This content is duplicated")



