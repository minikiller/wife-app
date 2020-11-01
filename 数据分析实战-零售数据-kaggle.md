

```python
#导入pandas包
import numpy as np
import pandas as pd
```


```python
#读取数据
data=pd.read_excel('/Users/elieen/Downloads/superstore_dataset2011-2015.xls',encoding='utf8')
```


```python
#查看数据集信息，打印前5行,总共有24列，太多了中间部分省略未显示
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row ID</th>
      <th>Order ID</th>
      <th>Order Date</th>
      <th>Ship Date</th>
      <th>Ship Mode</th>
      <th>Customer ID</th>
      <th>Customer Name</th>
      <th>Segment</th>
      <th>City</th>
      <th>State</th>
      <th>...</th>
      <th>Product ID</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
      <th>Quantity</th>
      <th>Discount</th>
      <th>Profit</th>
      <th>Shipping Cost</th>
      <th>Order Priority</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>42433</td>
      <td>AG-2011-2040</td>
      <td>1/1/2011</td>
      <td>6/1/2011</td>
      <td>Standard Class</td>
      <td>TB-11280</td>
      <td>Toby Braunhardt</td>
      <td>Consumer</td>
      <td>Constantine</td>
      <td>Constantine</td>
      <td>...</td>
      <td>OFF-TEN-10000025</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Tenex Lockers, Blue</td>
      <td>408.300</td>
      <td>2</td>
      <td>0.0</td>
      <td>106.140</td>
      <td>35.46</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22253</td>
      <td>IN-2011-47883</td>
      <td>1/1/2011</td>
      <td>8/1/2011</td>
      <td>Standard Class</td>
      <td>JH-15985</td>
      <td>Joseph Holt</td>
      <td>Consumer</td>
      <td>Wagga Wagga</td>
      <td>New South Wales</td>
      <td>...</td>
      <td>OFF-SU-10000618</td>
      <td>Office Supplies</td>
      <td>Supplies</td>
      <td>Acme Trimmer, High Speed</td>
      <td>120.366</td>
      <td>3</td>
      <td>0.1</td>
      <td>36.036</td>
      <td>9.72</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>2</th>
      <td>48883</td>
      <td>HU-2011-1220</td>
      <td>1/1/2011</td>
      <td>5/1/2011</td>
      <td>Second Class</td>
      <td>AT-735</td>
      <td>Annie Thurman</td>
      <td>Consumer</td>
      <td>Budapest</td>
      <td>Budapest</td>
      <td>...</td>
      <td>OFF-TEN-10001585</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Tenex Box, Single Width</td>
      <td>66.120</td>
      <td>4</td>
      <td>0.0</td>
      <td>29.640</td>
      <td>8.17</td>
      <td>High</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11731</td>
      <td>IT-2011-3647632</td>
      <td>1/1/2011</td>
      <td>5/1/2011</td>
      <td>Second Class</td>
      <td>EM-14140</td>
      <td>Eugene Moren</td>
      <td>Home Office</td>
      <td>Stockholm</td>
      <td>Stockholm</td>
      <td>...</td>
      <td>OFF-PA-10001492</td>
      <td>Office Supplies</td>
      <td>Paper</td>
      <td>Enermax Note Cards, Premium</td>
      <td>44.865</td>
      <td>3</td>
      <td>0.5</td>
      <td>-26.055</td>
      <td>4.82</td>
      <td>High</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22255</td>
      <td>IN-2011-47883</td>
      <td>1/1/2011</td>
      <td>8/1/2011</td>
      <td>Standard Class</td>
      <td>JH-15985</td>
      <td>Joseph Holt</td>
      <td>Consumer</td>
      <td>Wagga Wagga</td>
      <td>New South Wales</td>
      <td>...</td>
      <td>FUR-FU-10003447</td>
      <td>Furniture</td>
      <td>Furnishings</td>
      <td>Eldon Light Bulb, Duo Pack</td>
      <td>113.670</td>
      <td>5</td>
      <td>0.1</td>
      <td>37.770</td>
      <td>4.70</td>
      <td>Medium</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>




```python
#查看数据集大小，有多少行，多少列
data.shape
```




    (51290, 24)




```python
#查看每一列的数据类型
data.dtypes
```




    Row ID              int64
    Order ID           object
    Order Date         object
    Ship Date          object
    Ship Mode          object
    Customer ID        object
    Customer Name      object
    Segment            object
    City               object
    State              object
    Country            object
    Postal Code       float64
    Market             object
    Region             object
    Product ID         object
    Category           object
    Sub-Category       object
    Product Name       object
    Sales             float64
    Quantity            int64
    Discount          float64
    Profit            float64
    Shipping Cost     float64
    Order Priority     object
    dtype: object



# 2、数据清洗

0）因后面要进行时间序列分析，故先对Order Date进行数据清洗，后面分析都要用到


```python
#20066行数据前后的日期格式不一样，故先拆分为2个dataframe：data1和data2
data1=data.loc[0:20066,:]
data2=data.loc[20067:51289,:]

