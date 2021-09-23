# Importing the pickle library

import pickle

# Dumping the model object to save it as model.pkl file

pickle.dump(model, open('knnModel.pkl', 'wb+'))