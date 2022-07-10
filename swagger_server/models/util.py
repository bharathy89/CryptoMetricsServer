import os

import pymongo


def get_db():
    """
    get the mongodb Client
    :return: mongodb client
    """
    db_name = os.environ["MONGODB_DATABASE"]
    uri = (
        "mongodb://"
        + os.environ["MONGODB_USERNAME"]
        + ":"
        + os.environ["MONGODB_PASSWORD"]
        + "@"
        + os.environ["MONGODB_HOSTNAME"]
        + ":27017/"
        + os.environ["MONGODB_DATABASE"]
        + "?authSource=admin&retryWrites=true&w=majority"
    )
    client = pymongo.MongoClient(uri)
    db = client[db_name]
    return db
