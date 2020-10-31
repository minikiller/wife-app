import sys,time
import process
import pandas as pd
import numpy as np


print("程序初始化中...")
fd = pd.read_excel("./大病新表.xlsx", sheet_name="Sheet1")
fd.fillna(0, inplace=True)
source_total = fd.shape[0]
print("读取大病新表成功,共计{}条数据!".format(source_total))

target = pd.read_excel("./base.xls", sheet_name="Sheet1")
target.fillna(0, inplace=True)
target_total = target.shape[0]
# target[['借支金额']].fillna(0, inplace=True)
# target[['还款金额','借支金额']]=target[['还款金额','借支金额']].fillna(0, inplace=True)
# target.info()
print("读取base成功,共计{}条数据!".format(target_total))
print("-----------------------------------")
result = pd.DataFrame(columns=fd.columns)  # 错误结果
matched = pd.DataFrame(columns=fd.columns)  # 正确结果
drop_index = []  # 记录需要删除对行号
print("开始比对...")
max_steps = target_total
process_bar = process.ShowProcess(max_steps, '比对结束！')
for idx, row in target.iterrows():
    # print(type(row))
    # print(row["住院号"])
    fil = (fd["住院号"] == row["住院号"]) \
        & (fd["科室"] == row["科室"]) \
        & (fd["姓名"] == row["姓名"]) \
        & (fd["借支金额"] == row["借支金额"]) \
        & (fd["还款金额"] == row["还款金额"]) \
        & (fd["还款金额.1"] == row["还款金额.1"]) \
        & (fd["还款金额.2"] == row["还款金额.2"])
    _temp = fd[fil]
    if len(_temp) == 0:  # can not match
        # print("{} is false".format(idx))
        result.loc[len(result)] = row
    else:
        # print("{} is true,fd index is {}".format(idx,_temp.index.tolist()))
        matched.loc[len(matched)] = row
        drop_index.extend(_temp.index.tolist())
    process_bar.show_process()
    time.sleep(0.01)
# print(result)
# write to error
result.replace(0, np.nan, inplace=True)
result.to_excel("./result.xlsx", sheet_name="Sheet1", index=False)

matched.replace(0, np.nan, inplace=True)
matched.to_excel("./matched.xlsx", sheet_name="Sheet1", index=False)
# print(drop_index)

left = fd.drop(drop_index)  # 剩余对比结果
target.replace(0, np.nan, inplace=True)
left.to_excel("./left.xlsx", sheet_name="Sheet1", index=False)

print("对比结果如下：")
print("-----------------------------------")
print("一共对比记录："+str(target.shape[0]))
print("其中，正确比对合计："+str(matched.shape[0]))
print("错误对比结果合计："+str(result.shape[0]))
print("原始结果合计："+str(fd.shape[0]))
print("剩余对比结果合计："+str(left.shape[0]))
print("-----------------------------------")
print("最后产生三个文件：")
print("错误结果：result.xlsx")
print("正确结果：matched.xlsx")
print("剩余结果：left.xlsx")
print("-----------------------------------")
price_str = input("按任意键退出程序!")
sys.exit(0)
