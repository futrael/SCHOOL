import pickle

def watch():
    with open('data.pickle', 'rb') as f:
        data_new = pickle.load(f)
        return data_new

def load(data):
    data.update(watch())
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)