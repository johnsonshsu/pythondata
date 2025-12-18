import pandas as pd

# 地區名稱翻譯對照表
region_translation = {
    "Arab World": "阿拉伯世界",
    "Caribbean small states": "加勒比海小型國家",
    "Central Europe and the Baltics": "中歐與波羅的海地區",
    "Early-demographic dividend": "早期人口紅利國家",
    "East Asia & Pacific": "東亞與太平洋地區",
    "East Asia & Pacific (excluding high income)": "東亞與太平洋地區(不含高收入)",
    "East Asia & Pacific (IDA & IBRD countries)": "東亞與太平洋地區(IDA及IBRD國家)",
    "Euro area": "歐元區",
    "Europe & Central Asia": "歐洲與中亞地區",
    "Europe & Central Asia (excluding high income)": "歐洲與中亞地區(不含高收入)",
    "Europe & Central Asia (IDA & IBRD countries)": "歐洲與中亞地區(IDA及IBRD國家)",
    "European Union": "歐洲聯盟",
    "Fragile and conflict affected situations": "脆弱與衝突影響地區",
    "Heavily indebted poor countries (HIPC)": "重債窮國",
    "High income": "高收入國家",
    "IBRD only": "僅國際復興開發銀行",
    "IDA & IBRD total": "國際開發協會與國際復興開發銀行總計",
    "IDA blend": "國際開發協會混合",
    "IDA only": "僅國際開發協會",
    "IDA total": "國際開發協會總計",
    "Late-demographic dividend": "後期人口紅利國家",
    "Latin America & Caribbean": "拉丁美洲與加勒比海地區",
    "Latin America & Caribbean (excluding high income)": "拉丁美洲與加勒比海地區(不含高收入)",
    "Latin America & Caribbean (IDA & IBRD countries)": "拉丁美洲與加勒比海地區(IDA及IBRD國家)",
    "Least developed countries: UN classification": "最低度開發國家(聯合國分類)",
    "Low & middle income": "低收入與中等收入國家",
    "Low income": "低收入國家",
    "Lower middle income": "中低收入國家",
    "Middle East & North Africa": "中東與北非地區",
    "Middle East & North Africa (excluding high income)": "中東與北非地區(不含高收入)",
    "Middle East & North Africa (IDA & IBRD countries)": "中東與北非地區(IDA及IBRD國家)",
    "Middle income": "中等收入國家",
    "North America": "北美洲",
    "OECD members": "經濟合作暨發展組織會員國",
    "Other small states": "其他小型國家",
    "Pacific island small states": "太平洋島國小型國家",
    "Post-demographic dividend": "後人口紅利國家",
    "Pre-demographic dividend": "前人口紅利國家",
    "Small states": "小型國家",
    "South Asia": "南亞地區",
    "South Asia (IDA & IBRD)": "南亞地區(IDA及IBRD)",
    "Sub-Saharan Africa": "撒哈拉以南非洲地區",
    "Sub-Saharan Africa (excluding high income)": "撒哈拉以南非洲地區(不含高收入)",
    "Sub-Saharan Africa (IDA & IBRD countries)": "撒哈拉以南非洲地區(IDA及IBRD國家)",
    "Upper middle income": "中高收入國家",
    "World": "全球",
}

# 指標名稱翻譯對照表
indicator_translation = {
    "Agriculture, value added (% of GDP)": "農業增加值(佔GDP百分比)",
    "CO2 emissions (metric tons per capita)": "二氧化碳排放量(每人公噸)",
    "Domestic credit provided by financial sector (% of GDP)": "金融部門提供之國內信貸(佔GDP百分比)",
    "Electric power consumption (kWh per capita)": "電力消耗(每人千瓦時)",
    "Energy use (kg of oil equivalent per capita)": "能源使用量(每人石油當量公斤)",
    "Exports of goods and services (% of GDP)": "商品與服務出口(佔GDP百分比)",
    "Fertility rate, total (births per woman)": "總生育率(每名婦女生育數)",
    "GDP growth (annual %)": "GDP成長率(年增率%)",
    "Imports of goods and services (% of GDP)": "商品與服務進口(佔GDP百分比)",
    "Industry, value added (% of GDP)": "工業增加值(佔GDP百分比)",
    "Inflation, GDP deflator (annual %)": "通貨膨脹率-GDP平減指數(年增率%)",
    "Life expectancy at birth, total (years)": "出生時預期壽命(歲)",
    "Population density (people per sq. km of land area)": "人口密度(每平方公里人數)",
    "Services, etc., value added (% of GDP)": "服務業等增加值(佔GDP百分比)",
}

# 讀取CSV檔案
print("正在讀取CSV檔案...")
df = pd.read_csv('csv/country_indicators.csv')

print(f"原始資料筆數: {len(df)}")
print(f"原始欄位: {df.columns.tolist()}")

# 執行翻譯
print("\n正在翻譯地區名稱...")
df['地區名稱'] = df['地區名稱'].map(region_translation).fillna(df['地區名稱'])

print("正在翻譯指標名稱...")
df['指標名稱'] = df['指標名稱'].map(indicator_translation).fillna(df['指標名稱'])

# 儲存翻譯後的檔案
output_file = 'csv/country_indicators_translated.csv'
print(f"\n正在儲存翻譯後的檔案至: {output_file}")
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print("翻譯完成!")

# 顯示統計資訊
print("\n翻譯統計:")
print(f"地區種類數: {df['地區名稱'].nunique()}")
print(f"指標種類數: {df['指標名稱'].nunique()}")
print(f"\n前10個地區名稱:")
print(df['地區名稱'].value_counts().head(10))
print(f"\n所有指標名稱:")
print(df['指標名稱'].unique())
