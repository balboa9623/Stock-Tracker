from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import render

# for GoogleNews API
from GoogleNews import GoogleNews
# from newspaper import Article
# import pandas as pd

# from datetime import datetime, date, timedelta
import datetime

# NewsAPI
from newsapi import NewsApiClient

import nltk
nltk.download('punkt')


def HomePage(request):
    # template_name = 'home.html'

    newsapi = NewsApiClient(api_key='48020ab7cd514cbc87db96025a1843fb')
    top = newsapi.get_top_headlines(category='business', country='us')

    l = top['articles']
    desc = []
    news = []
    img = []
    url = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    lst = zip(news, desc, img , url)

    return render(request, 'home.html', context={'lst':lst})

    # today = datetime.date.today()
    # DD = datetime.timedelta(days=30)
    # earlier = today - DD
    # earlier_str = earlier.strftime("%m/%d/%Y")
    # # print(today)
    # # print(earlier_str)
    # googlenews = GoogleNews(start=earlier_str, end=today)
    # googlenews.search('Stock market')
    #
    # for i in range(2, 3):
    #     googlenews.getpage(i)
    #     result = googlenews.result()
    #     df = pd.DataFrame(result)
    # list=[]
    #
    # for ind in df.index:
    #     dict={}
    #     article = Article(df['link'][ind])
    #     article.download()
    #     article.parse()
    #     article.nlp()
    #     dict['Date']=df['date'][ind]
    #     dict['Media']=df['media'][ind]
    #     dict['Title']=article.title
    #     dict['Article']=article.text
    #     dict['Summary']=article.summary
    #     list.append(dict)
    # # print(list)
    # news_df = pd.DataFrame(list)
    # news_df.to_excel("articles.xlsx")


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("loginHome"))
        return super().get(request, *args, **kwargs)


class LoginPage(TemplateView):
    template_name = "home.html"

