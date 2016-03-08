
# Gendered analysis of Guardian bylines

This repo contains scripts to access The Guardian's content API and to analyze the gender of the bylines.

[A gist giving more background about using The Guardian's API](https://gist.github.com/dannguyen/c9cb220093ee4c12b840)

TKTK

The analysis was restricted to articles that had actual bylines and had a `newspaperPageNumber` attribute. Though it's fairly easy to pull down a year's worth of data, this analysis looks at articles from March 2015 to May 2015.


## Results

Generally, male bylines dominate the major sections, with the exception of business and lifeandstyle.

```
Section: commentisfree
  F: 221
  M: 380
  F/M: 58
Section: world
  F: 259
  M: 500
  F/M: 52
Section: business
  F: 280
  M: 282
  F/M: 99
Section: music
  F: 244
  M: 465
  F/M: 52
Section: politics
  F: 174
  M: 436
  F/M: 40
Section: film
  F: 44
  M: 413
  F/M: 11
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
Section: books
  F: 219
  M: 299
  F/M: 73
```
