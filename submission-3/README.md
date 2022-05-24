
# Cross-lingual sense disambiguation

The repository consists of corpus files and program code files.


***data*** folder contains the following files:

|name|description  |
|--|--|
| *auto-annotated.csv* | Presents hand-annotated examples of sentences with different or identical meanings. |
| *corpus-annotated.csv* | Presents auto classified examples of sentences with different or identical meanings. |
| *corpus.csv* | Presents a complete collection of words and examples of their use in pairs of sentences. |



The other files are:

|name|description  |
|--|--|
| *mask_classifier.py* | Represents an implementation of sentence classification by masking |
| *bert-classifier.ipynb* | Compares the meaning of the sentences according to the common word in the two sentences. |
| *bert-classifier-whole-sentences.ipynb* | Represents a comparison of complete sentence contexts against each other. |


> We propose to run ipynb files in the Google Colab environment.



