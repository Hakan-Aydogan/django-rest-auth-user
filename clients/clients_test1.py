import requests


def client():

    credentials = {
        'username': 'Doan',
        'password': '123456_A',
    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/login/',
        data=credentials,
    )

    print('status code', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
