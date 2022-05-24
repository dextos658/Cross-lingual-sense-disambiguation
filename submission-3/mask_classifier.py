from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from scipy import spatial
import pandas as pd
import re


def get_index(dataframe):
    for index, row in dataframe.iterrows():
        res1 = re.sub(r'[^a-zA-ZČŠŽčšž\s]', '', row["sentence1"]).lower()
        # print(res1)
        dataframe.at[index, 'index1'] = res1.split(" ").index(row["word"])
        res2 = re.sub(r'[^a-zA-ZČŠŽčšž\s]', '', row["sentence2"]).lower()
        # print(res2)
        df.at[index, 'index2'] = res2.split(" ").index(row["word"])

    # dataframe = dataframe.drop("index", 1)
    # dataframe.to_csv("test3.csv", index=False, header=False)
    return dataframe


def add_mask(string, i):
    arr = string.split(" ")
    if bert == 'EMBEDDIA/sloberta':
        arr[i] = "<mask>"
    else:
        arr[i] = "[MASK]"
    return " ".join(arr)


def meaning_distance(sen1, sen2, n_words):
    unmask1 = unmasker(sen1, top_k=n_words)
    top_words1 = [unmask1[i]['token_str'] for i in range(len(unmask1))]

    unmask2 = unmasker(sen2, top_k=n_words)
    top_words2 = [unmask2[i]['token_str'] for i in range(len(unmask2))]

    sentences = [' '.join(list) for list in [top_words1, top_words2]]

    embeddings = model.encode(sentences)

    distance = spatial.distance.cosine(embeddings[0], embeddings[1])

    return distance


filename = "test2.csv"
colnames = ['word', 'same_meaning', 'sentence1', 'sentence2', 'index1', 'index2']
df = pd.read_csv(filename, names=colnames, header=None)
df = get_index(df)
df_copy = df.copy()

# False - only classify, True - Also calculate accuracy on preannotated data
annotated = False
bert = 'EMBEDDIA/sloberta' # EMBEDDIA/crosloengual-bert
unmasker = pipeline('fill-mask', model=bert)
model = SentenceTransformer('sentence-transformers/use-cmlm-multilingual')

for num_words in [5, 10, 15, 20]:
    for index, row in df_copy.iterrows():
        df_copy.at[index, 'sentence1'] = add_mask(row['sentence1'], row["index1"])
        df_copy.at[index, 'sentence2'] = add_mask(row['sentence2'], row["index2"])

    df['distance'] = df_copy.apply(lambda row: meaning_distance(row["sentence1"], row["sentence2"], num_words), axis=1)
    df.to_csv("distances" + str(num_words) + ".csv")

    # print(df['distance'])
    # means = df.groupby("same_meaning")['distance'].mean()
    # print(means)

    print("********************************\n" + str(num_words) + "\n********************************")
    for threshold in [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]:
        df['class'] = df.apply(lambda row: 1 if row["distance"] < threshold else 0, axis=1)

        df.to_csv("corpus-" + str(num_words) + "-" + str(threshold) + ".csv", index=False, header=False)

        if annotated:
            matches = {"00": 0, "01": 0, "10": 0, "11": 0}
            for index, row in df.iterrows():
                if row["same_meaning"] == 1 and row["class"] == 1:
                    matches["11"] += 1
                elif row["same_meaning"] == 0 and row["class"] == 1:
                    matches["01"] += 1
                elif row["same_meaning"] == 1 and row["class"] == 0:
                    matches["10"] += 1
                else:
                    matches["00"] += 1

            print("Threshold: " + str(threshold))
            # recall = matches["00"] / (matches["00"] + matches["01"])
            # precision = matches["00"] / (matches["00"] + matches["10"])
            print("Accuracy: " + str((matches["00"] + matches["11"]) / len(df.index)))
            # print("Recall: " + str(recall))
            # print("Precision: " + str(precision))
            # print("F-Score: " + str(2 * precision * recall / (precision + recall)))
            # print("+++++++++++++++++++++++++++++++++++++++")
