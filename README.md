# Introduction to nhentei
## About:
Short: nhentei is a python implementation of nHentai's API.
Why: Because nHentai's documentation of their API is really...short. That's why nhentei exists.
nhentei is an asynchronous library, keep that in mind.
## Required packages:
Following packages will be installed too when pip installing nhentei:
 - aiohttp
 - requests
 - asyncio

Made in python 3
## Getting started:
Install nhentei via pip:

    pip install nhentei

 If you do not have pip installed, get pip first.
 To use it in your project, put


    from nhentei import nfunctions
  at the top of your python file.
  We'll refer to the commands with


    nfunctions.*functionName()*
   later

## Basic example:
nhentei basically consists out of utility functions containing direct API requests.

    from nhentei import nfunctions
	#Get a dictionary containing metadata:
    dict = await nfunctions.getByID("1")
    #This will return a dictionary containing all data of hentai with ID 1
    pages = dict['num_pages']
    #pages now contains the number of pages the hentai has

## Hentai dictionaries: What do they store?
You will find a list of keys you can use to get data from the dictionary below:
| key | description |
| :------------- | :----------: |
| id| unique nhentai identifier, starting from 1 |
| media_id |used to get images or media |
| title| returns a dictionary (more to that later) |
| images| returns a dictionary (more to that later)|
| scanlator| name of the scanlator |
| upload_date| date in unix timestamp format) |
| tags| returns an array of tags(more to that later) |
| num_pages| number of pages |
| num_favorites| number of favorites|

## "title" dictionary
The returned dictionary for the key "title" contains following keys:

    "english" --> Returns the title in english (string)(always exists)
    "japanese" --> Returns the title in japanese (string)(not guaranteed to exist)
    "pretty" --> Returns the title in a pretty format (string)(not guaranteed to exist)
## "images" dictionary
The returned dictionary for the key "images" contains following keys:

    "pages"--> Returns an array containing dictionaries, if the hentai has
		    14 pages, the array will go from 0-13.
		    Every dictionary contains following keys:
		    "t" --> returns a single char
		    "w" --> returns the width of the image
		    "h" --> returns the height of the image
    "cover"-->This dictionary contains following keys:
		    "t" --> returns a single char
		    "w" --> returns the width of the image
		    "h" --> returns the height of the image
    "thumbnail"-->This dictionary contains following keys:
		    "t" --> returns a single char
		    "w" --> returns the width of the image
		    "h" --> returns the height of the image
## "tags" array / list
Every array slot / list slot contains a dictionary representing a "tag",
it has following keys:

    "id" --> Identifier for the tag
    "type" --> Returns tag type: can be either "artist", "tag", "group", "parody", "character", "language", "category"
    "name" --> Depends on the "type": for artists, this will be the name of the artist, for tag it will be the name of the tag.
    "url" --> the payload url
    "count" --> number of hentai with this tag/artist/etc.

# Functions:

## getByID(id)
| parameter name | type | returns |  
| :------------- | :----------: | -----------: |  
| id | String | Dictionary containing hentai metadata |

This function will return the above explained dictionary by giving it an ID

## getByTags(tags, *page*, *sort*,  num)

**Takes parameters:**

 - **tags** (String format, separated by commas) The tags you want to search with
 - **page** (int format)(**optional**, defaults to 1) The result page to get
 - **sort** (String format)(**optional**, defaults to "popular") The sorting algorithm
 - **num** (int format)(**optional**, defaults to "popular") The number of entries

**Returns:** list -- Contains dictionaries with hentai with the tags

## getPayloadSearch(payload)

**Takes parameters:**

 -  **payload** (In string format, more to payloads soon)

**Returns**: dictionary

## getByTitle(title, *page*, *sort*)

**Takes parameters:**

 - **tags** (String format, separated by commas)
 - **page** (integer format)(**optional**, defaults to 1)
 - **sort** (String format)(**optional**, defaults to "popular")

**Returns:** list -- Contains dictionary of hentai with the title

## getByCharacter(character, *page*, *sort*)

**Takes parameters:**

 - **character** (String format, separated by commas)
 - **page** (integer format)(**optional**, defaults to 1)
 - **sort** (String format)(**optional**, defaults to "popular")

**Returns:** list -- Contains dictionary of hentai with the character(s)


## getByParody(title, *page*, *sort*)

**Takes parameters:**

 - **title** (String format, separated by commas)
 - **page** (integer format)(**optional**, defaults to 1)
 - **sort** (String format)(**optional**, defaults to "popular")

**Returns:** list -- Contains dictionary of hentai that are a parody of the title


## getCover(media_id)

**Takes parameters:**

 - **media_id** (String format, separated by commas)


**Returns:** url to the source image

## getPageImage(media_id, page)

**Takes parameters:**

 - **media_id** (String format, separated by commas)
 - **page** (String format, separated by commas) The page of the hentai, starts with 0


**Returns:** url to the source image


# Credits to:
EpicGamer for crawling through API outputs
[nhentai.net](nhentai.net) for the API and art
