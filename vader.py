import pandas as pd
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


continuing_file_path =os.getcwd()+ '\input.csv'

d = pd.read_csv(continuing_file_path, #loading that dataset
                encoding = "ISO-8859-1",
                header=None
               )


analyzer = SentimentIntensityAnalyzer()
#for sentence in sentences:
#    vs = analyzer.polarity_scores(sentence)
#    print("{:-<65} {}".format(sentence, str(vs)))

df = pd.DataFrame(columns=['neg', 'neu', 'pos','compound', 'text'])
print(df)

for index, row in d.iterrows():
    vs = analyzer.polarity_scores(row[0])
    vs['text'] = row[0]
    df = df.append(vs, ignore_index=True)

df.to_csv("output.csv",index=None, header=True,encoding="utf-8")
