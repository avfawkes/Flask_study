import requests

if __name__ == '__main__':
    num = int(input('Введи num: '))
    response = requests.post('http://localhost:5000/add', json={'num': num})

    print(response.status_code, response.json())

    if response.status_code == 200:
        print(response.json()['result'])
    else:
        print(response.text)
