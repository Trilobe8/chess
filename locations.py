from config import ACTIVE, URL_TEMPLATE, STREAM_URL_TEMPLATE, STREAM_TYPES, ANALYSIS_DIR, stream_url, HOME_TEMPLATE
import os
import json
from pprint import pprint
import errno
from json2html import *

def dump_summary():
  CATEGORIES = ACTIVE.keys()
  for category in ACTIVE.keys():
      for handle, player in ACTIVE[category].items():
           summary = {'urls':{'stats':URL_TEMPLATE.replace('HANDLE', handle.lower() ),
                              'home':HOME_TEMPLATE.replace('HANDLE', handle.lower() ),
                              'raw':'https://raw.githubusercontent.com/microprediction/chess/main/analysis/'+handle.lower()'/'+category+'/locations.json',
                              'level': stream_url(category=category,handle=handle, stream_type='level'),
                              'change':stream_url(category=category,handle=handle, stream_type='change'),
                              'daily':stream_url(category=category,handle=handle, stream_type='daily')}}
           pprint(summary)
           directory = ANALYSIS_DIR+os.path.sep+handle.lower()+os.path.sep+category
           summary_json_file = directory+os.path.sep+'locations.json'
           summary_html_file = directory+os.path.sep+'locations.html'
           readme_md_file = directory+os.path.sep+'README.md'
            
            
           try:
              os.makedirs(directory)
           except OSError as e:
              if e.errno != errno.EEXIST:
                  os.makedirs(directory)
                  
           with open(summary_json_file,'wt') as fp:
              json.dump(summary,fp=fp)
              
           summary_html = json2html.convert(summary)
           with open(summary_html_file,'wt') as fp:
               fp.write(summary_html)
                
           with open(readme_md_file,'wt') as fp:
               fp.write('### Analysis for ' + handle )
               fp.write('- View [raw]('+summary['raw']+') markdown for links to streams') 

 
if __name__=='__main__':
    dump_summary()
