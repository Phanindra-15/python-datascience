Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd

pd.read_csv("D:\py-data science\weather.csv")
       Data.Precipitation   Date.Full  ...  Data.Wind.Direction  Data.Wind.Speed
0                    0.00  2016-01-03  ...                   33             4.33
1                    0.00  2016-01-03  ...                   32             3.86
2                    0.16  2016-01-03  ...                   35             9.73
3                    0.00  2016-01-03  ...                   32             6.86
4                    0.01  2016-01-03  ...                   19             7.80
...                   ...         ...  ...                  ...              ...
16738                0.08  2017-01-01  ...                   23            19.98
16739                0.00  2017-01-01  ...                   26            15.16
16740                0.00  2017-01-01  ...                   26             1.65
16741                0.06  2017-01-01  ...                   24            18.16
16742                0.10  2017-01-01  ...                   23             7.51

[16743 rows x 14 columns]
df=pd.read_csv("D:\py-data science\weather.csv")
df
       Data.Precipitation   Date.Full  ...  Data.Wind.Direction  Data.Wind.Speed
0                    0.00  2016-01-03  ...                   33             4.33
1                    0.00  2016-01-03  ...                   32             3.86
2                    0.16  2016-01-03  ...                   35             9.73
3                    0.00  2016-01-03  ...                   32             6.86
4                    0.01  2016-01-03  ...                   19             7.80
...                   ...         ...  ...                  ...              ...
16738                0.08  2017-01-01  ...                   23            19.98
16739                0.00  2017-01-01  ...                   26            15.16
16740                0.00  2017-01-01  ...                   26             1.65
16741                0.06  2017-01-01  ...                   24            18.16
16742                0.10  2017-01-01  ...                   23             7.51

[16743 rows x 14 columns]
df = pd.read_excel("weather.xlsr","sheet1")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    df = pd.read_excel("weather.xlsr","sheet1")
  File "C:\Users\phani\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\phani\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\io\excel\_base.py", line 457, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "C:\Users\phani\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\io\excel\_base.py", line 1376, in __init__
    ext = inspect_excel_format(
  File "C:\Users\phani\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\io\excel\_base.py", line 1250, in inspect_excel_format
    with get_handle(
  File "C:\Users\phani\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\io\common.py", line 798, in get_handle
    handle = open(handle, ioargs.mode)
FileNotFoundError: [Errno 2] No such file or directory: 'weather.xlsr'
