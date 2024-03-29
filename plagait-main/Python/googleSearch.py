from bs4 import BeautifulSoup
from requests import get


def search_content(query):
    language_code = "fr"
    search_term = query.replace(' ', '%20')
    search_term = '"'+search_term+'"'

    google_url = 'https://www.google.com/search?q={}&hl={}&num=15&ie=UTF-8'.format(search_term,
                                                                                   language_code)
    HEADERS = ({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Referer": "https://www.google.com/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"92\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73",
        "X-Amzn-Trace-Id": "Root=1-6119c652-54b9df497ac083bd73adffdc",

        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/61.0.3163.100 Safari/537.36'
    })
    # ----------
    # http://43.255.113.232:80
    """
        proxy = "https://140.227.67.135:6000"
        proxies = None
        if proxy:
            if proxy[:5] == "https":
                proxies = {"https": proxy}
            else:
                proxies = {"http": proxy}

    """
    # ----------

    proxies = {
        'http': 'http://71.19.146.218:80',


    }
    response = get(google_url, headers=HEADERS, proxies=proxies)

    src = response.content

    soup = BeautifulSoup(src, 'html.parser')
    # print(soup.get_text())

    content_array = soup.get_text().split("secondes)")[
        1].split("Web")[1:]

    content = ' web '.join(content_array)

    return content


# -----------------------------------------------------------------------

# print(search("Le marketing Business to Business (B to B) est le marketing des entreprises qui vendent des biens ou des services à d'autres professionnels"))

# for j in search(query, tld="com", lang='en', num=4, start=0, stop=4, pause=2.0):
#    print(j)

"""
content = search_content(
    "Le marketing Business to Business (B to B) est le marketing des entreprises ")

print(content)

"""
