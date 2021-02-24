in_file = open('movie_lines.txt','rb')
out_file = open('../../character_dialogue_cornell.csv','a')
text = in_file.readlines()
for line in text:
    line = line.decode(errors='replace')
    line = line.split('+++$+++')
    out_file.write(f"{line[3]}¬{line[4]}")
in_file.close()
out_file.close()
from pandas import read_csv
df = read_csv("../../character_dialogue_cornell.csv",delimiter='¬',engine='python')
df.head(10)