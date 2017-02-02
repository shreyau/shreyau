import pickle

f = open('picle1.txt','r')
my_list = pickle.load(f)
my_dict = pickle.load(f)
my_str = pickle.load(f)
print my_list
print my_dict
print my_str

