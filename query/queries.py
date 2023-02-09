from query.mysqlquery import totalrecord, totalrecordfilter, emptysearch, valuesearch, insertjson


def totalrecords():
    insertjson()
    rsallcount = totalrecord()
    print(rsallcount)
    totalRecords = rsallcount['allcount']
    return totalRecords


def totalrecordwithfilters(likeString):
    rsallcount = totalrecordfilter(likeString)
    totalRecordwithFilter = rsallcount['allcount']
    return totalRecordwithFilter


def alldata(searchValue,likeString, row, rowperpage):
    
    if searchValue == '':
        employeelist = emptysearch(row, rowperpage)
    else:        
        employeelist=valuesearch(likeString, row, rowperpage)
    data = []
    for row in employeelist:
        data.append({
        'name': row['name'],
        'position': row['position'],
        'age': row['age'],
        'salary': row['salary'],
        'office': row['office'],
        })

    return data
 