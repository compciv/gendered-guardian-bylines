from csv import DictReader
from os.path import join
CLASSIFIED_DATA_FILE = join('tempdata', 'classifed_articles.csv')
MIN_GENDER_RATIO = 95 # only consider gender classifications of 95%+

datarows = list(DictReader(open(CLASSIFIED_DATA_FILE)))
# must typecast ratio to integer
for d in datarows:
    # a reminder...'ratio' is the likelihood that the gender
    # for a given name is actually that gender...probably should
    # have named `ratio` something else...
    if d['ratio']:
        d['ratio'] = int(d['ratio'])

# get breakdown for total bylines
print("Total bylines")
all_articles = {'M': 0, 'F': 0}
for d in datarows:
    if d['ratio'] and d['ratio'] >= MIN_GENDER_RATIO:
        all_articles[d['gender']] += 1

print("F:", all_articles['F'])
print("M:", all_articles['M'])
# ratio of female bylines:
rftotal = round(100 * all_articles['F'] / (all_articles['F'] + all_articles['M']))
print('F ratio of the total:', str(rftotal) + '%')





# look at frontpage bylines (yeah, look at that sloppy copy and paste!!!)
print("-----------------------------------------------")
print("Front page bylines")
front_page_articles = {'M': 0, 'F': 0}
for d in datarows:
    if d['ratio'] and d['ratio'] >= MIN_GENDER_RATIO:
        if d['newspaperPageNumber'] == '1': # remember it is serialized as a string...
            # finally, include it in our tally
            front_page_articles[d['gender']] += 1

print("F:", front_page_articles['F'])
print("M:", front_page_articles['M'])
# ratio of female bylines:
rftotal = round(100 * front_page_articles['F'] / (front_page_articles['F'] + front_page_articles['M']))
print('F ratio of the total:', str(rftotal) + '%')


# get section identifiers
print("----------------------------------------------")
print("By section")
section_ids = set([d['sectionId'] for d in datarows])
for sec_id in section_ids:
    sectionrows = [d for d in datarows if d['sectionId'] == sec_id]
    # skip if number of things per section is less than 500
    if len(sectionrows) > 500:
        print("Section:", sec_id)
        female_rows = [d for d in sectionrows if d['gender'] == 'F' and d['ratio'] > MIN_GENDER_RATIO]
        male_rows = [d for d in sectionrows if d['gender'] == 'M' and d['ratio'] > MIN_GENDER_RATIO]
        print("\tF:", len(female_rows))
        print("\tM:", len(male_rows))
        print("\tF/M:", round(100 * len(female_rows) / len(male_rows)))

