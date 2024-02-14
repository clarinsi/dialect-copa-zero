import json
import argparse

from transformers import AutoModelForCausalLM, AutoTokenizer
import json

import os

import sys
sys.path.append('../')
from prompt_definition import construct_prompt

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

model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

#tokenizer = AutoTokenizer.from_pretrained(checkpoint)
#model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint, torch_dtype="auto", device_map="auto", load_in_8bit=True)


for line in open(args.input):
    entry=json.loads(line)
    if len(responses)>=entry['idx']+1:
        print('skipping')
        continue
    print(entry['idx'])
    prompt=construct_prompt(entry)
    #prompt+=' which hypothesis seems more plausible?\nHypothesis 1: "'+entry['choice1']+'".\nHypothesis 2: "'+entry['choice2']+'".\nIt is of paramount importance to anwer only with "1" or "2".'
    print(prompt)
    #inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    messages = [
    {"role": "user", "content": prompt},
    ]
    encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")
    #prompt = "<s>[INST]"+prompt+"[/INST]"
    #encodeds = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
    model_inputs = encodeds.to("cuda")
    model.to("cuda")
    generated_ids = model.generate(model_inputs, max_new_tokens=100, do_sample=False, bos_token_id=model.config.bos_token_id,
                                eos_token_id=model.config.eos_token_id,
                                pad_token_id=model.config.eos_token_id)
    decoded = tokenizer.batch_decode(generated_ids)
    print(decoded[0])
    response=decoded[0]
    #outputs = model.generate(inputs)
    #response=tokenizer.decode(outputs[0])
    #print(response)
    responses.append(response)
    json.dump(responses,open(os.path.join(args.model,args.output),'wt'))
    sleep(int(args.sleep))
