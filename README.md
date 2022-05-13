# TigerMap
TigerMap is a course selection treasure map that helps you find your way through Princeton by showing which courses serve as prerequisites to a class and which courses that particular class unlocks. 

Created by Leo Stepanewk and Aaliyah Sayed for HackPrinceton Spring 2022.

https://devpost.com/software/tigermap

https://tiger-map.herokuapp.com/

## Inspiration
Course selection is an exciting but frustrating time to be a Princeton student. While you can look at all the cool classes that the university has to offer, it is challenging to aggregate a full list of prerequisites and borderline impossible to find what courses each of them leads to in the future. We recently encountered this problem when building our schedules for next fall. The amount of searching and cross-referencing that we had to do was overwhelming, and to this day, we are not exactly sure whether our schedules are valid or if there will be hidden conflicts moving forward. So we built TigerMap to address this common issue among students.

## What it does
TigerMap compiles scraped course data from the Princeton Registrar into a traversable graph where every class comes with a clear set of prerequisites and unlocked classes. A user can search for a specific class code using a search bar and then browse through its prereqs and unlocks, going down different course paths and efficiently exploring the options available to them.

## How we built it
We used React (frontend), Python (middle tier), and a MongoDB database (backend). Prior to creating the application itself, we spent several hours scraping the Registrar's website, extracting information, and building the course graph. We then implemented the graph in Python and had it connect to a MongoDB database that stores course data like names and descriptions. The prereqs and unlocks that are found through various graph traversal algorithms, and the results are sent to the frontend to be displayed in a clear and accessible manner.

## Challenges we ran into
Data collection and processing was by far the biggest challenge for TigerMap. It was difficult to scrape the Registrar pages given that they are rendered by JavaScript, and once we had the pages downloaded, we had to go through a tedious process of extracting the necessary information and creating our course graph. The prerequisites for courses is not written in a consistent manner across the Registrar's pages, so we had to develop robust methods of extracting data. Our main concern was ensuring that we would get a graph that completely covered all of Princeton's courses and was not missing any references between classes. To accomplish this, we used classes from both the Fall and Spring 21-22 semesters, and we can proudly say that, apart from a handful of rare occurrences, we achieved full course coverage and consistency within our graph.

## Accomplishments that we're proud of
We are extremely proud of how fast and elegant our solution turned out to be. TigerMap definitely satisifes all of our objectives for the project, is user-friendly, and gives accurate results for nearly all Princeton courses. The amount of time and stress that TigerMap can save is immeasurable.

## What we learned
- Graph algorithms
- The full stack development process
- Databases
- Web-scraping
- Data cleaning and processing techniques

## What's next for TigerMap
We would like to improve our data collection pipeline, tie up some loose ends, and release TigerMap for the Princeton community to enjoy!
