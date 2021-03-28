import json

SNAKES_CONFIG = './resources/snakes_config.json'
LADDERS_CONFIG = './resources/ladders_config.json'


def load_json(file_to_read):
    """
    Reads a json file and returns its content.
    :param file_to_read:
    :return: None if file read fails, else file contents.
    """
    data = None
    with open(file_to_read) as fp:
        data = json.load(fp)
    return data


def get_snakes_config():
    return load_json(SNAKES_CONFIG)


def get_ladders_config():
    return load_json(LADDERS_CONFIG)


if __name__ == '__main__':

    # Read snake and ladder configurations
    snakes_config = get_snakes_config()
    print(snakes_config)

    ladders_config = get_ladders_config()
    print(ladders_config)
