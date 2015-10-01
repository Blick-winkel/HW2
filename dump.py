import urllib.request as url
import re,glob,os
def load_dump():
    lang = input('Введите код языка: ')
    page = url.urlopen('https://dumps.wikimedia.org/backup-index.html')
    text = page.read().decode('utf-8')
    r = re.search('<a href="'+lang+'wiki/(.*?)"',text)
           
    #print ("https://dumps.wikimedia.org/" + lang + 'wiki/' + r.group(1)+'/'+lang+'wiki'+'-'+ r.group(1)+'-pages-articles-multistream.xml.bz2')
    
    url.urlretrieve("https://dumps.wikimedia.org/" + lang + 'wiki/' + r.group(1)+'/'+lang+'wiki'+'-'+
           r.group(1)+'-pages-articles-multistream.xml.bz2',lang+'wiki'+'-'+
           r.group(1)+'-pages-articles-multistream.xml.bz2')
    print ('загрузка завершена')
load_dump()


def find_articles():
    titles = []
    art = open('article_names.txt', 'w', encoding = 'utf-8')
    lang = input('Введите код языка: ')
    lang = lang + 'wiki-'
    names = glob.glob('*.xml')
    for name in names:
        if os.path.isfile(name) and lang in name and 'pages-articles-multistream' in name:
            f = open(name, 'rb')
            for line in f:
                line = line.decode('utf-8')
                articles = re.findall('<title>(.*?)</title>',line, flags=re.U)
                for i in articles:
                    titles.append(i)
    titles = (sorted(titles))
    for title in titles:
        art.write(title + '\r\n')
    f.close()
    art.close()




find_articles()