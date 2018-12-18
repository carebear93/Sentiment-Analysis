import collections
from collections import Counter

# Store Words in Array
wordcounts = []
# Count Unique Words
count = {}

# Access DataSet Sentences
with open('datasetSentences/datasetSentences.txt') as f:
    text = f.read()
    sentences = text.split('.')
    # Count Words
    c = collections.Counter(text.split())
    # Loop for Average Calculation
    for sentence in sentences:
        words = sentence.split(' ')
        # Loop counting Unique Words
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        wordcounts.append(len(words))
# Average word count is total word divided by length of word count
average_wordcount = sum(wordcounts)/len(wordcounts)

# Output
print "##########################################"
print "There are %d total words" %sum(c.values())
print "##########################################"
print "Size of vocabulary"
print len(count)
print "##########################################"
print "##########################################"
print "Overall Average Word Length Per Sentence:"
print average_wordcount
print "##########################################"
print "##########################################"
