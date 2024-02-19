
from rest_framework.response import Response
from .serializers import PostSerializer,SearchCrawlSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets,generics

import psycopg2

from selenium import webdriver
from ...models import Post
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

from jdatetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .crawl_web import *


class NewsViewset(viewsets.ViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #تعریف یک نمونه از کلاس صفحه ی کرول وب
    def __init__(self):
        self.instance_of_crawlweb = CrawlViewset()

    def list(self, request):
         # جستجوی متن موردنظر
        # queryset = Post.objects.filter(is_active=True)
        # folder_name = input("لطفا کلمه یا عبارت مورد نظر خود را وارد کنید: ")
        folder_name='دانشجو'
        # ایجاد یک instance از مرورگر
        driver = webdriver.Chrome()
        # باز کردن وب‌سایت مورد نظر
        driver.get("https://khabarfarsi.com/")
        wait = WebDriverWait(driver, 3)
        searchpageone = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div/div/div/form/div/div/input")))
        # جستجوی متن موردنظر
        # queryset = Post.objects.filter(is_active=True)
        searchpageone.send_keys(folder_name)
        searchpageone.send_keys(Keys.ENTER)
        for i in range(1, 3, 1):
            # بررسی نتایج جستجو برای بدست اوردن پایگاه خبری
            path = '//*[@id="search_results_wrapper"]/div['+str(i)+']/div[1]/div[2]/div[2]/span/a'
            urlsite = wait.until(EC.presence_of_element_located(
                (By.XPATH, path))).get_attribute('href')
            print(urlsite)

            if urlsite.endswith("isna.ir"):
                self.instance_of_crawlweb.isnacrawl(i, wait, folder_name)

            elif urlsite.endswith("tasnimnews.com"):
               self.instance_of_crawlweb.tasnimcrawl(i, wait, folder_name)

            elif urlsite.endswith("mehrnews.com"):
                self.instance_of_crawlweb.mehrcrawl(i, wait, folder_name)

        driver.quit()
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

class SearchViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=SearchCrawlSerializer
    queryset=Post.objects.all()
   
