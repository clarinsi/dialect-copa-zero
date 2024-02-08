import json
import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--argfile')
#parser.add_argument('-o', '--output')
#parser.add_argument('-m', '--model')
#parser.add_argument('-s', '--sleep', default=2)
args = parser.parse_args()
argdict=json.load(open(args.argfile))
responses=json.load(open(os.path.join(argdict['model'],argdict['output'])))
from collections import Counter
truth=[]
clear=[]
for line in open(argdict['input']):
    entry=json.loads(line)
    #print(entry['idx'])
    #print(responses[entry['idx']])
    #if len(responses)==entry['idx']:
    #    break
    try:
        label=int(responses[entry['idx']])-1
    except:
        truth.append(False)
        clear.append(False)
        continue
    truth.append(entry['label']==label)
    clear.append(True)
truth=Counter(truth)
clear=Counter(clear)
print(truth)
print(clear)
print(sum(clear.values()))
print('accuracy',truth[True]/sum(truth.values()))
print('lack of response',clear[False]/sum(clear.values()))
print(str(truth[True]/sum(truth.values()))+'\t'+str(truth[True]/clear[True])+'\t'+str(clear[False]/sum(clear.values())))
