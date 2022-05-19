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

# making config parser variables global 
gisconfig = configparser.ConfigParser()
gisconfig.read('inis/gis_data.ini')
gis_sections = []
gis_sections = [s for s in gisconfig.sections() if gisconfig.has_option(s,'gis_section') ] 
for g in gis_sections:
    print(f"{g = }")


def validate_filetype(ftype):
    if ftype in ['zip','raw','source','staged']:
        return ftype
    else:
        print("Invalid file type given")
        exit()

def download_gisdata(gis_section):      ## add code for "list" option
    for s in gis_sections:
        if gisconfig[gis_section] == gisconfig:
            print("WILL JUMP TO AND DOWNLOAD API FROM HERE\n.")
            return 

def create_dstamp_date(section_name, filetype):
    ''' Funct is a helper function to <<filepath_builder>> '''
    if filetype == 'zip':
        ## absolute path to parent directory of where file will be saved 
        #for x in gisconfig.sections():
            #print(f'{x = }')
        abspath_parent = gisconfig['pipelines']
        print(f"{abspath_parent = }")
        print("need to add timestamps here")
        return

def datestamp_vals():
    '''returns date values for given day '''
    ## creating filepath for specific "gis_id" and "filepath_type" that wsa passed as variable 
    datestamp = datetime.today().strftime('%Y%m%d')
    year = datetime.today().strftime('%Y')
    month = datetime.today().strftime('%m')
    day = datetime.today().strftime('%d')
    return datestamp,year,month,day

def zip_dwnld_path(gis_county):
    ''' returns path for download zipfile '''
    raw_gis_zipf_path = gisconfig.get('pipelines','raw')
    print(f"{raw_gis_zipf_path  = }")


    # timestamps
    z =  datestamp_vals()
    print(f'{z  = }')
    print("----------------------------------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\n")
    datestamp,yr,t,x = datestamp_vals()
    # location vars 
    st = gisconfig.get(gis_county,'state').upper()
    county = gisconfig.get(gis_county,'county').upper()


    # combining 
    raw_gis_zipf_path = f'{raw_gis_zipf_path}/{st}/{yr}/{datestamp}.raw.{st}_{county}.zip'

    rawzip_path = Path(raw_gis_zipf_path)
    print(f"{rawzip_path  = }")

def filepath_builder(gis_id, filepath_type=None):
    ''' user pass type of filepath they want and a gis_id (GIS county) and function returns absolute path for the pair '''
    # gis_data.ini parameters 
    print(f'{gis_id = }')      # will be either fl_lee or fl_char etc. 
    print(f'{filepath_type = }')

    if validate_filetype(filepath_type):
        print("")
        print("")
        print(f'{create_dstamp_date(gis_id,filepath_type) = }')
        print("")
        print("")

    # getting "GIS" config params for "gis_id"
    for sect in gisconfig.sections():
        if sect == gis_id:
            print(sect)
    for sect in gis_sections:
        if sect == gis_id:
            print(">>>>>>>>>>>>>>>>>>>>>>")
            print(sect)


    
    # if filepath_type in ['base','raw','stagin','consumption']
    #return gisconfig.get
    for opt in gisconfig[gis_id]:
        print(f'{opt = }')
        if gisconfig.get(gis_id,datestamp) == opt:
            print("yerrr")
            #filepath = f'{stem}{uniq_conf'
            filepath = gisconfig,get(gis_id,opt)
            print(f"{ filepath = }")
            if opt == 'raw':
                extension == ".gz"
            elif opt == 'staging':
                extension = gisconfig,get(gis_id,'source_filename')
            else:
                extension='.csv'
            filepath_with_datestamp = f'{filepath}/{year}/{datestamp}.{filepath}{extension}'
            print(f"{filepath_with_datestamp =}")

    # call pathconfig to generate correct time stamp        <<< TOO MUCH WORK ATM

    # filehelper.ini parameters/options
    return None 


def  main():
    print(f"{zip_dwnld_path('fl_lee') = }")
    for s in gis_sections:
        print("valid check")
        filepath_builder(s,"zip")

    

if __name__ == "__main__":
    main()
