a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


words = a_text.lower()


sep_words = words.split()   

word_num_pair = {}

for word in sep_words:
    if word in word_num_pair:
        word_num_pair[word] += 1
    else:
        word_num_pair[word] = 1
        
print( word_num_pair)
