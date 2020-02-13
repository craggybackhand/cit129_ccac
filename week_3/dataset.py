import csv

def processjailCSV():
    """
    Iterates over inputted CSV to tabulate inmates by race.
    """
    file = open('base_data.csv', newline='')
    #reads csv into a dictionary object
    reader = csv.DictReader(file)
    racecount = {}
    focusdate = '2019-06-01'
    
    for row in reader:
        if row['Date'] == focusdate:
            # ask dictionary if race key is already present in dictionary
            if row['Race'] not in racecount:
                #sets key to 1 if index not already present
                #initiates new index with the contents of 'Race' and sets its 
                #key to 1
                racecount[(row['Race'])] = 1
            else:
                racecount[(row['Race'])] += 1
                #increments counter if race index already present
    file.close
    
    print(racecount)
    
processjailCSV()