import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text_file, result_file, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    with open(text_file, encoding="utf8") as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}'
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(result_file, 'w', encoding="utf8") as f:
        f.write(''.join(json_['text']))


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))


if __name__ == '__main__':
    print(translate_it(text_file='DE.txt', result_file='done/DE-RU.txt', from_lang='de', to_lang='ru'))
    print(translate_it(text_file='ES.txt', result_file='done/ES-RU.txt', from_lang='es', to_lang='ru'))
    print(translate_it(text_file='FR.txt', result_file='done/FR-RU.txt', from_lang='fr', to_lang='ru'))
