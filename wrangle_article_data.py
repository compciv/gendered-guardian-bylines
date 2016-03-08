import json
from csv import DictWriter
from os import makedirs
from os.path import join
from glob import glob
WRANGLED_DATA_FILE = join('tempdata', 'wrangled_articles.csv')
WRANGLED_HEADERS = ['id', 'sectionId', 'byline', 'newspaperPageNumber',
    'webUrl', 'webTitle','webPublicationDate']
ARTICLES_DIR = join('tempdata', 'articles')
datafilenames = glob(join(ARTICLES_DIR, '*.json'))

wrangled_articles = []
for fname in datafilenames:
    articles = json.load(open(fname, 'r'))
    print("Opening", fname, 'which has', len(articles), 'articles')
    for a in articles:
        if( a['fields'].get('newspaperPageNumber')
            and a['fields'].get('byline') ):
            byline = a['fields']['byline']
            if('Editorial' not in byline and
                           'Letters' not in byline and
                           'Anonymous' not in byline and
                           'Corrections' not in byline):
                d = {'id': a['id']}
                d['sectionId'] = a['sectionId']
                d['webUrl'] = a['webUrl']
                d['webTitle'] = a['webTitle']
                d['webPublicationDate'] = a['webPublicationDate']
                d['byline'] = a['fields']['byline']
                d['newspaperPageNumber'] = a['fields']['newspaperPageNumber']
                wrangled_articles.append(d)

# write to file
with open(WRANGLED_DATA_FILE, 'w') as f:
    w = DictWriter(f, fieldnames=WRANGLED_HEADERS)
    w.writeheader()
    for a in wrangled_articles:
        w.writerow(a)
