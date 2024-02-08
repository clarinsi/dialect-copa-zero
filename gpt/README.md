
## gpt-3.5-turbo-0125

| copa-hr.train | copa-mk.train | copa-mk.train.trans | copa-sl-cer.train | copa-sl.train | copa-sr-tor.train | copa-sr-tor.train.trans | copa-sr.train | copa-sr.train.trans |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.843 | 0.733 | 0.713 | 0.535 | 0.79 | 0.715 | 0.772 | 0.795 | 0.825 |

## gpt-4-0125-preview

| copa-hr.train | copa-mk.train | copa-mk.train.trans | copa-sl-cer.train | copa-sl.train | copa-sr-tor.train | copa-sr-tor.train.trans | copa-sr.train | copa-sr.train.trans |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.963 | 0.945 | 0.9 | 0.608 | 0.96 | 0.92 | 0.912 | 0.955 | 0.96 |

```
python query.py -i ../dialect-copa/copa-sr-tor/train.jsonl -o copa-sr-tor.train.jsonl -m gpt-3.5-turbo-0125
python eval.py gpt-3.5-turbo-0125/copa-sr-tor.train.jsonl.args # for eval of a single dataset
python eval.py gpt-3.5-turbo-0125 -a # for all datasets eval
```