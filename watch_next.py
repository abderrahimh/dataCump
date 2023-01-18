import os
import sys
import re
import string

print("Loading spacy may take few minutes. Please wait.\n")
import spacy


#================================ functions
#----------------- real path
def get_script_path():
    return(os.path.dirname(os.path.realpath(sys.argv[0])))

#------------------ read and clean data 
def read_movies(data_path, movies_file, lines_list):
    try:
        with open(data_path + movies_file, 'r+') as f:
            for line in f:
                lines_list.append(re.sub("Movie [A-Z] :", '',line.replace('\n', '')))
    except:
        print(f"{data_path + movies_file} can not be found.")
        input("")
    finally:
        f.close()
    return(lines_list)

#------------------ find index of max similarity movie 
def next_movie_to_watch(sentence_com, list_senteces):
  sentence_to_compare = sentence_com
  sentences = list_senteces
  model_sentence = nlp(sentence_to_compare)
  index = 0
  ind = 0
  counter = 0
  for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    if similarity > ind:
      ind = similarity
      index = counter
    counter += 1
  return(index)

#==================== variables 

data_path = get_script_path()
movies_file = '\\movies.txt'
lines_list = []

planet_hulk = '''
Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.
'''
U_letters = list(string.ascii_uppercase)

#==================== main process
#-------------- cleaning main sentence
planet_hulk = planet_hulk.replace('\n', ' ')
planet_hulk = planet_hulk.lstrip()
planet_hulk = planet_hulk.rstrip()

#---------------- load data
lines_list = read_movies(data_path, movies_file, lines_list)
nlp = spacy.load("C:\\Users\\rahim\\Downloads\\en_core_web_md\\en_core_web_md-3.4.1")

#---------------- print output
movie_next_index = next_movie_to_watch(planet_hulk, lines_list)
print("The next movie to watch is: \n")
print(f"Movie {U_letters[movie_next_index]} : {lines_list[movie_next_index]}")

input("")
