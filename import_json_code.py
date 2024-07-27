import json

from core.application.models import Joke
from core.settings import BASE_DIR


def import_json_data():
    file = open(BASE_DIR / 'jokes.json', 'r')
    joke_dict = json.load(file)

    for joke_ in joke_dict:
        new_joke = Joke(
            setup=joke_['setup'], punch_line=joke_['punchline'], joke_type=joke_['type']
        )
        new_joke.save()


if __name__ == '__main__':
    import_json_data()