#对data1中Order Date数据进行时间格式转换
data1.loc[:,'Order Date']=pd.to_datetime(data.loc[:,'Order Date'],format='%d/%m/%Y',errors='coerce')
#对data2中Order Date数据进行时间格式转换
data2.loc[:,'Order Date']=pd.to_datetime(data.loc[:,'Order Date'],format='%d-%m-%Y',errors='coerce')

#合并data1和data2为一张表
data=data1.append(data2)
```

    /Users/elieen/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py:465: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      self.obj[item] = s



```python
#对data进行按Order Date日期进行排序
data_new=data.sort_values(by='Order Date',ascending=True,na_position='first')
```


```python
#截取Order Date中的年和月成为新的列，方面后续进行年度和月度销售分析
from datetime import datetime  #导入datetime模块
dt=data_new['Order Date'].astype(str) #转换成字符串格式
dt = dt.apply(lambda x:datetime.strptime(x, '%Y-%m-%d'))
data_new['month'] = dt.map(lambda x: x.month) #获取月份，并添加列month
data_new['year']=dt.map(lambda x:x.year) #获取年份，并添加列year
```

1）选择子集，选择销售分析子集数据


```python
#选取销售分析数据子集
sales_data=data_new[['Order Date','Sales','Profit','year','month']]
sales_data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order Date</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>year</th>
      <th>month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2011-01-01</td>
      <td>408.300</td>
      <td>106.140</td>
      <td>2011</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2011-01-01</td>
      <td>120.366</td>
      <td>36.036</td>
      <td>2011</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2011-01-01</td>
      <td>66.120</td>
      <td>29.640</td>
      <td>2011</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2011-01-01</td>
      <td>44.865</td>
      <td>-26.055</td>
      <td>2011</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2011-01-01</td>
      <td>113.670</td>
      <td>37.770</td>
      <td>2011</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
#导入matplotlib进行图表可视化展示
import matplotlib.pyplot as plt
% matplotlib inline
```


```python
#整体浏览
fig=plt.figure(figsize=(20,3))
sales_tem=sales_data[['Order Date','Sales','Profit']]
sales_tem.index=sales_tem['Order Date'].astype('object')
sales_tem[['Sales','Profit']].plot(kind='line',style='--g.',colormap='Accent_r',
                                  figsize=(10,4),title='four years Sales and Profit table',)
