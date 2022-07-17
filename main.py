# importing modules
import requests
from bs4 import BeautifulSoup

# do your configurations here
url = "https://www.amazon.in/Echo-Dot-3rd-Gen/dp/B07PFFMP9P/ref=sr_1_2?keywords=alexa&qid=1658040977&sprefix=a%2Caps%2C246&sr=8-2" # product page
price_limit = 4000 # price limit of product


# function which get information of given product
# it returns product_title, product_price, product_on_stock
def get_product_info(url):
    try:
        response = requests.get(url, headers=({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})).content
        soup = BeautifulSoup(response, 'html.parser')
        product_title = soup.find(id='productTitle').get_text().strip()
        product_price = float(soup.find(class_='a-offscreen').get_text().strip().replace(',', '').replace('₹', ''))
        product_stock = soup.find(class_='a-color-success')
       
        if (product_stock != None):
            product_on_stock = True
        else:
            product_on_stock = False
        return product_title, product_price, product_on_stock

    except:
        return None, None, None    

if __name__ == "__main__":
    product_details = get_product_info(url) # calling get_product_info() function
    
    try:
        if (int(price_limit) >= product_details[1]):
            print("Price Below Limit!, buy Now.")
            print(url)
        else:
            print("Price Above Limit, LOL")
    except:
        print("An Error Occured")
