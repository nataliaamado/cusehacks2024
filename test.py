import math
import pandas as pd
import feedparser

CampusEvents = feedparser.parse('events.rss')
ce_title = CampusEvents.feed.title
ce_link = CampusEvents.feed.link
ce_description = CampusEvents.feed.description
print(ce_title)
print(ce_link)
print(ce_description)

