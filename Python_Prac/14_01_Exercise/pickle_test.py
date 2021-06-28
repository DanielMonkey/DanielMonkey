import pickle
t1 = [1, 2, 3]
s = pickle.dumps(t1)
print(s)
t2 = pickle.loads(s)
print(t2)
print(t1 == t2)
print(t1 is t2)



