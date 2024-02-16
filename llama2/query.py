import json
import argparse
import sys
sys.path.append('../')
from prompt_definition import construct_prompt


from transformers import AutoTokenizer
import transformers
import torch

model = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

import json

import os

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
    prompt=construct_prompt(entry)#.replace(', but the task itself is in another language','')
    print(prompt)
    response = pipeline(
    '<s>[INST] '+prompt+ ' [/INST]',
    #do_sample=False,
    #top_k=1,
    #num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,)
    
    print(response[0]['generated_text'])
    responses.append(response[0]['generated_text'])
    json.dump(responses,open(os.path.join(args.model,args.output),'wt'))
    sleep(int(args.sleep))
