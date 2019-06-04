import numpy as np
import re
import pandas as pd
from KaggleWord2VecUtility import KaggleWord2VecUtility


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels(positive_data_file, negative_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    positive_examples = list(open(positive_data_file, "r", encoding='utf-8').readlines())
    positive_examples = [s.strip() for s in positive_examples]
    negative_examples = list(open(negative_data_file, "r", encoding='utf-8').readlines())
    negative_examples = [s.strip() for s in negative_examples]
    # Split by words
    x_text = positive_examples + negative_examples
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    positive_labels = [[0, 1] for _ in positive_examples]
    negative_labels = [[1, 0] for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels], 0)
    return [x_text, y]

def load_data_and_labels_kaggle(test_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    y=[]
    # Load data from files
    test_examples = pd.read_csv(test_data_file, 
                    header=0, delimiter='\t', quoting=3)
    # Generate labels
    for x in test_examples["sentiment"]:
        if x == 1 : #positive
            test_labels = [1]
        else : #negative
            test_labels = [0]
        y = np.concatenate([y,test_labels], 0)
    print(y)
    print(y.shape)
    print("sentiment complete")
    #print(test_examples["review"][:10])
    # preprocessing
    sentences = []
    for review in test_examples["review"]:
        tmpstr = KaggleWord2VecUtility.review_to_corpus(review, remove_stopwords=False)
        sentences.append(tmpstr)
<<<<<<< HEAD
    
    print("preprocessing complete")
    return [sentences, y]

def load_data_and_labels_kaggle2(test_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    y=[]
    # Load data from files
    training_examples = pd.read_csv(test_data_file, 
                    header=0, delimiter='\t', quoting=3)
    # Generate labels
    for x in training_examples["Sentiment"]:
        if x == 1 : #positive
            test_labels = [1]
        else : #negative
            test_labels = [0]
        y = np.concatenate([y,test_labels], 0)
    print(y)
    print(y.shape)
    print("sentiment complete")
    #print(test_examples["review"][:10])
    # preprocessing
    sentences = []
    for review in test_examples["review"]:
        tmpstr = KaggleWord2VecUtility.review_to_corpus(review, remove_stopwords=False)
        sentences.append(tmpstr)
=======
>>>>>>> 1aedca2954e328bef692d8e5700c94088fdfc225
    
    print("preprocessing complete")
    return [sentences, y]

def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
