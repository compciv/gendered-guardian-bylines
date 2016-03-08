
# Gendered analysis of Guardian bylines

__Disclaimer:__ This project [is meant to be one of several example projects showing how effectively and industriously we can use public data to do gender classification](http://www.compciv.org/assignments/projects/gender-detector-data/) if we don't care about statistics or real-world complexities or computational efficiency. It is not meant to be an actual study or a display of programming best practices.

## Introduction

This repo contains scripts to access The Guardian's content API and to analyze the gender of the bylines.

[A gist giving more background about using The Guardian's API](https://gist.github.com/dannguyen/c9cb220093ee4c12b840)

The analysis was restricted to articles that had actual bylines and had a `newspaperPageNumber` attribute. Though it's fairly easy to pull down a year's worth of data, this analysis looks at articles from March 2015 to May 2015.

### Findings in brief

Overall, women were found to have 32% of the total bylines covered in this analysis.

Though bylines attributed to women versus men reached near parity in the business section (about 280 bylines each), other sections met past expectations and stereotypes, including: in the lifestyles section, women's bylines nearly double that of the men's. In football, the ratio is 8 to 1 in favor of men.



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
