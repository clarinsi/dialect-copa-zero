# dialect-copa-zero

Current results on the train section of the data by zero-shotting with the following prompt (example in Croatian):

```
You will be given a task. The task definition is in English, but the task itself is in another language. Here is the task!
Given the premise "Dječak je imao problema sa zakopčavanjem svoje košulje.", and that we are looking for the result of this premise, which hypothesis is more plausible?
Hypothesis 1: "Nije htio nositi košulju.".
Hypothesis 2: "Tražio je svoju majku da mu pomogne.".
Answer only with "1" or "2".
Answer: 
```

| system | copa-hr.train | copa-mk.train | copa-mk.train.trans | copa-sl-cer.train | copa-sl.train | copa-sr-tor.train | copa-sr-tor.train.trans | copa-sr.train | copa-sr.train.trans |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bigscience/mt0-xxl | 0.738 | 0.838 | 0.782 | 0.54 | 0.787 | 0.78 | 0.713 | 0.828 | 0.765 |
| CohereForAI/aya-101 | 0.645 | 0.72 | 0.63 | 0.53 | 0.728 | 0.69 | 0.623 | 0.745 | 0.665 |
| gpt-3.5-turbo-0125 | 0.843 | 0.733 | 0.713 | 0.535 | 0.79 | 0.715 | 0.772 | 0.795 | 0.825 |
| gpt-4-0125-preview | 0.963 | 0.945 | 0.9 | 0.608 | 0.96 | 0.92 | 0.912 | 0.955 | 0.96 |
| meta-llama/Llama-2-7b-chat-hf | 0.44 | - | 0.2 | — | 0.033 | 0.163 | 0.09 | 0.145 | - |
| mistral/Mistral-7B-Instruct-v0.1 | 0.507 | 0.502 | 0.497 | 0.487 | 0.507 | 0.502 | 0.5 | 0.525 | 0.515 |
| mistral/Mistral-7B-Instruct-v0.2 | 0.542 | 0.497 | 0.448 | 0.285 | 0.515 | 0.507 | 0.487 | 0.542 | 0.537 |
| mistral/Mixtral-8x7B-Instruct-v0.1 | 0.705 | 0.665 | 0.632 | 0.405 | 0.682 | 0.68 | 0.637 | 0.71 | 0.713 |

Note on bad `meta-llama/Llama-2-7b-chat-hf` performance: it is often indecisive (gives no concrete result), but even when responding, is slightly above the random baseline.