plt.grid()
```


    <matplotlib.figure.Figure at 0x11d4d06d8>



![png](output_13_1.png)



```python
#计算年度&月度销售额/利润
#第一步：将数据采用groupby根据year和month进行分组
gb=sales_data.groupby(['year','month'])
#第二步：将分组后的数据进行求和，得到不同年份不同月份的销售额
sales_year=gb.sum()
sales_year
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Sales</th>
      <th>Profit</th>
    </tr>
    <tr>
      <th>year</th>
      <th>month</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="12" valign="top">2011</th>
      <th>1</th>
      <td>98898.48886</td>
      <td>8321.80096</td>
    </tr>
    <tr>
      <th>2</th>
      <td>91152.15698</td>
      <td>12417.90698</td>
    </tr>
    <tr>
      <th>3</th>
      <td>145729.36736</td>
      <td>15303.56826</td>
    </tr>
    <tr>
      <th>4</th>
      <td>116915.76418</td>
      <td>12902.32438</td>
    </tr>
    <tr>
      <th>5</th>
      <td>146747.83610</td>
      <td>12183.82870</td>
    </tr>
    <tr>
      <th>6</th>
      <td>215207.38022</td>
      <td>23415.24702</td>
    </tr>
    <tr>
      <th>7</th>
      <td>115510.41912</td>
      <td>5585.00352</td>
    </tr>
    <tr>
      <th>8</th>
      <td>207581.49122</td>
      <td>23713.66772</td>
    </tr>
    <tr>
      <th>9</th>
      <td>290214.45534</td>
      <td>35776.88394</td>
    </tr>
    <tr>
      <th>10</th>
      <td>199071.26404</td>
      <td>25963.41834</td>
    </tr>
    <tr>
      <th>11</th>
      <td>298496.53752</td>
      <td>32709.17772</td>
    </tr>
    <tr>
      <th>12</th>
      <td>333925.73460</td>
      <td>40647.98400</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">2012</th>
      <th>1</th>
      <td>135780.72024</td>
      <td>10401.63764</td>
    </tr>
    <tr>
      <th>2</th>
      <td>100510.21698</td>
      <td>15000.09618</td>
    </tr>
    <tr>
      <th>3</th>
      <td>163076.77116</td>
      <td>17992.91756</td>
    </tr>
    <tr>
      <th>4</th>
      <td>161052.26952</td>
      <td>17366.96722</td>
    </tr>
    <tr>
      <th>5</th>
      <td>208364.89124</td>
      <td>29876.70374</td>
    </tr>
    <tr>
      <th>6</th>
      <td>256175.69842</td>
      <td>34407.15362</td>
    </tr>
    <tr>
      <th>7</th>
      <td>145236.78512</td>
      <td>15585.38842</td>
    </tr>
    <tr>
      <th>8</th>
      <td>303142.94238</td>
      <td>43573.87858</td>
    </tr>
    <tr>
      <th>9</th>
      <td>289389.16564</td>
      <td>27776.18034</td>
    </tr>
    <tr>
      <th>10</th>
      <td>252939.85020</td>
      <td>30662.88270</td>
    </tr>
    <tr>
      <th>11</th>
      <td>323512.41690</td>
      <td>31820.72180</td>
    </tr>
    <tr>
      <th>12</th>
      <td>338256.96660</td>
      <td>32950.75130</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">2013</th>
      <th>1</th>
      <td>199185.90738</td>
      <td>26810.55968</td>
    </tr>
    <tr>
      <th>2</th>
      <td>167239.65040</td>
      <td>23762.49610</td>
    </tr>
    <tr>
      <th>3</th>
      <td>198594.03012</td>
      <td>23433.77462</td>
    </tr>
    <tr>
      <th>4</th>
      <td>177821.31684</td>
      <td>19462.03844</td>
    </tr>
    <tr>
      <th>5</th>
      <td>260498.56470</td>
      <td>28495.69410</td>
    </tr>
    <tr>
      <th>6</th>
      <td>396519.61190</td>
      <td>45478.41340</td>
    </tr>
    <tr>
      <th>7</th>
      <td>229928.95200</td>
      <td>28863.82720</td>
    </tr>
    <tr>
      <th>8</th>
      <td>326488.78936</td>
      <td>31023.66846</td>
    </tr>
    <tr>
      <th>9</th>
      <td>376619.24568</td>
      <td>38905.66778</td>
    </tr>
    <tr>
      <th>10</th>
      <td>293406.64288</td>
      <td>42433.22258</td>
    </tr>
    <tr>
      <th>11</th>
      <td>373989.36010</td>
      <td>48062.99670</td>
    </tr>
    <tr>
      <th>12</th>
      <td>405454.37802</td>
      <td>50202.87112</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">2014</th>
      <th>1</th>
      <td>241268.55566</td>
      <td>28001.38626</td>
    </tr>
    <tr>
      <th>2</th>
      <td>184837.35556</td>
      <td>19751.69996</td>
    </tr>
    <tr>
      <th>3</th>
      <td>263100.77262</td>
      <td>37357.26052</td>
    </tr>
    <tr>
      <th>4</th>
      <td>242771.86130</td>
      <td>23782.30120</td>
    </tr>
    <tr>
      <th>5</th>
      <td>288401.04614</td>
      <td>33953.55774</td>
    </tr>
    <tr>
      <th>6</th>
      <td>401814.06310</td>
      <td>43778.60280</td>
    </tr>
    <tr>
      <th>7</th>
      <td>258705.68048</td>
      <td>28035.87258</td>
    </tr>
    <tr>
      <th>8</th>
      <td>456619.94236</td>
      <td>53542.89496</td>
    </tr>
    <tr>
      <th>9</th>
      <td>481157.24370</td>
      <td>67979.45110</td>
    </tr>
    <tr>
      <th>10</th>
      <td>422766.62916</td>
      <td>58209.83476</td>
    </tr>
    <tr>
      <th>11</th>
      <td>555279.02700</td>
      <td>62856.58790</td>
    </tr>
    <tr>
      <th>12</th>
      <td>503143.69348</td>
      <td>46916.52068</td>
    </tr>
  </tbody>
