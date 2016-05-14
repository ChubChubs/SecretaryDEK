__author__ = 'masterbob'

import csv, os
from datetime import datetime, timedelta, date
# Load

def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as err:
            print("I/O error({0}): {1}".format(err))
    return



BASE = "../csv/base.csv"

#for line in open (FILE,"r"):
with open(BASE) as f:
    base = [{k: v for k, v in row.items()}
         for row in csv.DictReader(f, skipinitialspace=True)]


DAYZ = "../csv/day_z_info.csv"

#for line in open (FILE,"r"):
with open(DAYZ) as f:
    dayz = [{k: v for k, v in row.items()}
         for row in csv.DictReader(f, skipinitialspace=True)]

REC_INFO = "../csv/rec_info.csv"

#for line in open (FILE,"r"):
with open(REC_INFO) as f:
    rec_info = [{k: v for k, v in row.items()}
         for row in csv.DictReader(f, skipinitialspace=True)]

RECENZ = "../csv/recenz.csv"

#for line in open (FILE,"r"):
with open(RECENZ) as f:
    recenz = [{k: v for k, v in row.items()}
         for row in csv.DictReader(f, skipinitialspace=True)]


# Moving from Delphian time to something more convenient.

for item in base:
    item['data_z'] = date(1900,1,1) + timedelta(days=int(item['data_z']) - 2)
    item['data_r'] = date(1900,1,1) + timedelta(days=int(item['data_r']) - 2)

print(base[0])
print(dayz[0])
print(recenz[3])
print(rec_info[3])
for opezdol in rec_info:
    home = opezdol['home_address']
    opezdol['home'] = opezdol.pop('home_address')
    opezdol['passseries'] = opezdol.pop('pasport_a')
    opezdol['passnum'] = opezdol.pop('pasport_b')
    opezdol['passplace'] = opezdol.pop('pasport_c')
    passplace = opezdol['passplace'].split(',')
    if len(passplace) > 1:
        if passplace[0][0].isdigit():
            opezdol['passdate'] = datetime.strptime(passplace[0],"%d.%m.%Yр").date()
            del passplace[0]
        opezdol['passplace'] = ''.join(passplace)
    opezdol['idnum'] = opezdol.pop('id_code')
    pip = opezdol['pip_full']
    opezdol['name'] = pip.split(' ')[1]
    opezdol['surname'] = pip.split(' ')[0]
    opezdol['mname'] = pip.split(' ')[2]
    opezdol.pop('pip_full')
    opezdol['graduate'] = opezdol.pop('oswita')
    opezdol['extra_graduate'] = opezdol.pop('spec_oswita')
    opezdol['workplace'] = opezdol.pop('work_space_address')
    children = opezdol.pop('count_child')
    if len(children) > 0:
        opezdol['children'] = children
    else:
        opezdol['children'] = None
    opezdol['edugrade'] = opezdol.pop('V4en_z')
    opezdol['level'] = opezdol.pop('Nauk_stup')
    year = opezdol.pop('year_n')
    if len(year) == 4:
        opezdol['bdate'] = datetime.strptime(year,"%Y").date()
    else:
        opezdol['bdate'] = None
    print(opezdol['bdate'])
    opezdol['position'] = opezdol.pop('posada')
    opezdol.pop('pip')
    print(opezdol)

WriteDictToCSV("Reviewer.csv",['id','name','surname','mname','passseries','passnum','idnum','passplace','passdate','children'
        ,'graduate','extra_graduate','edugrade','level','workplace','home','position','bdate'],rec_info)
'''
fixtures:
user
userprofile
reviewer
diplomas
handing_days


WriteDictToCSV("scv.csv",['data_z', 'stud' ,'data_r', 'id_recenz',
                          'groups', 'stud', 'tema', 'keriv', 'year', 'id', 'sezon'], base)
'''
