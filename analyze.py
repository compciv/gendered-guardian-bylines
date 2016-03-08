from csv import DictReader
from os.path import join
CLASSIFIED_DATA_FILE = join('tempdata', 'classifed_articles.csv')

datarows = list(DictReader(open(CLASSIFIED_DATA_FILE)))
# must typecast ratio to integer
for d in datarows:
    if d['ratio']:
        d['ratio'] = int(d['ratio'])

# get section identifiers
section_ids = set([d['sectionId'] for d in datarows])


for sec_id in section_ids:
    sectionrows = [d for d in datarows if d['sectionId'] == sec_id]
    # skip if number of things per section is less than 500
    if len(sectionrows) > 500:
        print("Section:", sec_id)
        female_rows = [d for d in sectionrows if d['gender'] == 'F' and d['ratio'] > 95]
        male_rows = [d for d in sectionrows if d['gender'] == 'M' and d['ratio'] > 95]
        print("\tF:", len(female_rows))
        print("\tM:", len(male_rows))
        print("\tF/M:", round(100 * len(female_rows) / len(male_rows)))

