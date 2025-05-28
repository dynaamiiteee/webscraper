# webscraper
## Overview

**Project Title**: Webscraper

**Project Description**: A program that analyzes if a website is positive, negative, or neutral.

**Project Goals**: A web scraper that pulls the html from a website and then pulls out the article contents.  It then uses semetics to measure if a website is positive, negative, or neutral.

## Instructions for Build and Use

Steps to build and/or run the software:

1. You will need to install the python libraries used
2. You will also need to install python
3. then run the file test_scraper.py

Instructions for using the software:

1. The code will ask for you to input a link to a website.
2. Select any news article you would like. (The code was tested on [fool.com](https://www.fool.com/) news articles about the stock market.  For the most sure results use an article from that site)
3. It will then output the results to you.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* requests
* bs4
* time
* nltk
* python


## Useful Websites to Learn More
I found these websites useful in developing this software:

* [requests](https://pypi.org/project/requests/)
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
* [python](https://www.python.org/)
* [NLTK](https://www.nltk.org/install.html)
* [time](https://docs.python.org/3/library/time.html)
## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add code that recursively checks the other website links on each site it checks.
* [ ] Relate the articles to their main idea or stock they are associated with.
* [ ] Make a website for it that allows you to enter the link more conveniently.
