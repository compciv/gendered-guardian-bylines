import unicodedata
from gender import detect_gender
from csv import DictReader, DictWriter
from os.path import join
WRANGLED_DATA_FILE = join('tempdata', 'wrangled_articles.csv')
CLASSIFIED_DATA_FILE = join('tempdata', 'classifed_articles.csv')


def get_usable_name(namestr):
    """
    namestr can be many forms:
     - "Peter Bradshaw"
     - "Patrick Wintour, political editor"
     - "Interview by Laura Barnett"
     - "Al Gore, former US vice-president, and David Blood"
     - "Andrew Mueller, Julia Raeside, Martin Skegg and Ali Catterall"
     - "Juliette Garside in Barcelona and Samuel Gibbs

    So we'll do this:

    if the word "by" is in the byline, get the first word that
    comes after "by", i.e. "Laura" in "Interview by Laura Barnett

    Otherwise, get the very first word -- we only count the first
     person in each byline
    """
    if ' by ' in namestr:
        xby = namestr.split('by ')[1]
        uname = xby.split(' ')[0]
    else:
        uname = namestr.split(' ')[0]
    # remove funny accents
    uname = unicodedata.normalize('NFKD', uname).encode('ASCII', 'ignore').decode()
    return uname


with open(WRANGLED_DATA_FILE) as f:
    articles = list(DictReader(f))

classified_headers = list(articles[0].keys()) + ['usable_name', 'gender', 'ratio']

# prepare the CSV
w = open(CLASSIFIED_DATA_FILE, 'w');
wcsv = DictWriter(w, fieldnames=classified_headers)
wcsv.writeheader()


ct = 0
for a in articles:
    ct += 1
    uname = get_usable_name(a['byline'])
    print("Article", ct, "extracted: --",  uname, "-- from:", a['byline'])
    xresult = detect_gender(uname)
    a['usable_name'] = uname
    a['gender'] = xresult['gender']
    a['ratio'] = xresult['ratio']
    wcsv.writerow(a)

w.close()
