import pandas as pd
import re

# 讀取 CSV
df = pd.read_csv('csv/country_indicators.csv')

# 檢查是否有英文字母（排除括號內的英文縮寫如 GDP, IDA, IBRD）
def has_english(text):
    if pd.isna(text):
        return False
    # 移除括號內容後再檢查
    text_without_parens = re.sub(r'\([^)]*\)', '', str(text))
    # 檢查是否有連續3個以上的英文字母
    return bool(re.search(r'[A-Za-z]{3,}', text_without_parens))

# 檢查地區名稱
regions_with_english = df[df['地區名稱'].apply(has_english)]['地區名稱'].unique()
print(f'含有英文的地區名稱數量: {len(regions_with_english)}')
print('\n前30個範例:')
for r in list(regions_with_english)[:30]:
    print(f'  {r}')

print('\n' + '='*80 + '\n')

# 檢查指標名稱
indicators_with_english = df[df['指標名稱'].apply(has_english)]['指標名稱'].unique()
print(f'含有英文的指標名稱數量: {len(indicators_with_english)}')
print('\n所有範例:')
for i in list(indicators_with_english):
    print(f'  {i}')

# 儲存完整清單到檔案
with open('untranslated_items.txt', 'w', encoding='utf-8') as f:
    f.write('=== 未翻譯的地區名稱 ===\n\n')
    for r in sorted(regions_with_english):
        f.write(f'{r}\n')

    f.write('\n\n=== 未翻譯的指標名稱 ===\n\n')
    for i in sorted(indicators_with_english):
        f.write(f'{i}\n')

print(f'\n完整清單已儲存到 untranslated_items.txt')
