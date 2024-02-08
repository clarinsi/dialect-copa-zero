import json
import argparse
from openai import OpenAI
import os

client = OpenAI(api_key="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")
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')
parser.add_argument('-o', '--output')
parser.add_argument('-m', '--model')
parser.add_argument('-s', '--sleep', default=2)
args = parser.parse_args()

open(os.path.join(args.model,args.output+'.args'),'w').write(json.dumps(args.__dict__, indent=4))

from time import sleep
try:
    responses=json.load(open(os.path.join(args.model,args.output)))
except:
    responses=[]
for line in open(args.input):
    entry=json.loads(line)
    if len(responses)>=entry['idx']+1:
        print('skipping')
        continue
    print(entry['idx'])
    prompt='Given the premise "'+entry['premise']+'",'
    if entry['question']=='cause':
        prompt+=' and that we are looking for the cause of this premise,'
    else:
        prompt+=' and that we are looking for the result of this premise,'
    prompt+=' which hypothesis seems more plausible?\nHypothesis 1: "'+entry['choice1']+'".\nHypothesis 2: "'+entry['choice2']+'".\nPlease answer only with "1" or "2".'
    print(prompt)
    completion = client.chat.completions.create(model=args.model,
    messages=[
    {
        "role": "user",
        "content": prompt}
    ],
    temperature = 0)
    response=completion.choices[0].message.content
    responses.append(response)
    print(response)
    json.dump(responses,open(os.path.join(args.model,args.output),'wt'))
    sleep(args.sleep)
