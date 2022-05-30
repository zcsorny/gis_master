import configparser
import os 
import pymysql 
import requests
import re
from datetime import datetime
from pathlib import Path
from pprint import pprint
from zipfile import ZipFile 

# import argparse
#import fiona
#import pandas as pd


## different paths for each countny 
##      raw -- zip file of raw download data
##      staging -- path "stages" (cleans) csv 
##      consumption -- path uploads to db 

## defining config parser       **might be able to but in own function
inipath = 'gis_data.ini' 
gisconfig = configparser.ConfigParser()
gisconfig.read(inipath)
print(f"{gisconfig.sections()}")

def get_download_path(gis_job,download_type):
    ''' download_type is either raw zip (original), staging, consumption'''

    # datetime variables that will be configured upong function invocation
    datestamp = datetime.today().strftime('%Y%m%d')
    print(f'{datestamp}')
    # TODO validation check for download_type input
    valid_download_types = ['raw','statging','consumption']
    basepath = gisconfig[gis_job]['folder_path']
    
    if download_type == 'raw':
        # spreading f-string out over multiple lines for readability - will be single line string when invokedc:w
        path = (
                    f"{basepath}/{download_type}/"
                    f"{datestamp}.{gisconfig.get(gis_job,'state').upper()}"
                    f"-{gisconfig.get(gis_job,'county').upper()}.zip"
                    )
        print(f"{path     = }\n")
        return Path(path)
## TODO STATUS SUMMARY: nearly done with config file ;; starting to get baseline mappings/configs load instananeously && easily
## TODO ADD NEW SARASOTA COUNTY for MICHAELA once first two are sorted out

    elif download_type == "staging":
        path = f"{basepath}/{download_type})"
        print(f"{path     = }")
        return f"{basepath}/{staging}"

    elif  download_type == "consumption":
        path = f"{basepath}/{download_type}"
        print(f"{path     = }")
        return f"{basepath}/{download_type}"

    else:
        ## lg.info. can be 
        print("NEED TO CHANGE THOS TP :PG STMNT")


## TODO -- clean up code/make more pythonic 
##      >> code is working ;; just should make it cleaner/more maintainable
def download_zip(gis_job,download_type):
    ''' downloads GIS DATA from specific site to precofnigred pass '''

    ## calling helper function to get base dirpath 
    download_path = get_download_path('fl_charlotte','raw')
    basepath, _ = os.path.split(download_path)
    # ensures no errors are thrown for missing/already created folders (which are common for new datasets)
    os.makedirs(basepath,exist_ok=True)          

    # TODO add try/except block for downloading
    # downloading GIS data ;;
    # TEMPORARILY USING (just to confirm deserts are done)['folder_path']
    url = gisconfig[gis_job]['url']
    r = requests.get(url,stream=True)
    with open(Path(download_path),'wb') as dwnld:
        for chunk in r.iter_content(chunk_size=128):
            dwnld.write(chunk)
    print(f'\nGIS data has finished downloading...\nDownload Path:  {download_path}' )


def convert_zip():
    ''' unzips gis raw zip and converts the content/file into a standardized csv that is stored within pipeline '''
    return

def upload_csv():
    ''' upload csv/consumption file to db '''
    return

download_zip('fl_charlotte','raw')


    
