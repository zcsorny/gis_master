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

#def download_gisdata(gis_section):      ## add code for "list" option
#    for s in gis_sections:
#        if gisconfig[gis_section] == gisconfig:
#            print("WILL JUMP TO AND DOWNLOAD API FROM HERE\n.")
#            return 


def datestamp_vals():
    '''returns date values for given day '''

    ## needs to be called each time files are downloaded to ensure it stays in-sync
    datestamp = datetime.today().strftime('%Y%m%d')
    year = datetime.today().strftime('%Y')
    month = datetime.today().strftime('%m')
    day = datetime.today().strftime('%d')
    return datestamp,year,month ,day

## 1 of 4 file type functs 
def zip_dwnld_path(gis_county):
    ''' returns path for download zipfile '''

    # getting time value which will be used in funct
    ## path runtime vals
    datestamp,yr ,mm ,day  = datestamp_vals()
    st = gisconfig.get(gis_county,'state').upper()
    county = gisconfig.get(gis_county,'county').upper()

    # instructing py to grab "raw filetype"  (we have multiple file types in the pipeline 
    rawfile_base  = gisconfig.get('pipelines','raw')

    # combining 
    gis_zip = (
                f'{rawfile_base}/{st}/{yr}/'
                f'{datestamp}.raw.{st}_{county}.zip'
                )

    # turning into path obj for easy file ops 
    return Path(gis_zip)
    


def staging_download_helper():
    ''' '''
    return


def consumption_download_helper():
    ''' '''
    return

def filepath_builder(gis_id, filepath_type=None):
    ''' user pass type of filepath they want and a gis_id (GIS county) and function returns absolute path for the pair '''
    # gis_data.ini parameters 
    print(f'{gis_id = }')      # will be either fl_lee or fl_char etc. 
    print(f'{filepath_type = }')

    if validate_filetype(filepath_type):
        print("")
        print("")
        #print(f'{create_dstamp_date(gis_id,filepath_type) = }')
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



## STAGING FILE AND PATH
def staging_tpath():
    staging_path = gisconfig['pipelines']['base']
    print(f'{staging_tpath = }')


    ## adding job/country info directly after base 
    staging_path = f"{staging_path}/{gisconfig}" 
    print(f"{gisconfig.sections()    = }")
    gisconfig.get(dtime)

    ## TODO
    ##  --> add this to for loop for all of  gis sections 
#
#    for all counties in gis_county_list:
#        url_download_path = gisconfig[counties]['base/STATE/COUNTY']    ## I THEN ADD TIME and .ZIP
#        # can either call function with logic or do logic here          ## TODO ***

    ## configuring staging path with date/time info
    staging_path = f"{staging}"


def  main():
    #print(f"{zip_dwnld_path('fl_lee') = }")
    ####for s in gis_sections:
    ####    print("valid check")
    ####    filepath_builder(s,"zip")

    print(f"\n\n{gisconfig.sections()}\n\n")
    gisconfig.add_section('dtime')
    gisconfig.set('dtime','datestamp',datetime.today().strftime('%Y%m%d'))
    print("AFTERRR")
    print(f"\n\n{gisconfig.sections()}\n\n")

    

if __name__ == "__main__":
    main()
