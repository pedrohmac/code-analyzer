import requests
import json

def handler():


    headers = {
        'Accept': 'application/json'
    }
    url_start = "https://sample.url.com/interview/v1/transactions"

    cursor = False

    hashmap = {}

    bigger_value = 0
    solution = None

    while cursor is not None:

        if cursor is False:
            url = url_start
        else:
            url = url_start + "?cursor=" + cursor

        response = requests.request("GET", url, headers=headers).json()

        cursor = response.get('next_cursor')

        for transaction in response.get('data'):

            card_method = transaction['source_type']

            if card_method == "CARD":
                
                amount = transaction['amount']['amount']

                year = transaction['posted_at'][:7]

                if not year in hashmap.keys():
                    hashmap[year] = 0

                hashmap[year]+= amount

                if hashmap[year] > bigger_value:
                    bigger_value = hashmap[year]
                    solution = year

    print(solution)
    print(bigger_value)
    print(json.dumps(hashmap,indent=4))

handler()
