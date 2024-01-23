import requests
from bs4 import BeautifulSoup


def get_data(url,filename):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.text
        paragraphs = [p.text.strip() for p in soup.find_all('p')]
        headers = [h.text.strip() for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        links = [link['href'] for link in soup.find_all('a', href=True)]
        images = [img['src'] for img in soup.find_all('img', src=True)]

        print(f'Title: {title}\n')
        
        print('Headers:')
        for header in headers:
            print(header)
        print()

        print('Paragraphs:')
        for paragraph in paragraphs:
            print(paragraph)
        print()

        print('Links:')
        for link in links:
            print(link)
        print()

        print('Images:')
        for image in images:
            print(image)
        print()


        with open(filename+'.txt', 'w', encoding='utf-8') as file:
            file.write(f'Title: {title}\n\n')
            file.write('Headers:\n')
            for header in headers:
                file.write(f'{header}\n\n')
            file.write('Paragraphs:\n')
            for paragraph in paragraphs:
                file.write(f'{paragraph}\n\n')
            file.write('Links:\n')
            for link in links:
                file.write(f'{link}\n')
            file.write('Images:\n')
            for image in images:
                file.write(f'{image}\n')
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')

url1 = "https://cetcell.mahacet.org/search-institute/"
url2 = "https://cetcell.mahacet.org/search-institute/?getintitutecode=5380"

get_data(url1,"cellcet")
get_data(url2,"cellcetinst")

