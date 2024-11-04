import requests
from bs4 import BeautifulSoup

def scrape_product_details(url):
    # Extended headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.flipkart.com/",
        "DNT": "1",  # Do Not Track Request Header
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an HTTPError for bad responses (e.g., 404, 500)
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the page. Error: {e}")
        return None, None

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the title
    title_element = soup.find('span', class_='VU-ZEz')
    title = title_element.get_text(strip=True) if title_element else 'Title not found'
    
    # Find the price
    price_element = soup.find('div', class_='Nx9bqj')
    price = price_element.get_text(strip=True) if price_element else 'Price not found'
    
    return title, price

# Example usage
url = "https://www.flipkart.com/urbanware-professional-maxtopt99-rechargeable-cordless-electric-blade-beard-trimmer-ke91-shaver-men/p/itm1fb2b5499aa54?pid=SHVGSYMFTSQTNXMD&lid=LSTSHVGSYMFTSQTNXMD9FIEBZ&marketplace=FLIPKART&store=zlw%2F79s%2Fu3j&spotlightTagId=BestsellerId_zlw%2F79s%2Fu3j&srno=b_1_13&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=7688bbdc-8708-4324-bee0-055adb330ac4.SHVGSYMFTSQTNXMD.SEARCH&ppt=browse&ppn=browse&ssid=43zgapi6dc0000001730701725660"
title, price = scrape_product_details(url)

print("Title:", title)
print("Price:", price)
