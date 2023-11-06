import sys
import io_local.io as io
import nlp.nlp_controller as nlpc

inputFolder = 'files/inputs'
outputFolder = 'files/outputs'

project = 't3'
inFilename = inputFolder + '/' + project + '.txt'
outProjectFolder = outputFolder + '/' + project

def run():
  text = io.textFileToString(inFilename)
  sents = nlpc.textToSents(text)
  nlpDicts = []
  nlpTypesDict = {}
  for sent in sents:
    if sent != '':
      sent = sent.replace('\n','')
      nlpDict = nlpc.sentToNLPSequence(sent)
      nlpDicts.append(nlpDict)
      pos = nlpDict[posSeq]
      if pos not in nlpTypesDict:
        nlpTypesDict[pos] = {
          
        }