# dialect-copa-zero

## Zero-shot

Results on the train section of the data by zero-shotting with the following prompt (example in Croatian):

```
You will be given a task. The task definition is in English, but the task itself is in another language. Here is the task!
Given the premise "Dječak je imao problema sa zakopčavanjem svoje košulje.", and that we are looking for the result of this premise, which hypothesis is more plausible?
Hypothesis 1: "Nije htio nositi košulju.".
Hypothesis 2: "Tražio je svoju majku da mu pomogne.".
Answer only with "1" or "2".
Answer: 
```

| system | avg | copa-en.train | copa-hr.train | copa-mk.train | copa-mk.train.trans | copa-sl-cer.train | copa-sl.train | copa-sr-tor.train | copa-sr-tor.train.trans | copa-sr.train | copa-sr.train.trans |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bigscience/mt0-xxl | | 0.89 | 0.738 | 0.838 | 0.782 | 0.54 | 0.787 | 0.78 | 0.713 | 0.828 | 0.765 |
| CohereForAI/aya-101 | | 0.808 | 0.645 | 0.72 | 0.63 | 0.53 | 0.728 | 0.69 | 0.623 | 0.745 | 0.665 |
| gpt-3.5-turbo-0125 | | 0.923 | 0.843 | 0.733 | 0.713 | 0.535 | 0.79 | 0.715 | 0.772 | 0.795 | 0.825 |
| gpt-4-0125-preview | | 0.988 | 0.963 | 0.945 | 0.9 | 0.608 | 0.96 | 0.92 | 0.912 | 0.955 | 0.96 |
| meta-llama/Llama-2-7b-chat-hf | | 0.533 | 0.152 | 0.035 | 0.033 | 0.02 | 0.175 | 0.043 | 0.09 | 0.095 | 0.145 |
| mistral/Mistral-7B-Instruct-v0.1 | 0.52 | 0.652 | 0.507 | 0.502 | 0.497 | 0.487 | 0.507 | 0.502 | 0.5 | 0.525 | 0.515 |
| mistral/Mistral-7B-Instruct-v0.2 | 0.508 | 0.723 | 0.542 | 0.497 | 0.448 | 0.285 | 0.515 | 0.507 | 0.487 | 0.542 | 0.537 |
| mistral/Mixtral-8x7B-Instruct-v0.1 | 0.67 | 0.875 | 0.705 | 0.665 | 0.632 | 0.405 | 0.682 | 0.68 | 0.637 | 0.71 | 0.713 |
| tiiuae/falcon-7b-instruct | | 0.49 | 0.463 | 0.357 | 0.515 | 0.485 | 0.5 | 0.398 | 0.51 | 0.407 | 0.458 |

Note on bad `meta-llama/Llama-2-7b-chat-hf` performance, but also other models on hard tasks such as sl-cer: it is often indecisive (gives no concrete answer), which is considered an incorrect answer, therefore has accuracy lower than 0.5 (random baseline).

Lack of clear response by model and dataset is the following.

| system | copa-en.train | copa-hr.train | copa-mk.train | copa-mk.train.trans | copa-sl-cer.train | copa-sl.train | copa-sr-tor.train | copa-sr-tor.train.trans | copa-sr.train | copa-sr.train.trans |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bigscience/mt0-xxl | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| CohereForAI/aya-101 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| gpt-3.5-turbo-0125 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| gpt-4-0125-preview | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| meta-llama/Llama-2-7b-chat-hf | 0.105 | 0.735 | 0.927 | 0.895 | 0.95 | 0.665 | 0.905 | 0.835 | 0.807 | 0.667 |
| mistral/Mistral-7B-Instruct-v0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| mistral/Mistral-7B-Instruct-v0.2 | 0.028 | 0.05 | 0.072 | 0.14 | 0.42 | 0.052 | 0.065 | 0.07 | 0.035 | 0.043 |
| mistral/Mixtral-8x7B-Instruct-v0.1 | 0.018 | 0.01 | 0.013 | 0.028 | 0.122 | 0.01 | 0.013 | 0.02 | 0.015 | 0.015 |
| tiiuae/falcon-7b-instruct | 0.02 | 0.052 | 0.3 | 0.033 | 0.072 | 0.05 | 0.18 | 0.035 | 0.172 | 0.075 |

