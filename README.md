
# Gendered analysis of Guardian bylines

__Disclaimer:__ This project [is meant to be one of several example projects showing how effectively and industriously we can use public data to do gender classification](http://www.compciv.org/assignments/projects/gender-detector-data/) if we don't care about statistics or real-world complexities or computational efficiency. It is not meant to be an actual study or a display of programming best practices.

## Introduction

This repo contains scripts to access The Guardian's content API and to analyze the gender of the bylines.

[A gist giving more background about using The Guardian's API](https://gist.github.com/dannguyen/c9cb220093ee4c12b840)

The analysis was restricted to articles that had actual bylines and had a `newspaperPageNumber` attribute. Though it's fairly easy to pull down a year's worth of data, this analysis looks at articles from March 2015 to May 2015.

### Findings in brief

Overall, women were found to have 32% of the total bylines covered in this analysis.

Though bylines attributed to women versus men reached near parity in the business section (about 280 bylines each), other sections met past expectations and stereotypes, including: in the lifestyles section, women's bylines nearly double that of the men's. In football, the ratio is 8 to 1 in favor of men.



### Methodology and caveats

The [dataset comes from the Guardian's API](https://gist.github.com/dannguyen/c9cb220093ee4c12b840) and covers the time period from March 1, 2015 to May 31, 2015. The data, as fetched from the API, is wrangled/filtered to 11,000 records, which have these characteristics:

- a valid `"newspaperPageNumber"` value, which would indicate that the particular article appeared in print.
- a valid `"byline"` -- bylines that were rejected include `"Editorial"` and `"Letters"`

The byline field is _not at all_ straightforward or uniform. Here are the kinds of values that it might have:

- "Peter Bradshaw"
- "Patrick Wintour, political editor"
- "Interview by Laura Barnett"
- "Al Gore, former US vice-president, and David Blood"
- "Andrew Mueller, Julia Raeside, Martin Skegg and Ali Catterall"
- "Juliette Garside in Barcelona and Samuel Gibbs"

It's difficult enough to consistently extract a full name. But what are we to do with bylines with multiple people? For simplicity's sake, I've taken the narrow view that whoever comes first in the byline is the most important person to the story. Therefore, every story will be considered as having one byline, either male or female or nondeterminate. Whether this completely destroys the statistical analysis is a question for another time.


#### British names

Virtually every British person I know who has the name of "Robin" is male. In America, every "Robin" I know is female. This is just one sign that the [U.S. baby name data may be lacking](https://www.ssa.gov/oact/babynames/background.html), and if I had more time, I'd [collect the data from data.uk.gov](https://data.gov.uk/dataset/baby_names_england_and_wales).

To compensate, I've added an extra filter in my [classify.py](classify.py) script:

~~~py
MIN_GENDER_RATIO = 95 # only consider gender classifications of 95%+
for d in datarows:
    if d['ratio'] and d['ratio'] >= MIN_GENDER_RATIO:
      # etc etc
~~~

This eliminates all bylines/names for which we don't have at least a 95% certainty as it stands with American baby name data. 






## How to use it

Note: if you want to __clone__ this repo from Github, run this:

    git clone https://github.com/compciv/gendered-guardian-bylines


It will create a new sub-folder named `gendered-guardian-bylines`. 

Simply run the following scripts provided in this repo in this order:


### fetch_gender_data.py

Downloads the raw [babyname data from the Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html) and unpacks it into the __tempdata/babynames__ directory.


### wrangle_gender_data.py

Selects and compiles the baby name records for every five years between 1900 and 1991, and adds the records for 2014.


### creds_guardian.txt

The script that fetches data from the Guardian API expects you to have registered as a developer with the Guardian: [some background and context here](https://gist.github.com/dannguyen/c9cb220093ee4c12b840).

Once you've gone through the process, create a file named `creds_guardian.txt` and paste in the API key you were given.

### fetch_article_data.py

Fetches article data as raw JSON, for every day as designated by `START_TIME` and `END_TIME`

### wrangle_article_data.py

The fetched data comes as JSON files for every day.

This script reads through every day's worth of results and selects only results that have:

- a valid `byline`
- a valid `newspaperPageNumber`

It stores all of the results in a flat CSV file for easy access: [wrangled_articles.csv](wrangled_articles.csv)


### classify.py

For each row in [tempdata/wrangled_articles.csv](tempdata/wrangled_articles.csv), I use the `detect_gender()` function in the __gender.py__ script to determine the likely gender of the name. 

The bylines can be quite diverse in their format. So the `extract_usable_name()` formula does these things:

- if the string `' by '` is in the byline, then assume it is in the format of `"something by first_name last_name"`
- else, assume that it is in the format of `"firstname lastname blah blah"`
- split by space, grab the first word
- Because Guardian authors are more likely to have non-ASCII characters in their name, we write a little subroutine to transliterate, i.e. from `"Beyoncé"` to `"Beyonce"`:



~~~py
    import unicodedata
    # etc. etc.
    uname = unicodedata.normalize('NFKD', uname).encode('ASCII', 'ignore').decode()
~~~



A new file -- [tempdata/classified_articles.csv](tempdata/classified_articles.csv) -- is produced. Basically, it's wrangled_data.csv with three new columns:

- gender
- ratio (the likelihood/bias of the baby boy vs girl numbers)
- usable_name - the partial string extracted from `first_name` to do the classification.


### analyze.py

Reads [tempdata/classified_data.csv](tempdata/classified_data.csv) and produces the output seen at the bottom of this README's analysis.



### Ancillary files

Here are some supporting files. You don't actually _run_ these, but they are called by the other files.

### gender.py

This contains the code to load the wrangled gender data and the `detect_gender()` function.


### Past research and analysis

Gender analysis of the media has frequently been broached by examining not just the demographic makeup of a news organization's hired journalists, but the number and placement of bylines accorded to those journalists.

Margaret Sullivan, the New York Times Public Editor, referred to [a Women's Media Center study](http://wmc.3cdn.net/2e85f9517dc2bf164e_htm62xgan.pdf) in a column titled, [Still Talking About It: ‘Where Are the Women?’](http://publiceditor.blogs.nytimes.com/2014/05/12/still-talking-about-it-where-are-the-women):

> * At the nation’s 10 most widely circulated newspapers, men had 63 percent of the bylines, nearly two for every one for a woman. (The study looked at bylines only in the first section of the papers.)
>
> * Among those papers, The Times had the biggest gender gap – with 69 percent of bylines going to men.

Though the Guardian is a different paper based in a different country and culture, there is no reason to believe that the gap is different or less substantial. In fact, [the Guardian's own datablog looked at its competitors' and its own gap](http://www.theguardian.com/news/datablog/2012/sep/07/gender-media-best-data-available).

One [datapoint in late 2011](http://www.theguardian.com/news/datablog/2011/dec/06/women-representation-media): 

> National papers were all shown to have large gender gaps in byline averages. The Daily Mail and the Guardian recorded the lowest male dominance at 68% male and 72% male respectively.
> 

While I won't be measuring the exact same datapoints, [I will be using the Guardian's API](https://gist.github.com/dannguyen/c9cb220093ee4c12b840) to collect article metadata from their system -- covering a period of about 2 months -- and look at the gender breakdown of bylines per section in the print newspaper.

The [Guardian also considered front page bylines](http://www.theguardian.com/news/datablog/2012/oct/15/women-newspapers-front-pages) -- in 2012, a sampling found the byline ratio to be 68 to 19 in favor of men.


## Results

Generally, male bylines dominate the major sections, with the exception of business and lifeandstyle.

```
Total bylines
F: 3117
M: 6778
F ratio of the total: 32%
-----------------------------------------------
Front page bylines
F: 43
M: 270
F ratio of the total: 14%
----------------------------------------------
By section
Section: books
  F: 219
  M: 299
  F/M: 73
Section: football
  F: 111
  M: 817
  F/M: 14
Section: sport
  F: 36
  M: 885
  F/M: 4
Section: lifeandstyle
  F: 469
  M: 247
  F/M: 190
Section: world
  F: 259
  M: 500
  F/M: 52
Section: commentisfree
  F: 221
  M: 380
  F/M: 58
Section: politics
  F: 174
  M: 436
  F/M: 40
Section: music
  F: 244
  M: 465
  F/M: 52
Section: business
  F: 280
  M: 282
  F/M: 99
Section: film
  F: 44
  M: 413
  F/M: 11
```
