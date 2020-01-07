import csv
import os
from beautifultable import BeautifulTable

def csv_output(path, packages):
    """ Export to CSV file """
    fieldnames = ['domain', 'notBefore', 'notAfter', 'remaining', 'exception']
    with open(path, mode='w') as f:         
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for package in packages:
            writer.writerow(
                {
                    'domain': package['domain'],
                    'notBefore': package['notBefore'],
                    'notAfter': package['notAfter'], 
                    'remaining': package['remaining'],
                    'exception': package['exception']
                }
            )

def table(path):
    """ Read from CSV export and show output in terminal """
    
    tb = BeautifulTable(max_width=1000)
    tb.column_headers = ['domain', 'notBefore', 'notAfter', 'remaining', 'exception']
    tb.column_alignments['domain'] = BeautifulTable.ALIGN_LEFT

    with open(path) as f:
        reader = csv.DictReader(f)
        for cert in reader:
            tb.append_row([cert['domain'], cert['notBefore'], cert['notAfter'], cert['remaining'], cert['exception']])
    print (tb)

