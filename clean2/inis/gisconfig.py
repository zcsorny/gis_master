''' Creates .INI config file containing all config variables related to pulling & processing GIS data '''
from datetime import datetime
import configparser

def create_ini():
    ''' defines section/option values and creates ini file for gis data '''

    config = configparser.ConfigParser()
    
    config['database'] = {
        "database.dbms":        "mysql",
        "database.db":          "gis_test",
        "database.username":	"flask",
        "database.password":    "Lifetime!098",
        "database.host":        "127.0.0.1",
        "database.port":        "3306",
        }

    # base folders for all sections/areas (e.g. raw,staging, consuming/prod, etc.) within data retrieval pipeline
    # file path "trunk" (e.g. "raw" corresponds to a pipeline")
    config['pipelines'] = {
            'base':             "/home/lpusa-admin/datpipe/external/GIS",
            'raw':              "%(base)s/raw/",
            'staging':          "%(base)s/staging",
            'consumption':      "%(base)s/consumption",
            }

    config['fl_charlotte'] = {
            'gis_section':      "True",
            'state':            'fl',
            'county':           "charlotte",
            'trial':            "no",
            'gis_url':          "https://www.ccappraiser.com/downloads/charlotte.zip",
            'source_filename':  "cd.txt",
            'notes':            "Property appraisers table updates nightly",
            #'raw_dpath':    "${pipelines:raw}s/${state}s/${county}/"
    }

    config['fl_lee'] = {
            'gis_section':      "True",
            'state':            'fl',
            'county':           "lee",
            'trial':            "no",
            'gis_url':          "https://www.arcgis.com/sharing/rest/content/items/d6c42c6e3268484a8512b7ec57ecdb2f/data",
            'source_filename':  "Parcels.shp",
#            'notes':                ""
    }


    ## creating ini file with above config params
    with open('inis/gis_data.ini', 'w') as f:
        config.write(f)

if __name__ == "__main__":
    create_ini()
