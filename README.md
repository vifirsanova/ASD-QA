# ASD-QA

Autism Spectrum Disorder QA (ASD QA) supports the inclusion of people with special needs. First of all, it is a QA dataset in the Russian language for the inclusion of people with autism spectrum disorder (ASD) and Asperger syndrome in particular. The dataset is based on the data from [the informational website](https://aspergers.ru). The usage of the data is agreed.


## Results obtained on [the project dataset](https://doi.org/10.6084/m9.figshare.13295831)

|Base model | F-Score |
|-----------|---------|
|[Multilingual BERT](https://github.com/google-research/bert/blob/master/multilingual.md) | 0.55 |
|[774M GPT-2](https://github.com/openai/gpt-2) | 0.63 |

## Sample outputs (Russian)

**BERT based model**

**Q:** Каковы социальные черты синдрома Аспергера? 

**A:** Некоторые люди полагают, что синдром Аспергера не более чем иной "способ мышления", то есть вариант нормы.

**GPT-2 based model**

**Q:** Отличается ли у аутистов мировосприятие? 

**A:** Некоторые станут утверждать, что несомненно да.
