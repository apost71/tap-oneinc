import pymssql
import datetime
import decimal
import singer
import json

logger = singer.get_logger()

username = 'cc-data-eng'
password = 'Rqv>yUVQ'
server = 'dc2-ccrep.oneinc.local'

conn = pymssql.connect(
    host='localhost',
    user=username,
    password=password,
    database='PolicyOne_ClearCover'
)

cursor = conn.cursor()

cursor.execute('select * from Period')


columns = ['PeriodID', 'PolicyTermID', 'PeriodActiveStartDate', 'PeriodActiveEndDate', 'IsCurrentPeriod', 'WrittenPremium', 'AdditionalDownPaymentTaken', 'NewMonthlyPayment', 'TriggeringEndorsementID', 'PreviousPeriodID', 'SpawningEndorsementId']

schema = dict()

schema['properties'] = {
    'PeriodID': {
        'type': ['integer']
    },
    'PolicyTermID': {
        'type': ['integer']
    },
    'PeriodActiveStartDate': {
        'type': ['string'],
        'format': 'date-time'
    },
    'PolicyActiveEndDate': {
        'type': ['string'],
        'format': 'date-time'
    },
    'IsCurrentPeriod': {
        'type': ['boolean']
    },
    'WrittenPremium': {
        'type': ['number']
    },
    'AdditionalDownPaymentTaken': {
        'type': ['null', 'number']
    },
    'NewMonthlyPayment': {
        'type': ['null', 'number']
    },
    'TriggeringEndorsementID': {
        'type': ['integer']
    },
    'PreviousPeriodID': {
        'type': ['null', 'integer']
    },
    'SpawningEndorsementId': {
        'type': ['null', 'integer']
    }
}

row = cursor.fetchone()
records = []
iter = 0
while iter < 10:
    # print("ID=%d, Name=%s" % (row[0], row[1]))
    result = {}
    for i, record in enumerate(row):
        if isinstance(record, decimal.Decimal):
            record = float(record)
        if isinstance(record, datetime.datetime):
            record = record.strftime('%Y-%m-%d %H:%M:%S.%f')
        result[columns[i]] = record
    # print(result)
    records.append(result)
    row = cursor.fetchone()
    iter += 1

singer.write_schema('period', schema, 'PeriodID')
singer.write_records('period', records)


