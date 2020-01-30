
import pandas as pd
import subprocess
import shlex
from io import StringIO
import os
#############################################################################################################################
##################                                                                                         ##################
##################                    Reading in Textfile containing text and ids                          ##################
##################                                                                                         ##################
#############################################################################################################################
current_folder = os.getcwd()

continuing_file_path =os.getcwd()+ '\input.csv'



d_1 = pd.read_csv(continuing_file_path, #loading that dataset
                         encoding = "ISO-8859-1")

#d_1 = pd.read_clipboard(continuing_file_path,)




df_text = d_1.iloc[:,0] #only text is relevant CHANGE THE NUMBER 3 in case your text is on another position
#############################################################################################################################
##################                                                                                         ##################
##################                    Sentiment Analysis for Sentistrengh                                  ##################
##################                                                                                         ##################
#############################################################################################################################

SentiStrengthLocation = os.getcwd()+'\SentiStrength.jar' #The location of SentiStrength on your computer
SentiStrengthLanguageFolder = os.getcwd()+'\SentiStrength_Data\\'

 #The location of the unzipped SentiStrength data files on your computer

if not os.path.isfile(SentiStrengthLocation):
    print("SentiStrength not found at: ", SentiStrengthLocation)
else:
    print ("files are there")
if not os.path.isdir(SentiStrengthLanguageFolder):
    print("SentiStrength data folder not found at: ", SentiStrengthLanguageFolder)
else:
    print ("files are there")

df_text1 = df_text.str.replace(",", " ")# All comma will be deleted to not interfere with the comma that is used as delimiter
df_text1 = df_text1.str.replace("\n", " ") # just to make sure everything is in the right format
df_text1 = df_text1.str.replace("+", " ")
df_text1 = df_text1.str.replace('"', " ")
df_texttext = df_text1
conc_text = '\n'.join(list(df_texttext)) # list = [a,b,c]

p = subprocess.Popen(shlex.split("java -jar '" + SentiStrengthLocation + "' stdin sentidata '" + SentiStrengthLanguageFolder + "'"),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
b = bytes(conc_text.replace(" ","+"), 'utf-8')
stdout_text, stderr_text = p.communicate(b)
stdout_text = stdout_text.decode("utf-8")
stdout_text = stdout_text.replace(' ',',')
stdout_text = stdout_text.rstrip().replace("\t", ",") #remove the tab spacing between the positive and negative ratings. e.g. 1    -5 -> 1 -5
result = stdout_text

text_rating = pd.read_csv(StringIO(result), sep=',', header = None)
text_rating1 = text_rating.iloc[:, 0:2]

df_sentiment_age = d_1.assign(sen_pos = text_rating1.iloc[:, 0])
df_sentiment_age = df_sentiment_age.assign(sen_neg = text_rating1.iloc[:, 1])


#df_sentiment_age.to_csv(r'D:\\DownloadsDesktop\\Desktop\\Oxford',  ###change to your desired destination
#                                     index=None, header=True,
#                                     encoding="utf-8")

#print("Finished! The results will be in: D:\\DownloadsDesktop\\Desktop\\Oxford")
>>>>>>> daf04ac0a43998bb7a6560ce27362e99c919d678:sentiStrenth_general_file.py
