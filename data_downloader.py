""" 
    code downloads raw GIS data from URL defined in INI file 
    code then converts the downloaded zip file containing the GIS data into a CSV 
    transformed csv is stored in datapipe folder for future consumption
""" 

import argparse
import configparser
import fiona
import os
import pandas as pd
import pymysql
import pytz
import re
import requests
from collections import defaultdict
from datetime import datetime
from io import BytesIO
from pathlib import Path
from pprint import pprint
from zipfile import ZipFile

### change from current tp download raw path 

# passed all tests      ^%^
# returns list of gis sections to download 
def gis_sections(parser, sections=None):
    ''' passed configparser object, and also can be given optional sections variable specifying GIS sections to download
        assumes all GIS sections if no "sections" variable is passed 
        validates and returns list of INI GIS sections 
    '''
    section_list = []
    # checks that all items in sections list map to valid ini section 
    if sections:
        for y in sections:
            match = False 
            for x in parser.sections():
                if x == y:
                    match = True
                    section_list.append(y)
                    break
            if match is False:
                print("ERROR. INVALID OBJECT IN DOWNLOAD LIST.\n\n^^SWTICH ABOVE TO LOGGING LIBRARY")
                exit()
    ## creates list of all GIS sections (default option)
    else:
        for s in parser.sections():
            [section_list.append(s) for o in parser.options(s) if o == 'gis_url']
    #print(f"{section_list = }")
    return section_list

## PASSED ALL TESTS         ^%^
def raw_download_path(parser,section_id):
    ''' creates and returns raw download path with datestamp for the specified GIS section '''

    # configuring unique filename
    datestamp = datetime.today().strftime('%Y%m%d')
    raw_filename = f"{datestamp}.{parser.get(section_id,'state')}_{parser.get(section_id,'county')}.zip"
    print(f"Download Filename:\n{raw_filename}")

    # configuring directory 
    dwnld_dir_path = parser.get(section_id,'raw_download_path') 
    os.makedirs(dwnld_dir_path,exist_ok=True)           ## creates directory if it doesnt exist, if exists does nothing 

    # joining filename and dirpath
    raw_dwnld_path = os.path.join(dwnld_dir_path, raw_filename)
    print(f"\n{raw_dwnld_path = }")
    return raw_dwnld_path 


## PASSED ALL TESTS         ^%^
def gis_downloader(parser,section_id, url=None, dwnldpath=None):
    ''' passed parser object, and download path 
        Downloads raw GIS data to the download path as .ZIP file
    '''
    url = parser.get(section_id,'gis_url')
    raw_dpath = raw_download_path(parser,section_id)
    print(f"\n{url = }\n{raw_dpath = }\n")
    r = requests.get(url,stream=True)
    try: 
        with open(raw_dpath,'wb') as url_download:
            for chunk in r.iter_content(chunk_size=128):
                url_download.write(chunk)
    except:
        print("Error. The download has failed. Please check the logs for more information.")
        exit()

    print("Returning downloaded zipfile filepath... ")
    return raw_dpath 




def main():
    ''' main funct. config parser object defined here '''
    config = configparser.ConfigParser()
    config.read('gis.ini')
    section_test = gis_sections(parser=config)
    for x in section_test:
        print(f"\n\n{x = }")
        #print(f"{config.options(x) = }")
        #print(f"{config.get(x,'raw_download_path') = }")
        rawpath = raw_download_path(config,x)
        print(f"\n{rawpath = }")
        print("")
        print(f"\n\n\n{gis_downloader(config,x) = }")
        print("")
    # download data


    return 


if __name__ == '__main__':
    ### fixed configparser referencing 
    main()

"""
def main():
    download_list = downloads()
    print(f'\n\n{download_list = }\n\n')
    for x in download_list:
        print(f"\n\n{x = }")
        print(f"{config.get(x,'gis_url')}")
        ## user x.get() to determine if shapefile or csv/standard zip
        url=config.get(x,'gis_url')
        raw_fpath = config.get(x,'raw_download_path')
        print("\n\n",'*'*50)
        print("Calling downloader() function ....")
        downloader(url,raw_fpath)
        print("\nFinished with downloader funct for this url...")
        print("\n")
    return


    if gis_section is None:



def transform_zip():
    ''' Creates and stores csv file from the raw GIS zipfile
        ## TODO
        download the CSV equivalent take a .zip file 
        ## mock layout/rerunng steps:
        > get the coonfig ini file the current "job" (aka current county whose CSV.standard I neeed to do 
        >> create CSV eqivalent
        > get the arguments & values 
        > confirm the file is "small" or 

        ## step 1: get configparse iptions list, and 
        ### FILE FORMAT FOR '''

    ## CORE LOGIN NOT CORP.SHILL
    # Get configparser 

    pass


def transform_shapefile():
    ''' creates and stores CSV file from shapefile zip for dataset '''
    return



"""
