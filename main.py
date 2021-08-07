
import requests
import bs4

# WEB SCRAPING - Nikola Tesla Wikipedia

result = requests.get('https://en.wikipedia.org/wiki/Nikola_Tesla')

print(type(result))

#organized the html code
soup = bs4.BeautifulSoup(result.text, 'lxml')

print(soup)

#just to grap the header page of nikola tesla
header = soup.select('h1')[0].getText()

#grapping the paragraphs in nikola tesla page
paragraphs = soup.select('p')[0].getText()

#grapping the image of nikola tesla in his wikipedia from image class in the html
image = soup.select('.image')[0]
print(image)

#let's try saving the picture of tesla in a folder on the computer
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/N.Tesla.JPG/220px-N.Tesla.JPG')
f = open('TelsaImage.jpg', 'wb')
f.write(image_link.content)
f.close()


#toscraping.com - let's print the title of the three star rated books

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
page_num = 2
base_url.format(page_num)

page1 = requests.get(base_url.format(1))
page1_soup = bs4.BeautifulSoup(page1.text, 'lxml')

#checking if the soup tracks what we want by checking its length (n of elements)
print(len(page1_soup.select('.product_pod')))

products = page1_soup.select('.product_pod')

example = products[0]
print(example.select('a')[1]['title'])

#lets print two star rated books using loops
two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        #way 1 to check if star rating two is present
        #if 'star-rating Two' in str(book):
           # print(book)

        #way 2 to check is star rating two is present
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)
            print(two_star_titles)

#We can check if something is 2 starts (string call in , example.select(rating))
#example.select('a')[1]['title'] to grab the book's title

'''
usage of soup.select() in CSS code

1-selecting an element tag and identifying which one in [] brackets
soup.select('div')[0]
soup.select('title')[0]
soup.select('h1')[0]
soup.select('p')[0]

2-selecting element's id 
soup.select('#some_id')

3-selecting an element's class
soup.select('.some_class')

4.select an element's span
soup.select('div.span')

5-select an element's span within a div element, with nothing in between
soup.select('div > span')
'''
