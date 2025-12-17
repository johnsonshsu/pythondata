import csv

# 洲別翻譯對應
continent_translation = {
    'Africa': '非洲',
    'Americas': '美洲',
    'Asia': '亞洲',
    'Europe': '歐洲',
    'FSU': '前蘇聯',
    'Oceania': '大洋洲'
}

# 讀取並翻譯 CSV
input_file = 'gapminder_unfiltered.csv'
output_file = 'gapminder_unfiltered_translated.csv'

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8', newline='') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 處理標題行
    header = next(reader)
    writer.writerow(header)

    # 處理資料行
    translated_count = 0
    for row in reader:
        if len(row) >= 2:
            # 翻譯洲別欄位(索引 1)
            if row[1] in continent_translation:
                row[1] = continent_translation[row[1]]
                translated_count += 1
        writer.writerow(row)

print(f'翻譯完成!')
print(f'已翻譯 {translated_count} 筆資料')
print(f'輸出檔案: {output_file}')
print(f'\n洲別翻譯對應:')
for eng, chi in continent_translation.items():
    print(f'  {eng} → {chi}')
