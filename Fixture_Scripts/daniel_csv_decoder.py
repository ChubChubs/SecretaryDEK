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
for guide in rec_info:
    home = guide['home_address']
    guide['home'] = guide.pop('home_address')
    guide['passseries'] = guide.pop('pasport_a')
    guide['passnum'] = guide.pop('pasport_b')
    guide['passplace'] = guide.pop('pasport_c')
    passplace = guide['passplace'].split(',')
    if len(passplace) > 1:
        if passplace[0][0].isdigit():
            guide['passdate'] = datetime.strptime(passplace[0],"%d.%m.%Yр").date()
            del passplace[0]
        guide['passplace'] = ''.join(passplace)
    guide['idnum'] = guide.pop('id_code')
    pip = guide['pip_full']
    guide['name'] = pip.split(' ')[1]
    guide['surname'] = pip.split(' ')[0]
    guide['mname'] = pip.split(' ')[2]
    guide.pop('pip_full')
    guide['graduate'] = guide.pop('oswita')
    guide['extra_graduate'] = guide.pop('spec_oswita')
    guide['workplace'] = guide.pop('work_space_address')
    children = guide.pop('count_child')
    if len(children) > 0:
        guide['children'] = children
    else:
        guide['children'] = None
    guide['edugrade'] = guide.pop('V4en_z')
    guide['level'] = guide.pop('Nauk_stup')
    year = guide.pop('year_n')
    if len(year) == 4:
        guide['bdate'] = datetime.strptime(year,"%Y").date()
    else:
        guide['bdate'] = None
    print(guide['bdate'])
    guide['position'] = guide.pop('posada')
    guide.pop('pip')
    print(guide)

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
