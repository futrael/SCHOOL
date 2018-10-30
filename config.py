import pickle


token = '558134598:AAHuA7FRrQrY5_7hbMbLLw2kQcPh9LMTSxs'


def look(userid):
    with open('data.pickle', 'rb') as f:
        data_new = pickle.load(f)
        print()
        return data_new.get(str(userid))


def watch():
    with open('data.pickle', 'rb') as f:
        data_new = pickle.load(f)
        return data_new


def load(data):
    data_new = watch()
    data_new.update(data)
    with open('data.pickle', 'wb') as f:
        pickle.dump(data_new, f)


if __name__ == "__main__":
    load({'test': ['nastyajessy', 'knfalis4']})
    print(watch())
