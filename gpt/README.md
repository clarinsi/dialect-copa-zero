python query.py -i ../dialect-copa/copa-sr-tor/train.jsonl -o copa-sr-tor.train.jsonl -m gpt-3.5-turbo-0125
python query.py -i ../dialect-copa/copa-sr-tor/train.trans.jsonl -o copa-sr-tor.train.trans.jsonl -m gpt-3.5-turbo-0125
python eval.py -a gpt-3.5-turbo-0125/copa-sr-tor.train.jsonl.args