f = open('./tweetid2sentence.txt','r')
g = open('../hate_nfold/RNNtrainSet_hate0_tree.txt','w+')
h = open('../hate_nfold/RNNtestSet_hate0_tree.txt','w+')
i = open('../hate_resource/hate_label_All.txt','w+')

f.readline()

count = 0 

while(1):

    curline = f.readline()

    if not curline:
        break
    
    data = curline.split('\t')

    if count < 80000:
        g.write(data[1])
    
    else:
        h.write(data[1])

    count += 1

f.close()
g.close()
h.close()
i.close()
