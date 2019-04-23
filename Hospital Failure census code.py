
import pandas as pd
import censusdata












#change from county to FIPS

county65plus = censusdata.download('acs5', 2015, censusdata.censusgeo([('county', '*')]),
                                   ['DP05_0001E', 'DP05_0014PE', 'DP05_0015PE', 'DP05_0016PE',],
                                   tabletype='profile')
county65plus['percent_65plus'] = (county65plus['DP05_0014PE'] + county65plus['DP05_0015PE']
                                  + county65plus['DP05_0016PE'])
county65plus = county65plus[['DP05_0001E', 'percent_65plus']]
county65plus = county65plus.rename(columns={'DP05_0001E': 'population_size'})
county65plus.describe()

#poverty levels
""B06012""-->1:below 100,2:100-149,3:150,
#with medicaid coverage 1 gives us total
B27007-->4,7,10,13,16,19,22,25,28,32,35,38,41,44,47,50,53,56
#employment: 1 is 
B23001--> 7
14
21
28
35
42
49
56
63
70
75
80
85
93
100
107
114
121
128
135
142
149
156
161
166
171
#college students in the area 
B14004-->3
8
19
24

