import pickle

with open('hw1.pkl', 'rb') as f:
    model = pickle.load(f)

X_test = [[1, 1, 1, 21.121217366373163]]
y_pred = model.predict(X_test)
print(y_pred)