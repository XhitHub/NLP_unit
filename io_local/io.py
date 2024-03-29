import csv
import os
import pandas as pd

def csvToList(filename):
  with open(filename, newline='') as f:
      reader = csv.reader(f)
      data = list(reader)
  return data

def textFileToString(filename):
  f = open(filename, "r")
  res = ""
  for x in f:
    res += x
  return res

def tupleListToCsv(filename, data):
  # data=[('smith, bob',2),('carol',3),('ted',4),('alice',5)]
  with open(filename,'w') as out:
      csv_out=csv.writer(out)
      # csv_out.writerow(['name','num'])
      for row in data:
          csv_out.writerow(row)

def mapListToCsv(filename, mapsList):
  # data=[('smith, bob',2),('carol',3),('ted',4),('alice',5)]
  keys = set().union(*(d.keys() for d in mapsList))
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  # with open(filename,'w') as out:
  #   dict_writer = csv.DictWriter(out, keys)
  #   dict_writer.writeheader()
  #   dict_writer.writerows(mapsList)
  df = pd.DataFrame(mapsList)
  df.to_csv(filename, index=False)
