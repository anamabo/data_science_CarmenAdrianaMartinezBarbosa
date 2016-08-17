import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


###  data stuctures --> Series

s= pd.Series([-1,3,5, np.nan, 6, 8])
#print (s)
#print (s[0])

###  data structures --> Data Frame (table) with labeled columns

dates= pd.date_range('20150101', periods=6)
table= pd.DataFrame(np.random.randn(6, 4), index=dates, columns= list('ABCD'))
#print (table)

### data sctructures --> using a dictionaty

table1= pd.DataFrame({'A': [1,2,3,4],
                      'B': pd.Timestamp('19840825'),
                      'C': np.arange(4),
                      'D': pd.Categorical(['test', 'train', 'food', 'naa'])
                      })
#print (table1)


### see top and bottom rows of tables
print (table1.head(3))
print (table1.tail(1))

### data structures --> Quick statistics

statistics= table.describe()
print (statistics)

### data structures --> operations

table1.T   # transpose (rows-> columns, colums ->rows)
table1['A'] # Obtaining columns
print (table1.loc[1, 'A'])
print (table1.iloc[:, 1:3])  # select 1 and 2nd columns


###### VOY en boolean indexing
