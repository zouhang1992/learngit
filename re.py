import re
import datetime
 
m = re.search('output_(?P<year>\d{4}).(?P<month>\d{2}).(?P<day>\d{2})', 'output_2016.07.26.txt')
 
weekday = datetime.datetime(int(m.group('year')),int(m.group('month')),int(m.group('day'))).strftime("%w")
 
filename = 'output_' + m.group('year') + '-' + m.group('month') + '-' + m.group('day') + '-' + weekday + '.txt'
 
print (weekday)
print filename
