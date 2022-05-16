''' trimmed version of bloated downloader '''
import argparse
import configparser
import fiona
import glob
import os
import pandas as pd
import pymysql
import pytz
import re
import requests
import shutil
from collections import defaultdict
from datetime import datetime
from io import BytesIO
from pathlib import Path
from pprint import pprint
from zipfile import ZipFile

### change from current tp download raw path 

# returns list of gis sections to download 
def gis_sections(parser, sections=None):
    ''' defines GIS data that will be downloaded '''
    section_list = []

    # confirms all elements in user-list map to config section 
    if sections is None:
        for s in parser.sections():
            [section_list.append(s) for o in parser.options(s) if o == 'gis_url']
        return section_list

    else:
        for y in sections:
            match = False 
            for x in parser.sections():
                if x == y:
                    match = True
                    section_list.append(y)
                    break
            if match is False:
                print("Error here bitchaass.")
                exit()

def download_gis_data(parser,section_id):
    ''' downloads raw GIS data into zip file '''
    url = parser.get(section_id,'gis_url')
    download_dest = Path(parser.get(section_id,'raw_download_dir'),
        f"{datetime.today().strftime('%Y%m%d')}.{parser.get(section_id,'state')}_{parser.get(section_id,'county')}.zip")
    print(download_dest)
    os.makedirs(download_dest.parent,exist_ok=True)
    r = requests.get(url,stream=True)
    with open(download_dest,'wb') as url_download:
        for chunk in r.iter_content(chunk_size=128):
            url_download.write(chunk)
#    try:
#        with open(zip_path,'wb') as url_download:
#            for chunk in r.iter_content(chunk_size=128):
#                url_download.write(chunk)
#    except:
#        print("Error downloading URL")
    return

def stage_data(parser,section_id):
    ''' takes zips and stores data as csv '''
    # assigning config paths to variables
    raw_zipfile_path = Path(
            parser.get(section_id,'raw_download_dir'),
            f"{datetime.today().strftime('%Y%m%d')}.{parser.get(section_id,'state')}_{parser.get(section_id,'county')}.zip"
            )
    
    datestamp = datetime.today().strftime('%Y%m%d')
    staging_filepath = Path(parser.get(section_id,'staging_abspath'))
    staging_dir = staging_filepath.parent
    print(f"{staging_dir = }")
    staging_filename = staging_filepath.name

    ## TODO - FIX
    ## CURRENT STATUS: extracting entire zip folder instead of just "cd.txt"
    with ZipFile(raw_zipfile_path) as zf:
        for zipf in zf.namelist():
             if zipf == parser.get(section_id,'source_filename'):
                 zf.extract(zipf,Path(f'{staging_dir}', f'{datestamp}.{staging_filename}'))


def main():
    ''' main funct. config parser object defined here '''
    config = configparser.ConfigParser()
    config.read('gis.ini')
    section_list = gis_sections(parser=config)
    for x in section_list:
        download_gis_data(config,x)
        stage_data(config,x)
        #unzip_download(parser=config,section=x)
    return 


if __name__ == '__main__':
    main()
