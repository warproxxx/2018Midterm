from glob import glob
from io import BytesIO
import os
import inspect

def get_name():
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__

    full_path = os.path.realpath(filename)

    return full_path

def get_locations(datadir="Election_Paper"):
    '''
    Returns the directory of located script along with the root directory (eg: where twitter_data is located)
    
    Parameters:
    ___________
    datadir: The current root directory

    Returns:
    ________
    root_dir_location
    '''

    path = get_name()
    dir_location = os.path.dirname(path)
    root_dir_location = dir_location.split(datadir)[0] + datadir

    return root_dir_location

def merge_csvs(files, ignore_name=None, ignore_first=True):
    '''
    Appends csvs and returns

    Parameters:
    ___________

    files (List):
    List of files to append

    ignore_name (string):
    Name to ignore

    ignore_first (Boolean):
    If set to true, first line of all files except one will be ignored

    Returns:
    ________
    combined (BytesIO):
    BytesIO of the files. Returns None if there is no file
    '''
    combined = BytesIO()
    first = 1

    if ignore_name != None:
        ignored_files = [file for file in files if ignore_name not in file] 
    else:
        ignored_files = files

    if len(ignored_files) >= 1:
        for file in ignored_files:
            
            with open(file, "rb") as f:

                if ignore_first == True:
                    if (first != 1):
                        next(f)                
                    else:
                        first = 0
                
                combined.write(f.read())

        combined.seek(0)
        
        return combined
    else:
        return None