#Import Libraries
from bs4 import BeautifulSoup
import requests

#Function to scrape the data
#Example Bitcoin https://coinmarketcap.com/currencies/bitcoin/
def scrape(coin="bitcoin/"):
    #Get the URL of the website

    URL = "https://coinmarketcap.com/currencies/"+coin

    #Make a request to the webiste
    webpage = requests.get(URL)

    #Parse the text from the website
    soup = BeautifulSoup(webpage.text, "html.parser")

    #Get the name of the coin and the ticker symbol
    coin_name = soup.find("h1", attrs={'class':'priceHeading'}).text.strip()
    
    #Get the coin's current price
    current_price = soup.find("div", attrs={'class':'priceValue'}).text.strip()
    
    
    print(coin_name, current_price)
    

# Run the function (By Default Bitcoin will be select)
scrape()
scrape("ethereum")