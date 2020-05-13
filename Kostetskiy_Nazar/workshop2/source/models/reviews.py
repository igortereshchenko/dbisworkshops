import logging
import pickle

from .fixtures import UserReview1


class Reviews:
    def __init__(self):
        self.data = self.initialize()

    def initialize(self):
        data = self.loads()
        if data is not None:
            return data
        else:
            self.save(UserReview1)
            return UserReview1

    def set_data(self, **data):
        for k, v in data:
            if k in self.data:
                self.data[k] = v
        return self.data

    @staticmethod
    def save(data):
        with open('temp/reviews_data.pickle', 'wb') as f:
            pickle.dump(data, f)
        return data

    @staticmethod
    def loads():
        try:
            f = open("temp/reviews_data.pickle", "rb")
            # Do something with the file
        except FileNotFoundError:
            logging.warning('file reviews_data does not exists')
        else:
            data = pickle.load(f)
            f.close()
            return data
