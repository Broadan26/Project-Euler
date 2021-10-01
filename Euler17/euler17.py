import time
import requests

def example(num: int):
    '''Testing before hammering the API endpoint'''
    num_to_find = str(num)
    request = 'https://api.funtranslations.com/translate/numbers.json?text=' + num_to_find
    response = requests.get(request)
    jsonResponse = response.json()
    number = str(jsonResponse["contents"]["translated"])
    number.replace('-', '')
    number.replace(' ', '')
    print(number)

def euler17(limit: int) -> int:
    answer = 0
    for num in range(limit, 0, -1):
        try:
            num_to_find = str(num)
            request = 'https://api.funtranslations.com/translate/numbers.json?text=' + num_to_find
            response = requests.get(request)
            response.raise_for_status()
            jsonResponse = response.json()
            number = str(jsonResponse["contents"]["translated"])

            number.replace('-', '')
            number.replace(' ', '')
            answer += len(number)

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
    return answer

def main():
    limit = 1000

    start = time.time()
    length_of_nums = euler17(limit) # 21124
    print(f'Character length of first {limit} numbers is = {length_of_nums}')
    end = time.time()
    print('Time Elapsed:', end - start)

if __name__ == "__main__":
    main()
