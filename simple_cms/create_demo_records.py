# -*-coding:utf-8-*-

"""
create demo records
"""

from simple_cms.wsgi import *
from news.models import Article, Column

def main():
    column_urls = (
        ('体育新闻', 'sports'),
        ('社会新闻', 'social'),
        ('娱乐新闻', 'entertainment'),
        ('科技新闻', 'tech'),
    )
    for column_name, url in column_urls:
        c = Column.objects.get_or_create(name=column_name, slug=url)[0]

        # 一个栏目搞十篇新闻
        for i in xrange(1, 6):
            article = Article.objects.get_or_create(
                title='{}_{}'.format(column_name,i),
                slug='article_{}'.format(i),
                content='新闻内容:{}_{}'.format(column_name,i),
            )[0]
            article.column.add(c)


if __name__ == '__main__':
    main()
    print('Done!')