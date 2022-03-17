from pandas import read_json, to_datetime
from isbntools.app import isbn_from_words

library = read_json('library.json')
original_columns = library.columns

library['isbn'] = library.apply(lambda x : isbn_from_words(x.title + " " + x.authors) or None, axis=1)
library["Date Added"] = library.apply(lambda x: to_datetime(x["date_added"], format='%Y-%m-%d', exact=False).strftime('%Y-%m-%d'), axis=1)
library["Date Read"] = library.apply(lambda x: to_datetime(x["date_added"], format='%Y-%m-%d', exact=False).strftime('%Y-%m-%d') if x["is_finished"] == True else None, axis=1)
library['Title'] = library.apply(lambda x : x.title, axis=1)

library.drop(columns=original_columns, inplace=True)
library.dropna(subset=['isbn', 'Date Read'], inplace=True)
library.to_csv('library.csv', index=False)
