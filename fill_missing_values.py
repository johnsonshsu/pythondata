import csv

# 讀取原始 CSV 檔案
input_file = r'd:\Python\demo\pythondata\csv\country_indicators.csv'
output_file = r'd:\Python\demo\pythondata\csv\country_indicators.csv'

rows = []
with open(input_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows.append(header)

    # 處理每一行資料
    for row in reader:
        if len(row) == 4:
            # 如果數值欄位(第4個欄位)是空的,填入 0
            if row[3].strip() == '':
                row[3] = '0'
        rows.append(row)

# 寫入處理後的資料
with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f'處理完成!已將空白數值填入 0')
print(f'總共處理了 {len(rows)-1} 筆資料')
