import os
import csv

def ListEveryFile(d):
    # returns a list of every file in current directory AND sub-folders
    counter_rec = []
    try:
        contents = os.listdir(d)
        for file in contents:
            if '.' in file:
                counter_rec.append(file)
            if '.' not in file:
                subfolder = d + '\\' + file
                for file in ListEveryFile(subfolder):
                    counter_rec.append(file)
    except NotADirectoryError:
        counter_rec.append(d)
    except PermissionError:
        print('Access to {} is denied.'.format(d))
    return counter_rec

def duplicate_checker(directory, name):
    # INPUT: directory is a string representing the directory you want to search for duplicate file names, n is the name
    # you want to give to the output Excel file.
    # OUTPUT: An Excel file containing the names of the files in the directory in one column and the number of
    # occurences in the next column. Use DATA>SORT on column B on largest to smallest.
    tracker = {}
    contents = ListEveryFile(directory)
    for file in contents:
        if file not in tracker:
            tracker[file] = 0
            tracker[file] += 1
        else:
            #print('Duplicate: {}'.format(file))
            tracker[file] += 1
    w = csv.writer(open("{}.csv".format(name), "w", encoding="utf-8"))
    for key, val in tracker.items():
        w.writerow([key, val])
    return tracker