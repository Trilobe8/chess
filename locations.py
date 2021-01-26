from config import ACTIVE, URL_TEMPLATE, STREAM_URL_TEMPLATE, STREAM_TYPES, ANALYSIS_DIR, stream_url
import os
import json
from pprint import pprint

def dump_summary():
  CATEGORIES = ACTIVE.keys()
  for category in ACTIVE.keys():
      for handle, player in ACTIVE[category].items():
           summary = {'urls':{'stats':URL_TEMPLATE.replace('HANDLE', handle.lower() ),
                              'level': stream_url(category=category,handle=handle, stream_type='level'),
                              'change':stream_url(category=category,handle=handle, stream_type='change'),
                              'daily':stream_url(category=category,handle=handle, stream_type='daily')}}
           pprint(summary)
           directory = ANALYSIS_DIR+os.path.sep+handle.lower()+os.path.sep+category
           summary_file = directory+os.path.sep+'summary.json'
           try:
              os.mkdirs(directory)
           except Exception as e:
              print(e)
           with open(summary_file,'wt') as f:
              json.dump(summary_file,summary)

 
if __name__=='__main__':
    dump_summary()
