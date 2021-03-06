import asyncio
import aiohttp
import requests
# Get hentai by id: Returns dictionary containing hentai or False
async def getByID(_id):
    if not str(_id).isdigit():
        return False;
    async with aiohttp.ClientSession() as session: # Using aiohttp, request a session
        async with session.get('http://nhentai.net/api/gallery/'+str(_id)) as resp:
            try:
                response = await resp.json() # Await response
                if "error" in response:
                    # Does not exist:
                    return False;
                else:
                    return response;
            except:
                print("Error: Web request failed. (ID search)")
                return False;



async def getByTags(_tags,_page = 1,_sort='popular',_num = 1): # Returns an array containing dictionaries of hentai.

    payload = {'query':'tag:'+str(_tags),'page':_page, 'sort': str(_sort)}
    #payload = {'query':'tag:'+str(_tags),'page': 1, 'sort': 'popular'}
    try:
        async with session.get(url='https://nhentai.net/api/galleries/search', params=payload) as resp:
            response = await resp.json() # Await response

            resultArray = response["result"]
            resultLength = int(len(resultArray))
            return resultArray[:_num];
    except:
        print("Error: Web request failed. (Payload)(Tags)")


#Payload search

"""
Example:
    payload = {'query':f'title:{requestedTagString}','page': 1, 'sort':'popular'}
                    This above payload will return search results with hentai containing a specified title.

"""
async def getPayloadSearch(payload):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://nhentai.net/api/galleries/search', params=payload) as resp:
                response = await resp.json() # Await response
                return response;
    except:
        print("Error: Web request failed. (Payload)")


# Gets a hentai dictionary by Title (optional: page, sorting)
async def getByTitle(_title,_page = 1,_sort='popular'):
    payload = {'query':'title:'+str(_title),'page': _page, 'sort': _sort}
    #payload = {'query':'tag:'+str(requestedTagString),'page': 1, 'sort': 'popular'}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://nhentai.net/api/galleries/search', params=payload) as resp:
                response = await resp.json() # Await response
                return response["result"]
    except:
        print("Error: Web request failed. (Payload)(Title)")



# Gets a hentai dictionary by Title (optional: page, sorting)
async def getByCharacter(_character,_page = 1,_sort='popular'):
    payload = {'query':f'character:{requestedTagString}','page':_page,'sort':_sort}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://nhentai.net/api/galleries/search', params=payload) as resp:
                response = await resp.json() # Await response
                return response["result"];
    except:
        print("Error: Web request failed. (Payload)(Character)")


# Gets a hentai dictionary by Title (optional: page, sorting)
async def getByParody(_parody,_page = 1,_sort='popular'):
    payload = {'query':f'parodies:{requestedTagString}','page':_page ,'sort':_sort}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://nhentai.net/api/galleries/search', params=payload) as resp:
                response = await resp.json() # Await response
                return response["result"];
    except:
        print("Error: Web request failed. (Payload)(Parody)")



async def getCover(_mediaid):
    if not str(_id).isdigit():
        return False;
    coverURL = "https://t.nhentai.net/galleries/"+mediaID+"/cover.jpg"
    return coverURL;


async def getPageImage(_mediaid, _page):
    if not str(_id).isdigit():
        return False;
    coverURL = "https://i.nhentai.net/galleries/"+str(_mediaid)+"/"+str(_page)+".jpg"
    return coverURL;
