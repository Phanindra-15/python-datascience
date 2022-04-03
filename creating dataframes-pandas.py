Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import pandas as pd
jupyter notebook
SyntaxError: invalid syntax. Perhaps you forgot a comma?
import jupyter notebook
SyntaxError: invalid syntax
import pandas as pd
data = {
  "brand": ["Ford","laer","bier","audi","bmw","toyota"]
  "model": ["Mustang","dubar","jase","dqedwf","wfwf","fwfwe"]
  "year": [1964,2001,2002,2003,2004,2005]
}
df = pd.DataFrame(data)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
data = {
  "brand": ["Ford","laer","bier","audi","bmw","toyota"],
  "model": ["Mustang","dubar","jase","dqedwf","wfwf","fwfwe"],
  "year": [1964,2001,2002,2003,2004,2005]
}
df = pd.DataFrame(data)
df
    brand    model  year
0    Ford  Mustang  1964
1    laer    dubar  2001
2    bier     jase  2002
3    audi   dqedwf  2003
4     bmw     wfwf  2004
5  toyota    fwfwe  2005
df.shape
(6, 3)
rows,columns = df.shape
rows
6
columns
3
df.head()
  brand    model  year
0  Ford  Mustang  1964
1  laer    dubar  2001
2  bier     jase  2002
3  audi   dqedwf  2003
4   bmw     wfwf  2004
df.head(2)
  brand    model  year
0  Ford  Mustang  1964
1  laer    dubar  2001
df.tail()
    brand   model  year
1    laer   dubar  2001
2    bier    jase  2002
3    audi  dqedwf  2003
4     bmw    wfwf  2004
5  toyota   fwfwe  2005
df.tail(1)
    brand  model  year
5  toyota  fwfwe  2005
df[2:5]
  brand   model  year
2  bier    jase  2002
3  audi  dqedwf  2003
4   bmw    wfwf  2004
df[:]
    brand    model  year
0    Ford  Mustang  1964
1    laer    dubar  2001
2    bier     jase  2002
3    audi   dqedwf  2003
4     bmw     wfwf  2004
5  toyota    fwfwe  2005
df.columns
Index(['brand', 'model', 'year'], dtype='object')
df.rows
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    df.rows
  File "C:\Users\phani\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\generic.py", line 5575, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'rows'
df.brand
0      Ford
1      laer
2      bier
3      audi
4       bmw
5    toyota
Name: brand, dtype: object
df.year
0    1964
1    2001
2    2002
3    2003
4    2004
5    2005
Name: year, dtype: int64
df['year'].max()
2005
df['year'].min()
1964
df['year'].std()
15.98436736314578
df.describe()
              year
count     6.000000
mean   1996.500000
std      15.984367
min    1964.000000
25%    2001.250000
50%    2002.500000
75%    2003.750000
max    2005.000000
#conditionally select data in database

df(df.year>=2002)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    df(df.year>=2002)
TypeError: 'DataFrame' object is not callable
