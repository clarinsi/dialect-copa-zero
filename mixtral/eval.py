import json
import sys
import argparse
import os
from collections import Counter

def count(argfile_path):
    argdict=json.load(open(argfile_path))
    responses_path=os.path.join(argdict['model'],argdict['output'])
    train_path=argdict['input']
    long_responses=json.load(open(responses_path))
    responses=[]
    for e in long_responses:
        e=e[e.find('[/INST]')+5:]
        one=e.find('1')
        two=e.find('2')
        if one!=-1 and two!=-1:
            if one<two:
                responses.append('1')
            else:
                responses.append('2')
        elif one!=-1:
            responses.append('1')
        elif two!=-1:
            responses.append('2')
        else:
            responses.append('ah')
    print(responses)
    truth=[]
    clear=[]
    for line in open(train_path):
        entry=json.loads(line)
        #print(entry['idx'])
        #print(responses[entry['idx']])
        if len(responses)==entry['idx']:
            print('INCOMPLETE OUTPUT')
            break
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
    return truth,clear,truth[True]/sum(truth.values()),clear[False]/sum(clear.values())

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('argfile')
    parser.add_argument('-t', '--table', action='store_true')
    parser.add_argument('-a', '--all', action='store_true')
    #parser.add_argument('-m', '--model')
    #parser.add_argument('-s', '--sleep', default=2)
    args = parser.parse_args()
    if args.all:
        model_path=args.argfile
        header=[]
        row=[]
        for file in sorted(os.listdir(model_path)):
            if file.endswith('.args'):
                header.append(file[:-11])
                _,_,a,l=count(os.path.join(model_path,file))
                row.append(a)
        print('| '+' | '.join(header)+' |')
        print('| '+' | '.join(['---' for e in header])+' |')
        print('| '+' | '.join([str(round(e,3)) for e in row])+' |')
    else:
        truth,clear,acc,lack=count(args.argfile)    
        if not args.table:
            print(truth)
            print(clear)
            print(sum(clear.values()))
            print('accuracy',acc)
            print('lack of response',lack)
            print(str(truth[True]/sum(truth.values()))+'\t'+str(truth[True]/clear[True])+'\t'+str(clear[False]/sum(clear.values())))
        else:
            print("%.3f | %.3f" % (truth[True]/sum(truth.values()),clear[False]/sum(clear.values())))