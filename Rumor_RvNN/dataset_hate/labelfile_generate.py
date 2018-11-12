import pandas as pd

csvfile = pd.read_csv('./hatespeech_labels.csv')

f = open('../hate_resource/hate_label_All.txt','w+')

for index, row in csvfile.iterrows():
    # print(row['tweet_id'])
    string = row['label']+'\t'+'data'+'\t'+str(row['tweet_id'])+'\n'
    f.write(string)

f.close()