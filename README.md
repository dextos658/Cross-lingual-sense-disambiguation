# Cross-lingual sense disambiguation

The repository is used for the development of the project **Cross-lingual sense disambiguation** in the course **Natural Language Processing** in the academic year 2021/2022 at the Faculty of Computer Science and Informatics, University of Ljubljana.

Authors: Zala Erič, Miha Debenjak, Denis Derenda Cizel

Advisor: Slavko Žitnik

# About the project

In human language, the same word can have different meanings depending on its intended use in a sentence. In the context of natural language processing, word sense discrimination can be described as the ability to determine the meaning of a word used in a given sentence or context.

For example, consider the two examples of the distinct sense that exist for the word **_“bass”_**:

-   I can hear bass /*frequency sound*.
-   He likes to eat grilled bass /*fish*.

Our goal is to prepare a solution that will be able to determine if the word X is used in the same context or not in 2 different sentences. This can be achieved by using different methods: Supervised Machine Learning, Semi-Supervised Learning, Dictionary Methods …

## ✅ Submission 1

We started by defining our group and choosing our area of work. We then checked the scope of work, looked for articles containing similar work and came up with an initial idea for the project. Find out more in the report.

## ✅ Submission 2

From the CVJT synonym dictionary (https://viri.cjvt.si/sopomenke/eng/) , which we obtained in xml format from the clarin.si website, we obtained a list of words  should have multiple meanings. To start with, we have chosen 2000 different words that we expect to have multiple meanings. Then, for about 500 words, we extracted 10 uses in sentences for each of them. This data is extracted through an AP interface provided by the sketchengine.eu website, which hosts SLOVENIAN WEB (SLWAC 2.1) corpus, which holds 754 255 589 different words and 50 847 258 sentences. Thus, we have compiled a collection of words and their usages, which we will use to classify the meanings. We also examined different implementations of the BERT algorithm and which methods we would use to fine-tune it. We estimate that we will manually review 30% of the word usage comparisons.

## 🔜 Submission 3

/
