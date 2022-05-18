''' Modeling off cookbook recipe, makes ini files more robust than if I were to only predefine them '''
import string
from datetime import datetime
import configparser

def create_ini():
    config = configparser.ConfigParser()
    
    config['database'] = {
        "database.dbms":            "mysql",
        "database.db":            	"gis_test",
        "database.username":	"flask",
        "database.password":        "Lifetime!098",
        "database.host":            "127.0.0.1",
        "database.port":            "3306"
        }

    config['fl_charlotte'] = {
            'state':    'fl',
            'county':   "charlotte",
            'trial':   "no",
            'gis_url':          "https://www.ccappraiser.com/downloads/charlotte.zip",
            'raw_file_type':    "csv"
    }
#        source_filename = cd.txt
#        staging_path = /home/lpusa-admin/datpipe/external/GIS/staging/%(state)s/%(county)s/
#        staging_filename = %(state)s_%(county)s_gis.%(raw_file_type)s
#        staging_abspath= %(staging_path)s/%(staging_filename)s
#        notes = "Property appraisers table updates nightly"
#        g supporting data urs

    config['fl_lee'] = {
            'state':                "fl",
            'county':               "lee",
            'trial':                "no",
            'gis_url':              "https://www.arcgis.com/sharing/rest/content/items/d6c42c6e3268484a8512b7ec57ecdb2f/data",
            'raw_file_type':        "shapefile",
            'raw_download_dir':     "/home/lpusa-admin/datpipe/external/GIS/raw/%(state)s/%(county)s/",
            'source_filename':      "Parcels.shp"
    }
# csv
#    staging_path = /home/lpusa-admin/datpipe/external/GIS/staging/%(state)s/%(county)s/
#    staging_filename = %(state)s_%(county)s_gis.%(raw_file_type)s
#    staging_abspath= %(staging_path)s/%(staging_filename)s

    config['time'] = {
            'datestamp': f'{datetime.today().strftime("%Y%m%d")}',
            'Year': f'{datetime.today().strftime("%Y")}',
            'Month': f'{datetime.today().strftime("%m")}',
            'day': f'{datetime.today().strftime("%d")}'
    }

    with open('boilerplate.ini', 'w') as f:
        config.write(f)


if __name__ == "__main__":
    create_ini()


#def LoadConfig(file, config={}):
#    """
#    returns a dictionary with keys of the form
#    <section>.<option> and the corresponding values
#    """
#    config = config.copy(  )
#    cp = configparser.ConfigParser(  )
#    cp.read(file)
#    for sec in cp.sections(  ):
#        name = string.lower(sec)
#        for optn in cp.options(sec):
#            config[f'{name}.{string.lower(optn)}'] = string.strip(
#                cp.get(sec, optn))
#    return config
#
#if __name__ == "__main__":
#    for i in ini_content:
#        print(f'{i = }')
#        print(f'{LoadConfig("boilerplate.ini", i)}')
