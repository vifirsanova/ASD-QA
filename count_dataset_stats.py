import json
from pathlib import Path

import statistics

path_orig, path_short = Path('original.json'), Path('short.json')
data_orig, data_short = json.loads(path_orig.read_text(encoding='utf-8')), json.loads(path_short.read_text(encoding='utf-8'))

orig_q = []
orig_a = []
short_q = []
short_a = []

def listing(data, list_q, list_a):

  for item in data['data']:
    for paragraph in item['paragraphs']:
      for qa in paragraph['qas']:
        list_q.append(qa['question'])
        list_a.append(qa['answers'][0]['text'])
  
  return list_q, list_a

orig_q, orig_a  = listing(data_orig, orig_q, orig_a)
short_q, short_a = listing(data_short, short_q, short_a)

def avg_symbols(strings):
  return round(sum(map(len, strings)) / len(strings))

def avg_tokens(strings):
  return round(statistics.mean([len(token) for token in [element.split() for element in strings]]))

print('Average number of symbols in answers')
print('Original dataset version', avg_symbols(orig_a))
print('Shortened dataset version', avg_symbols(short_a))

print('\nAverage number of tokens in answers')
print('Original dataset version', avg_tokens(orig_a))
print('Shortened dataset version', avg_tokens(short_a))
