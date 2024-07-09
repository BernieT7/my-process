import pandas as pd


data = pd.read_csv("數據分析bypandas/college.csv")
new_data = data.groupby("學校名稱")[["在學學生數小計", "在學學生數女", "在學學生數男"]].sum()
new_data["女生比例"] = round((new_data["在學學生數女"]/new_data["在學學生數小計"])*100, 0)
new_data["男生比例"] = round((new_data["在學學生數男"]/new_data["在學學生數小計"])*100, 0)
new_data = new_data.sort_values(by="男生比例")
new_data["女生比例"] = new_data["女生比例"].astype(str) + "%"
new_data["男生比例"] = new_data["男生比例"].astype(str) + "%"
new_data.to_csv("數據分析bypandas/大學男女比.csv")