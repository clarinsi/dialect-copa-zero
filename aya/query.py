import json
import argparse

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import json
import os,sys
sys.path.append('../')
from prompt_definition import construct_prompt
checkpoint = "CohereForAI/aya-101"


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

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint, torch_dtype="auto", device_map="auto", load_in_8bit=True)


for line in open(args.input):
    entry=json.loads(line)
    if len(responses)>=entry['idx']+1:
        print('skipping')
        continue
    print(entry['idx'])
    prompt=construct_prompt(entry)
    print(prompt)
    inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs)
    response=tokenizer.decode(outputs[0])
    print(response)
    responses.append(response)
    json.dump(responses,open(os.path.join(args.model,args.output),'wt'))
    sleep(int(args.sleep))
