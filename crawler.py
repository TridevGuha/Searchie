#!/usr/bin/env python3

def get_page(url):
    try:
        import urllib.request
        return urllib.request.urlopen(url).read().decode('utf-8')
    except:
        return ''

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
            print(crawled)
    return crawled

#print(crawl_web('https://www.udacity.com/cs101x/index.html'))
#print(crawl_web('http://xkcd.com/554'))
print(crawl_web('http://xkcd.com/353'))
