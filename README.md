# Audible -> Goodreads sync

This is a simple project to export your audible library information and format it in a way that may be imported into goodreads.

Created using [audible-cli](https://github.com/mkb79/audible-cli), with inspiration from [this gist](https://gist.github.com/readywater/b71c11428a151654474cdb673756319e).

Note that this is just a script, and has not actually been implemented as an extension for audible-cli - though that may eventually happen as time allows.

The transform omits any items in the audible library that did not have an isbn or has not been finished.

## Usage
Prerequisites:
* Python 3.10
* Poetry

```
poetry install
poetry shell
audible quickstart
audible library export -f json -o library.json
python goodreads_transform.py
```

In your browser, navigate to goodreads -> My Books, select the import option on left under tools. Import from file, provide library.csv.