</table>
</div>




```python
year_2011=sales_year.loc[(2011,slice(None)),:].reset_index()
year_2012=sales_year.loc[(2012,slice(None)),:].reset_index()
year_2013=sales_year.loc[(2013,slice(None)),:].reset_index()
year_2014=sales_year.loc[(2014,slice(None)),:].reset_index()
year_2011
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>month</th>
      <th>Sales</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2011</td>
      <td>1</td>
      <td>98898.48886</td>
      <td>8321.80096</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2011</td>
      <td>2</td>
      <td>91152.15698</td>
      <td>12417.90698</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2011</td>
      <td>3</td>
      <td>145729.36736</td>
      <td>15303.56826</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2011</td>
      <td>4</td>
      <td>116915.76418</td>
      <td>12902.32438</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2011</td>
      <td>5</td>
      <td>146747.83610</td>
      <td>12183.82870</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2011</td>
      <td>6</td>
      <td>215207.38022</td>
      <td>23415.24702</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2011</td>
      <td>7</td>
      <td>115510.41912</td>
      <td>5585.00352</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2011</td>
      <td>8</td>
      <td>207581.49122</td>
      <td>23713.66772</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2011</td>
      <td>9</td>
      <td>290214.45534</td>
      <td>35776.88394</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2011</td>
      <td>10</td>
      <td>199071.26404</td>
      <td>25963.41834</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2011</td>
      <td>11</td>
      <td>298496.53752</td>
      <td>32709.17772</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2011</td>
      <td>12</td>
      <td>333925.73460</td>
      <td>40647.98400</td>
    </tr>
  </tbody>
</table>
</div>




```python
#构建销售表
sales=pd.concat([year_2011['Sales'],year_2012['Sales'],
                 year_2013['Sales'],year_2014['Sales']],axis=1)
