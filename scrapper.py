import requests
from bs4 import BeautifulSoup
import datetime
import schedule
import time
import database
import models
from sqlalchemy.exc import SQLAlchemyError


def scrape_and_store():
    cookies = {
        '_ga': 'GA1.1.216949129.1681445540',
        '_ga_TM52BJH9HF': 'GS1.1.1681445540.1.1.1681447041.0.0.0',
        'RT': '"z=1&dm=bseindia.com&si=9809f7fe-8d92-4c50-b750-7ec6addbdcff&ss=lgg19cw3&sl=3&tt=2j2&bcn=%2F%2F684d0d48.akstat.io%2F&rl=1&obo=1&ld=wbp8&r=293frbsj&ul=wbp9"',
    }

    headers = {
        'authority': 'www.bseindia.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': '_ga=GA1.1.216949129.1681445540; _ga_TM52BJH9HF=GS1.1.1681445540.1.1.1681447041.0.0.0; RT="z=1&dm=bseindia.com&si=9809f7fe-8d92-4c50-b750-7ec6addbdcff&ss=lgg19cw3&sl=3&tt=2j2&bcn=%2F%2F684d0d48.akstat.io%2F&rl=1&obo=1&ld=wbp8&r=293frbsj&ul=wbp9"',
        'if-modified-since': 'Fri, 14 Apr 2023 04:37:06 GMT',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx', cookies=cookies, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'id': 'ContentPlaceHolder1_gvbulk_deals'})

    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        deal_date = datetime.datetime.strptime(
            cols[0].text.strip(), '%d/%m/%Y').date()
        security_code = int(cols[1].text.strip())
        security_name = cols[2].text.strip()
        client_name = cols[3].text.strip()
        deal_type = cols[4].text.strip()
        quantity = int(cols[5].text.replace(',', '').strip())
        price = float(cols[6].text.replace(',', '').strip())
        val = {
            'security_code': security_code,
            'security_name': security_name,
            'client_name': client_name,
            'deal_type': deal_type,
            'quantity': quantity,
            'price': price,
            'deal_date': deal_date
        }

        try:
            db = database.SessionLocal()
            db_bulk_deal = models.BulkDeals(**val)
            db.add(db_bulk_deal)
            db.commit()
            db.refresh(db_bulk_deal)
            print(f"Inserted %s" % db_bulk_deal)
        except SQLAlchemyError as e:
            db.rollback()
            print("Error: %s" % e)


# schedule.every().day.at("09:00").do(scrape_and_store)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

scrape_and_store()
