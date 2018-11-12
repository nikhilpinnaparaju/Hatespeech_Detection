from stanfordcorenlp import StanfordCoreNLP
import logging
import json
import string

class StanfordNLP:
    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

if __name__ == '__main__':
    sNLP = StanfordNLP()

    f = open('./hatespeech_features.csv','r')
    g = open('../hate_resource/hatedata.TD_RvNN.txt','w+')

    f.readline()

    count = 0

    while(1):

        curline = f.readline()

        if not curline:
            break

        data = curline.split(',',2)
        try:
            tid = int(data[0])
            text = data[1]

            table = str.maketrans('', '', string.punctuation)

            text = text.translate(table)

            tokens = sNLP.word_tokenize(text)
            dep_parse = sNLP.dependency_parse(text)

            parents = {}
            for triple in dep_parse:
                if triple[1]:
                    parents[triple[2]] = triple[1]
                else:
                    parents[triple[2]] = None
                # print(triple[2],tokens[triple[2]-1])

            # print(parents)
            par_pointers = [None,]
            for key in parents:
                par_pointers.append(parents[key])
            
            print(par_pointers)

# -----------------------------------------------------------------

            root = -1
            maxlen = -1

            for i in range(1,len(par_pointers)):
                if par_pointers[i] == None:
                    root = i

                if len(tokens[i-1]) > maxlen:
                    maxlen = len(tokens[i-1])
                    # print(tokens[i-1])

            for i in range(1,len(par_pointers)):
                
                par = par_pointers[i]
                cur = i
                npar = len(set(par_pointers))
                
                # to_write = 'ok\n'
                to_write = str(tid)+'\t'+str(par)+'\t'+str(cur)+'\t'+str(npar)+'\t'+str(maxlen)+'\t'+tokens[cur-1].lower()+'\n'
                g.write(to_write)
                # print(tid,'\t',par,'\t',cur,'\t',npar,'\t',maxlen,'\t',tokens[cur-1].lower(),'\n')

        except Exception as e:
            # print(e)
            continue