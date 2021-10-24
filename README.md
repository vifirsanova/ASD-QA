# ASD-QA

Autism Spectrum Disorder QA (ASD QA) supports the inclusion of people with special needs. First of all, it is a QA dataset in the Russian language for the inclusion of people with autism spectrum disorder (ASD) and Asperger syndrome in particular. The dataset is based on the data from [the informational website](https://aspergers.ru). The usage of the data is agreed.


## Example of results obtained on [the project dataset](https://doi.org/10.6084/m9.figshare.13295831)

Results may vary according to the dataset settings and model parameters.

|Base model | F-Score | Exact Match |
|-----------|---------|---------|
|[XLM-RoBERTa](https://huggingface.co/transformers/model_doc/xlmroberta.html) | 0.48 | 0.39 |
|[Multilingual BERT](https://github.com/google-research/bert/blob/master/multilingual.md) | 0.40 | 0.29 |
|[Multilingual DistilBERT](https://huggingface.co/distilbert-base-multilingual-cased)| 0.42 | 0.32 |
|[Russian BERT (Geotrend)](https://huggingface.co/Geotrend/bert-base-ru-cased)| 0.39 | 0.30 |
|[774M GPT-2](https://github.com/openai/gpt-2) | 0.63 | 0.52 |
|[117M GPT-2](https://github.com/openai/gpt-2) | 0.53 | 0.43 |

## Sample outputs (Russian)

**BERT based model**

**Q:** Каковы социальные черты синдрома Аспергера? 

**A:** Некоторые люди полагают, что синдром Аспергера не более чем иной "способ мышления", то есть вариант нормы.

**GPT-2 based model**

**Q:** Отличается ли у аутистов мировосприятие? 

**A:** Некоторые станут утверждать, что несомненно да.
