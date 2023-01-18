import spacy
import os

while True:
  os.system('cls')
  print("This program uses english small or medium language core")
  choice_of_core = input("Please type in s for small or m for midium  s/m: ")
  
  if choice_of_core.lower() == 'm':
    nlp = spacy.load('en_core_web_md')
  elif choice_of_core.lower() == 's':
    nlp = spacy.load('en_core_web_sm')
  else:
    print("Your input is not right!")
    input("")
    continue

  print("\ncomparing cat with monkey and banana")
  print("========================================\n")
  word1 = nlp("cat")
  word2 = nlp("monkey")
  word3 = nlp("banana")
  print(word1.similarity(word2))
  print(word3.similarity(word2))
  print(word3.similarity(word1))
  
  #----------------Note1
  '''
  Relationship between items can be direct or indirect simple or complex. It depends on the 
  way we identify and incorporate the rules to represent relationships.  In this context it 
  uses only the language as a source of iformation.  animals are seen as a single class hence 
  mokeys and cat are close in this way.  From my statistical background we used to look more
  at information collected through other senses such as eyes 'dimensions' 'colors' 'shapes'. 
  In this context relationships are derived from language use and the richness and truthfulness
  of these relationsships depends only on the level of language use and intensity.  In the example 
  bellow cats and monkeys both have a negative similarity with market because they don't do the shopping
  but that should not happen unless the language experince is not deep enough as modern cat and dogs has
  their supplies stored in markets as well.
  '''
  
  print("\ncomparing a set of tokens.")
  print("========================================\n")
  tokens = nlp('cat apple monkey banana market')
  for token1 in tokens:
    for token2 in tokens:
      print("===============================")
      print(token1.text, token2.text, token1.similarity(token2))
  
  
  print("\ncomparing senteces")
  print("========================================\n")
  sentence_to_compare = "Why is my cat on the car"
  sentences = ["where did my dog go",
  "Hello, there is my car",
  "I\'ve lost my cat in my car",
  "I\'d like my boat back",
  "I will name my dog Diana"]
  
  model_sentence = nlp(sentence_to_compare)
  
  for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print("----------------------------------")
    print(sentence + " - ", similarity)
  
  
  #------------Note2
  '''
  en_core_web_sm have less iformation about these items so the results were vague
  as the results of cat vs monkey are not far away from cat and bannan which is 
  not correct.  en_core_web_md contain more iformation hence the clear similariy 
  differnces are much more obvous
  '''
  input("")
