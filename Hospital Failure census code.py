
import pandas as pd
import censusdata


def normalize_index(x):
    prt1=str(x).split('>')
    prt2=prt1[0].split(':')
    return str(int(prt2[3]))+str(prt1[1]).split(':')[1]



#builds out the item name from a value 
def create_census_value(table_name,item):
        if len(item)==1:
            return str(table_name)+'_00'+item+'E'
        elif len(item)==2:
            return str(table_name)+'_0'+item+'E'
        else:
            return str(table_name)+'_'+item+'E'

#inputs table_name, items inside of table,year for acs
def create_census_datapull(table_name,items,year):
    output_list=[]
    for item in items:
        item_exam=str(item)
        output_list.append(create_census_value(table_name,item_exam))
    
    new_data=censusdata.download('acs1', year, censusdata.censusgeo([ ('county','*')]),output_list)    
    return new_data



year_list=[2015,2016,2017]

#65 plus for medicare
for year in year_list:


    county65plus = censusdata.download('acs1', year, censusdata.censusgeo([ ('county','*')])
                                       ,['B01001_001E', 'B01001_020E', 'B01001_021E', 'B01001_022E', 'B01001_023E',
                                        'B01001_024E', 'B01001_025E', 'B01001_044E', 'B01001_045E', 'B01001_046E',
                                        'B01001_047E', 'B01001_048E', 'B01001_049E'])

    county65plus['pop_65plus'] = (county65plus.B01001_020E + county65plus.B01001_021E + county65plus.B01001_022E
                                      + county65plus.B01001_023E + county65plus.B01001_024E + county65plus.B01001_025E
                                      + county65plus.B01001_044E + county65plus.B01001_045E + county65plus.B01001_046E
                                      + county65plus.B01001_047E + county65plus.B01001_048E
                                      + county65plus.B01001_049E) 
    county65plus1 = county65plus[['B01001_001E', 'pop_65plus']]
    county65plus1 = county65plus1.rename(columns={'B01001_001E': 'population_size'})
    county65plus1['year']=year
    county65plus1['join_col']= county65plus1.index.map(normalize_index)
    county65plus1[['pop_65plus','join_col']].to_csv('Desktop\_age'+str(year)+'_output.csv')


 #Medicaid
for year in year_list:
    medicaid_data=create_census_datapull('B27007',[4,7,10,13,16,19,22,25,28,32,35,38,41,44,47,50,53,56],year)
    medicaid_data['medicaid_total'] = medicaid_data.sum(axis=1)
    medicaid_data['join_col']= medicaid_data.index.map(normalize_index)
    medicaid_data[['medicaid_total','join_col']].to_csv('Desktop\_medicaid'+str(year)+'_output.csv')       

#employment
for year in year_list:
    employment_data=create_census_datapull('B23001',[7,14,21,28,35,42,49,56,63,70,75,80,85,93,100,107,114,121,128,135,142,149,156,161,166,171],year)
    employment_data['employment_total'] = employment_data.sum(axis=1)
    employment_data['join_col']=  employment_data.index.map(normalize_index)
    employment_data[['employment_total','join_col']].to_csv('Desktop\_employment'+str(year)+'_output.csv')
    
#college
for year in year_list:
    college_data=create_census_datapull('B14004',[3,8,19,24],year)
    college_data['college_total'] = college_data.sum(axis=1)
    college_data['join_col']=  college_data.index.map(normalize_index)
    college_data[['college_total','join_col']].to_csv('Desktop\_college'+str(year)+'_output.csv')