sales.columns=['Sales-2011','Sales-2012','Sales-2013','Sales-2014']
sales.index=['Jau','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
sales
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sales-2011</th>
      <th>Sales-2012</th>
      <th>Sales-2013</th>
      <th>Sales-2014</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Jau</th>
      <td>98898.48886</td>
      <td>135780.72024</td>
      <td>199185.90738</td>
      <td>241268.55566</td>
    </tr>
    <tr>
      <th>Feb</th>
      <td>91152.15698</td>
      <td>100510.21698</td>
      <td>167239.65040</td>
      <td>184837.35556</td>
    </tr>
    <tr>
      <th>Mar</th>
      <td>145729.36736</td>
      <td>163076.77116</td>
      <td>198594.03012</td>
      <td>263100.77262</td>
    </tr>
    <tr>
      <th>Apr</th>
      <td>116915.76418</td>
      <td>161052.26952</td>
      <td>177821.31684</td>
      <td>242771.86130</td>
    </tr>
    <tr>
      <th>May</th>
      <td>146747.83610</td>
      <td>208364.89124</td>
      <td>260498.56470</td>
      <td>288401.04614</td>
    </tr>
    <tr>
      <th>Jun</th>
      <td>215207.38022</td>
      <td>256175.69842</td>
      <td>396519.61190</td>
      <td>401814.06310</td>
    </tr>
    <tr>
      <th>Jul</th>
      <td>115510.41912</td>
      <td>145236.78512</td>
      <td>229928.95200</td>
      <td>258705.68048</td>
    </tr>
    <tr>
      <th>Aug</th>
      <td>207581.49122</td>
      <td>303142.94238</td>
      <td>326488.78936</td>
      <td>456619.94236</td>
    </tr>
    <tr>
      <th>Sep</th>
      <td>290214.45534</td>
      <td>289389.16564</td>
      <td>376619.24568</td>
      <td>481157.24370</td>
    </tr>
    <tr>
      <th>Oct</th>
      <td>199071.26404</td>
      <td>252939.85020</td>
      <td>293406.64288</td>
      <td>422766.62916</td>
    </tr>
    <tr>
      <th>Nov</th>
      <td>298496.53752</td>
      <td>323512.41690</td>
      <td>373989.36010</td>
      <td>555279.02700</td>
    </tr>
    <tr>
      <th>Dec</th>
      <td>333925.73460</td>
      <td>338256.96660</td>
      <td>405454.37802</td>
      <td>503143.69348</td>
    </tr>
  </tbody>
</table>
</div>




```python
#构建利润表
profit=pd.concat([year_2011['Profit'],year_2012['Profit'],
                 year_2013['Profit'],year_2014['Profit']],axis=1)
profit.columns=['Profit-2011','Profit-2012','Profit-2013','Profit-2014']
profit.index=['Jau','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
profit
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Profit-2011</th>
      <th>Profit-2012</th>
      <th>Profit-2013</th>
      <th>Profit-2014</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Jau</th>
      <td>8321.80096</td>
      <td>10401.63764</td>
      <td>26810.55968</td>
      <td>28001.38626</td>
    </tr>
    <tr>
      <th>Feb</th>
      <td>12417.90698</td>
      <td>15000.09618</td>
      <td>23762.49610</td>
      <td>19751.69996</td>
    </tr>
    <tr>
      <th>Mar</th>
      <td>15303.56826</td>
      <td>17992.91756</td>
      <td>23433.77462</td>
      <td>37357.26052</td>
    </tr>
    <tr>
      <th>Apr</th>
      <td>12902.32438</td>
      <td>17366.96722</td>
      <td>19462.03844</td>
      <td>23782.30120</td>
    </tr>
    <tr>
      <th>May</th>
      <td>12183.82870</td>
      <td>29876.70374</td>
      <td>28495.69410</td>
      <td>33953.55774</td>
    </tr>
    <tr>
      <th>Jun</th>
      <td>23415.24702</td>
      <td>34407.15362</td>
      <td>45478.41340</td>
      <td>43778.60280</td>
    </tr>
    <tr>
      <th>Jul</th>
      <td>5585.00352</td>
      <td>15585.38842</td>
      <td>28863.82720</td>
      <td>28035.87258</td>
    </tr>
    <tr>
      <th>Aug</th>
      <td>23713.66772</td>
      <td>43573.87858</td>
      <td>31023.66846</td>
      <td>53542.89496</td>
    </tr>
    <tr>
      <th>Sep</th>
      <td>35776.88394</td>
      <td>27776.18034</td>
      <td>38905.66778</td>
      <td>67979.45110</td>
    </tr>
    <tr>
      <th>Oct</th>
      <td>25963.41834</td>
      <td>30662.88270</td>
      <td>42433.22258</td>
      <td>58209.83476</td>
    </tr>
    <tr>
      <th>Nov</th>
      <td>32709.17772</td>
      <td>31820.72180</td>
      <td>48062.99670</td>
      <td>62856.58790</td>
    </tr>
    <tr>
      <th>Dec</th>
      <td>40647.98400</td>
      <td>32950.75130</td>
      <td>50202.87112</td>
      <td>46916.52068</td>
    </tr>
  </tbody>
</table>
</div>




```python
#计算2011-2014年年度总销售额及增长率

#计算年度销售额并图表展示
sales_sum=sales.sum()
sales_sum.plot(kind='bar',colormap = 'RdYlGn_r',alpha=0.5)
plt.grid()

#计算每年增长率
rise_12=sales_sum[1]/sales_sum[0]-1
rise_13=sales_sum[2]/sales_sum[1]-1
rise_14=sales_sum[3]/sales_sum[2]-1
rise_rate=[0,rise_12,rise_13,rise_14]

#表格显示增长率
sales_sum=pd.DataFrame({'sales_sum':sales_sum})
sales_sum['rise_rate']=rise_rate
sales_sum
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sales_sum</th>
      <th>rise_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Sales-2011</th>
      <td>2.259451e+06</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Sales-2012</th>
      <td>2.677439e+06</td>
      <td>0.184995</td>
    </tr>
    <tr>
      <th>Sales-2013</th>
      <td>3.405746e+06</td>
      <td>0.272017</td>
    </tr>
    <tr>
      <th>Sales-2014</th>
      <td>4.299866e+06</td>
      <td>0.262533</td>
    </tr>
  </tbody>
</table>
</div>




![png](output_18_1.png)



```python
sales.style.background_gradient(cmap='Greens',axis =0)
```


```python
sales.plot.area(colormap = 'Accent_r',stacked=False)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11d3fe048>




![png](output_20_1.png)



```python
#计算每月同比增长率
rise=pd.DataFrame()
rise['rise_2012']=(sales['Sales-2012']-sales['Sales-2011'])/sales['Sales-2011']
rise['rise_2013']=(sales['Sales-2013']-sales['Sales-2012'])/sales['Sales-2012']
rise['rise_2014']=(sales['Sales-2014']-sales['Sales-2013'])/sales['Sales-2013']
rise

# 色彩映射
rise.style.background_gradient(cmap='Greens',axis =1,low=0,high=1)
# cmap：颜色; axis：映射参考，0为行，1以列
```

 
```python
#计算2011年个月份销售占比及贡献最大月份
sales_11_sort=sales['Sales-2011'].sort_values(ascending=False)

sales_11_sort.plot(kind='bar',color='g',alpha=0.5,figsize=(10,6))
plt.ylabel('monthly sales of 2011')

p=sales_11_sort.cumsum()/sales_11_sort.sum()  #创建累计占比，Series
key=p[p>0.8].index[0]
key_num=sales_11_sort.index.tolist().index(key)
print('超过80%累计占比的节点值索引为：' ,key)

p.plot(style='--ko', secondary_y=True) #y副坐标轴
plt.axvline(key_num,hold=None,color='r',linestyle='--',alpha=0.8)
plt.text(key_num+0.2,p[key],'cumulative proportion: %.3f%%' %(p[key]*100),color='r')
plt.ylabel('proportion of cumulative sales')

key_num = sales_11_sort[:key_num+1]
print('核心月份为：')
print(key_num)
# 输出决定性因素产品
```

    超过80%累计占比的节点值索引为： Mar
    核心月份为：
    Dec    333925.73460
    Nov    298496.53752
    Sep    290214.45534
    Jun    215207.38022
    Aug    207581.49122
    Oct    199071.26404
    May    146747.83610
    Mar    145729.36736
    Name: Sales-2011, dtype: float64



![png](output_22_1.png)



```python
#计算2012年个月份销售占比及贡献最大月份
sales_12_sort=sales['Sales-2012'].sort_values(ascending=False)

sales_12_sort.plot(kind='bar',color='g',alpha=0.5,figsize=(10,6))
plt.ylabel('monthly sales of 2012')

p=sales_12_sort.cumsum()/sales_12_sort.sum()  #创建累计占比，Series
key=p[p>0.8].index[0]
key_num=sales_12_sort.index.tolist().index(key)
print('超过80%累计占比的节点值索引为：' ,key)

p.plot(style='--ko', secondary_y=True) #y副坐标轴
plt.axvline(key_num,hold=None,color='r',linestyle='--',alpha=0.8)
plt.text(key_num+0.2,p[key],'cumulative proportion: %.3f%%' %(p[key]*100),color='r')
plt.ylabel('proportion of cumulative sales')

key_num = sales_12_sort[:key_num+1]
print('核心月份为：')
print(key_num)
# 输出决定性因素产品
```

    超过80%累计占比的节点值索引为： Apr
    核心月份为：
    Dec    338256.96660
    Nov    323512.41690
    Aug    303142.94238
    Sep    289389.16564
    Jun    256175.69842
    Oct    252939.85020
    May    208364.89124
    Mar    163076.77116
    Apr    161052.26952
    Name: Sales-2012, dtype: float64



![png](output_23_1.png)



```python
#计算2013年个月份销售占比及贡献最大月份
sales_13_sort=sales['Sales-2013'].sort_values(ascending=False)

sales_13_sort.plot(kind='bar',color='g',alpha=0.5,figsize=(10,6))
plt.ylabel('monthly sales of 2013')

p=sales_13_sort.cumsum()/sales_13_sort.sum()  #创建累计占比，Series
key=p[p>0.8].index[0]
key_num=sales_13_sort.index.tolist().index(key)
print('超过80%累计占比的节点值索引为：' ,key)

p.plot(style='--ko', secondary_y=True) #y副坐标轴
plt.axvline(key_num,hold=None,color='r',linestyle='--',alpha=0.8)
plt.text(key_num+0.2,p[key],'cumulative proportion: %.3f%%' %(p[key]*100),color='r')
plt.ylabel('proportion of cumulative sales')

key_num = sales_13_sort[:key_num+1]
print('核心月份为：')
print(key_num)
# 输出决定性因素产品
```

    超过80%累计占比的节点值索引为： Jau
    核心月份为：
    Dec    405454.37802
    Jun    396519.61190
    Sep    376619.24568
    Nov    373989.36010
    Aug    326488.78936
    Oct    293406.64288
    May    260498.56470
    Jul    229928.95200
    Jau    199185.90738
    Name: Sales-2013, dtype: float64



![png](output_24_1.png)



```python
#计算2014年个月份销售占比及贡献最大月份
sales_14_sort=sales['Sales-2014'].sort_values(ascending=False)

sales_14_sort.plot(kind='bar',color='g',alpha=0.5,figsize=(10,6))
plt.ylabel('monthly sales of 2014')

p=sales_14_sort.cumsum()/sales_14_sort.sum()  #创建累计占比，Series
key=p[p>0.8].index[0]
key_num=sales_14_sort.index.tolist().index(key)
print('超过80%累计占比的节点值索引为：' ,key)

p.plot(style='--ko', secondary_y=True) #y副坐标轴
plt.axvline(key_num,hold=None,color='r',linestyle='--',alpha=0.8)
plt.text(key_num+0.2,p[key],'cumulative proportion: %.3f%%' %(p[key]*100),color='r')
plt.ylabel('proportion of cumulative sales')

key_num = sales_14_sort[:key_num+1]
print('核心月份为：')
print(key_num)
# 输出决定性因素产品
```

    超过80%累计占比的节点值索引为： Jul
    核心月份为：
    Nov    555279.02700
    Dec    503143.69348
    Sep    481157.24370
    Aug    456619.94236
    Oct    422766.62916
    Jun    401814.06310
    May    288401.04614
    Mar    263100.77262
    Jul    258705.68048
    Name: Sales-2014, dtype: float64



![png](output_25_1.png)



```python
#计算2011-2014年年度总利润及增长率

#计算年度总利润并图表展示
profit_sum=profit.sum()
profit_sum.plot(kind='bar',colormap = 'RdYlGn_r',alpha=0.5)
plt.grid()

#计算每年增长率
rise_12=profit_sum[1]/profit_sum[0]-1
rise_13=profit_sum[2]/profit_sum[1]-1
rise_14=profit_sum[3]/profit_sum[2]-1
rise_rate=[0,rise_12,rise_13,rise_14]

#表格显示增长率
profit_sum=pd.DataFrame({'profit_sum':profit_sum})
profit_sum['rise_rate']=rise_rate
profit_sum
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>profit_sum</th>
      <th>rise_rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Profit-2011</th>
      <td>248940.81154</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>Profit-2012</th>
      <td>307415.27910</td>
      <td>0.234893</td>
    </tr>
    <tr>
      <th>Profit-2013</th>
      <td>406935.23018</td>
      <td>0.323731</td>
    </tr>
    <tr>
      <th>Profit-2014</th>
      <td>504165.97046</td>
      <td>0.238934</td>
    </tr>
  </tbody>
</table>
</div>

![png](output_26_1.png)


```python
profit.style.background_gradient(cmap='Greens',axis =0)
```
   
```python
profit.plot.area(colormap = 'Accent_r',stacked=False)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11fb23f60>




![png](output_28_1.png)



```python
#计算每月同比增长率
rise_p=pd.DataFrame()
rise_p['rise_2012']=(profit['Profit-2012']-profit['Profit-2011'])/profit['Profit-2011']
rise_p['rise_2013']=(profit['Profit-2013']-profit['Profit-2012'])/profit['Profit-2012']
rise_p['rise_2014']=(profit['Profit-2014']-profit['Profit-2013'])/profit['Profit-2013']
rise
```
# 色彩映射
rise_p.style.background_gradient(cmap='Greens',axis =1,low=0,high=1)
# cmap：颜色; axis：映射参考，0为行，1以列

```python
profit_rate=pd.DataFrame()
profit_rate['p-rate-11']=profit['Profit-2011']/sales['Sales-2011']
```


```python
profit_rate_2011=profit['Profit-2011']/sales['Sales-2011']
sales['Sales-2011'].plot(kind='bar',color='g',alpha=0.5)
profit['Profit-2011'].plot(kind='bar',color='g',alpha=0.7)
profit_rate_2011.plot(style='--r.', secondary_y=True,alpha=0.5,label='profit_rate_2011')
plt.legend(loc='upper center')
plt.grid()
```


![png](output_31_0.png)



```python
profit_rate_2012=profit['Profit-2012']/sales['Sales-2012']
sales['Sales-2012'].plot(kind='bar',color='g',alpha=0.5)
profit['Profit-2012'].plot(kind='bar',color='g',alpha=0.7)
profit_rate_2012.plot(style='--r.', secondary_y=True,alpha=0.5,label='profit_rate_2012')
plt.legend(loc='best')
plt.grid()
```


![png](output_32_0.png)



```python
profit_rate_2013=profit['Profit-2013']/sales['Sales-2013']
sales['Sales-2013'].plot(kind='bar',color='g',alpha=0.5)
profit['Profit-2013'].plot(kind='bar',color='g',alpha=0.7)
profit_rate_2013.plot(style='--r.', secondary_y=True,alpha=0.5,label='profit_rate_2013')
plt.legend(loc='best')
plt.grid()
```


![png](output_33_0.png)



```python
profit_rate_2014=profit['Profit-2014']/sales['Sales-2014']
sales['Sales-2014'].plot(kind='bar',color='g',alpha=0.5)
profit['Profit-2014'].plot(kind='bar',color='g',alpha=0.7)
profit_rate_2014.plot(style='--r.', secondary_y=True,alpha=0.5,label='profit_rate_2014')
plt.legend(loc='best')
plt.grid()
```


![png](output_34_0.png)



```python

```
