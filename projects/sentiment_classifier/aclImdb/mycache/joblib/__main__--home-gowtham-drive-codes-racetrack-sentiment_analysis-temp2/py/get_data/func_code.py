# first line: 16
@mem.cache
def get_data():
    for filename in glob.glob("/home/gowtham/drive/codes/racetrack/sentiment_analysis/aclImdb/train/pos"+'*.txt'):
        count_vect.transform(filename)
