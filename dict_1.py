#dict_1.py
#enter words and its synonyms manually into dictionary
#take input from user and check if the word is present in the dictionary
#if present retreive the synonyms of the word else add the word and its synonym into the dictionary

dict1={}
class Dict1:
 def __init__(self,dict1):
    self.dict1={'amazing':'incredible, unbelievable,fabulous','Awful':'dreadful, terrible','Brave':'courageous,fearless','Crooked':' bent,    twisted,curved','Decide':'determine, settle, choose','Explain':'elaborate, clarify'}

 def find_word(self):
  #print dict1
  inp=raw_input("enter the key to search :")
  if inp in self.dict1:
    #print "*****"
    print self.dict1[inp]
  else:
    print "Word not present in dictionary :"
    val=raw_input("enter the synonyms of the word :")
    self.dict1[inp] = val
    print self.dict1
    a.find_word()

a=Dict1(dict1)
a.find_word()
