f = open('./hatespeech_features.csv','r')
g = open('./datasetSentences.txt','w+')
h = open('./tweetid2sentence.txt','w+')
i = open('./datasetSplit.txt','w+')

f.readline()
count = 1

string = 'sentence_index\tsentence\n'
g.write(string)

string = 'sentence_index\ttweet_id\n'
h.write(string)

string = 'sentence_index,splitset_label\n'
i.write(string)

while(1):

    curline = f.readline()

    if not curline:
        break

    data = curline.split(',',2)
    
    try:
        tid = int(data[0])
        # print(data[1])
        string = str(count)+'\t'+data[1].strip()+'\n'
        g.write(string)

        string = str(count)+'\t'+data[0].strip()+'\n'
        h.write(string)

        if count < 75000:
            string = str(count)+',1\n'
            i.write(string)

        elif count<80000:
            string = str(count)+',2\n'
            i.write(string)

        elif count<100000:
            string = str(count)+',3\n'
            i.write(string)    

        count += 1

    except:
        continue

g.close()
f.close()
h.close()
i.close()