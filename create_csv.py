import csv
from itertools import islice

ATTRIBUTES = [ 'name',  'bearId',     'brewerId', 'ABV',
              'style', 'appearance', 'aroma',    'palate',
              'taste', 'overall',    'time',    'profileName',
              'text' ]

def parseReviews( txt_filename1, txt_filename2, csv_filename ):
    txt_f1 = open( txt_filename1, 'r', encoding='ISO-8859-1', errors='replace' )
    txt_f2 = open( txt_filename1, 'r', encoding='ISO-8859-1', errors='replace' )
    
    line_iter  = iter( txt_f1.readlines() + txt_f2.readlines() )
    
    with open( csv_filename, 'w+' ) as csv_f:
        writer = csv.writer( csv_f )
        writer.writerow( ATTRIBUTES )
        while True:
            lines = [ line.strip() for line in list( islice( line_iter, 14 ) ) ]
            if not lines: # EOF
                break
            lines_data = [ ':'.join( line.split(':')[1:] ).strip() for line in lines[:-1] ]
            writer.writerow( lines_data )

parseReviews( 'Beeradvocate.txt', 'Ratebeer.txt', 'beer_reviews.csv' )
