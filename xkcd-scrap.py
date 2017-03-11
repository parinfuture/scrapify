import os, requests, bs4
url = 'https://xkcd.com/'
if not os.path.exists('xkcd'):
    os.makedirs('xkcd')

while not url.endswith('x'):
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        print(comicUrl)
        
        #Downloading the image
        print('Downloading image %s...' %(comicUrl))
        comicUrl1 = 'http:' + comicUrl
        res = requests.get(comicUrl1)
        res.raise_for_status()
        
        imageFile = open(os.path.join('xkcd1', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + prevLink.get('href')
    
print('Done.')