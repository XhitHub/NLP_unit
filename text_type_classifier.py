import sys
import io_local.io as io
import nlp.nlp_controller as nlpc

inputFolder = 'files/inputs'
outputFolder = 'files/outputs'

# project = 't4'

def run(project):
  inFilename = inputFolder + '/' + project + '.txt'
  outProjectFolder = outputFolder + '/' + project
  text = io.textFileToString(inFilename)
  sents = nlpc.textToSents(text)
  nlpDicts = []
  nlpTypesDict = {}
  for sent in sents:
    if not sent.text == '':
      print(sent)
      # sent = sent.replace('\n','')
      nlpDict = nlpc.sentToNLPSequence(sent)
      nlpDict['_text'] = nlpDict['_text'].replace('\n', '')
      nlpDict['lemmaSeq'] = nlpDict['lemmaSeq'].replace('\n', '')
      if nlpDict['_text'] != '':
        nlpDicts.append(nlpDict)
      pos = nlpDict['posSeq']
      if pos not in nlpTypesDict:
        nlpTypesDict[pos] = {
          'count': 0
        }
      nlpTypesDict[pos]['count'] = nlpTypesDict[pos]['count'] + 1
  print(nlpDicts)
  for nd in nlpDicts:
    nd['count'] = nlpTypesDict[nd['posSeq']]['count']
  nlpDicts.sort(key=lambda x: x['count'], reverse=True)
  io.mapListToCsv(outProjectFolder + '/nlp_seqs.csv', nlpDicts)  