## Few-shot

Results on the train section of the data, on models where improvement is observed when 4-shotting with the following prompt (example in Croatian):

```
You will be given a task. The task definition is in English, but the task itself is in another language. Answer only with "1" or "2". Here are some examples of the task:
Example 1:
Premise: "Čovek odvrnuja slavinu."
Question: "effect"
Hypothesis 1: "Ve-ce se napunija sas vodu."
Hypothesis 2: "Voda ističala od slavinu."
Answer: "2"

Example 2:
Premise: "Devojčica našla bubaljku među njojne žitarice."
Question: "effect"
Hypothesis 1: "Sipala mleko u činiju."
Hypothesis 2: "Izgubila si apetit."
Answer: "2"

Example 3:
Premise: "Žena otišla u penziju."
Question: "effect"
Hypothesis 1: "Primila si penziju."
Hypothesis 2: "Otplatila si hipoteku."
Answer: "1"

Example 4:
Premise: "Teja sam si ušparam struju."
Question: "effect"
Hypothesis 1: "Pomeja sam patos u praznu sobu."
Hypothesis 2: "Ugasija sam svetlo u praznu sobu."
Answer: "2"

Now to your task!
Premise: "Devojka zamislila želju."
Question: "cause"
Hypothesis 1: "Videla crnu mačku."
Hypothesis 2: "Videla zvezdu padalicu."
Answer: 
```

| system | N-shot | avg |  copa-en.train | copa-hr.train | copa-mk.train | copa-mk.train.trans | copa-sl-cer.train | copa-sl.train | copa-sr-tor.train | copa-sr-tor.train.trans | copa-sr.train | copa-sr.train.trans |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mistral/Mistral-7B-Instruct-v0.1 | 0 | 0.52 | 0.652 | 0.507 | 0.502 | 0.497 | 0.487 | 0.507 | 0.502 | 0.5 | 0.525 | 0.515 |
| mistral/Mistral-7B-Instruct-v0.1 | 4 | 0.59 | 0.745 | 0.593 | 0.578 | 0.56 | 0.527 | 0.598 | 0.565 | 0.542 | 0.603 | 0.595 |
| mistral/Mistral-7B-Instruct-v0.2 | 0 | 0.508 | 0.723 | 0.542 | 0.497 | 0.448 | 0.285 | 0.515 | 0.507 | 0.487 | 0.542 | 0.537 |
| mistral/Mistral-7B-Instruct-v0.2 | 4 | 0.7 | 0.938 | 0.718 | 0.688 | 0.647 | 0.515 | 0.738 | 0.65 | 0.63 | 0.738 | 0.743 |
| mistral/Mistral-7B-Instruct-v0.2 | 10 | 0.708 | 0.925 | 0.757 | 0.708 | 0.665 | 0.507 | 0.718 | 0.667 | 0.632 | 0.75 | 0.752 |
| mistral/Mixtral-8x7B-Instruct-v0.1 | 0 | 0.67 | 0.875 | 0.705 | 0.665 | 0.632 | 0.405 | 0.682 | 0.68 | 0.637 | 0.71 | 0.713 |
| mistral/Mixtral-8x7B-Instruct-v0.1 | 4 | 0.745 | 0.927 | 0.797 | 0.705 | 0.718 | 0.487 | 0.777 | 0.713 | 0.73 | 0.807 | 0.785 |
| mistral/Mixtral-8x7B-Instruct-v0.1 | 10 | 0.755 | 0.932 | 0.818 | 0.703 | 0.682 | 0.5 | 0.802 | 0.723 | 0.748 | 0.848 | 0.795 |
| mistral/Mixtral-8x7B-Instruct-v0.1 | 20 | 0.76 | 0.95 | 0.805 | 0.735 | 0.693 | 0.555 | 0.792 | 0.713 | 0.713 | 0.845 | 0.802 |

