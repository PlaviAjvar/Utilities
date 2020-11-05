import zipfile
from pathlib import Path
import sys

extension = '.zip'

# default parameters
source = './'
destination = None

# look at command line arguments
for arg_idx, argv in enumerate(sys.argv):
    if argv == '-s':
        if arg_idx + 1 < len(sys.argv):
            source = sys.argv[arg_idx + 1]
        else:
            raise Exception('Insufficient number of command line arguments')

    if argv == "-d":
        if arg_idx + 1 < len(sys.argv):
            destination = sys.argv[arg_idx + 1]
        else:
            raise Exception('Insufficient number of command line arguments')

if destination is None:
    destination = source
    
print('*******************************')
print('Source directory:', source)
print('Destination directory:', destination)
print('Extension:', extension)
print('*******************************')
print('')

# get all dir files
toplevel = Path(source)
zipnames = [zipfile.name for zipfile in toplevel.glob('*' + extension)]

# extract all the zipfiles
for zipname in zipnames:
    print('*******************************')
    print('Extracting', zipname)
    print('*******************************')

    path_to_zip_file = source + "/" + zipname

    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination)
