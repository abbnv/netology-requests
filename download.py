import requests

API_KEY = 'AgAAAAAfQXwUAADLWz8QlvAb20NauE-TI0IDaCg'
URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

def download_on_disk(file, path):
    # загружаем файлы на диск
    headers = {'Authorization': f'OAuth {API_KEY}'}
    params = {
        'path': f'%2F{path}'

    }
    response = requests.get(URL, params=params, headers=headers)
    response = response.json()

    upload = requests.put(response.get('href'), data=file)
    print(upload)

    if upload.status_code == 201:
        print("Файл загружен")
    else:
        print("Ошибка")


if __name__ == '__main__':
    download_on_disk("FR-RU.txt", path='path')
