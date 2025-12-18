"""
國家/地區名稱翻譯對照表及批次更新工具
"""
import pandas as pd

# 完整的英文到繁體中文翻譯對照表
translation_dict = {
    "Afghanistan": "阿富汗",
    "Albania": "阿爾巴尼亞",
    "Algeria": "阿爾及利亞",
    "American Samoa": "美屬薩摩亞",
    "Andorra": "安道爾",
    "Angola": "安哥拉",
    "Antigua and Barbuda": "安地卡及巴布達",
    "Argentina": "阿根廷",
    "Armenia": "亞美尼亞",
    "Aruba": "阿魯巴",
    "Australia": "澳洲",
    "Austria": "奧地利",
    "Azerbaijan": "亞塞拜然",
    "Bahamas, The": "巴哈馬",
    "Bahrain": "巴林",
    "Bangladesh": "孟加拉",
    "Barbados": "巴貝多",
    "Belarus": "白俄羅斯",
    "Belgium": "比利時",
    "Belize": "貝里斯",
    "Benin": "貝南",
    "Bermuda": "百慕達",
    "Bhutan": "不丹",
    "Bolivia": "玻利維亞",
    "Bosnia and Herzegovina": "波士尼亞與赫塞哥維納",
    "Botswana": "波札那",
    "Brazil": "巴西",
    "British Virgin Islands": "英屬維京群島",
    "Brunei Darussalam": "汶萊",
    "Bulgaria": "保加利亞",
    "Burkina Faso": "布吉納法索",
    "Burundi": "蒲隆地",
    "Cabo Verde": "維德角",
    "Cambodia": "柬埔寨",
    "Cameroon": "喀麥隆",
    "Canada": "加拿大",
    "Cayman Islands": "開曼群島",
    "Central African Republic": "中非共和國",
    "Chad": "查德",
    "Channel Islands": "英吉利海峽群島",
    "Chile": "智利",
    "China": "中國",
    "Colombia": "哥倫比亞",
    "Comoros": "葛摩",
    "Congo, Dem. Rep.": "剛果民主共和國",
    "Congo, Rep.": "剛果共和國",
    "Costa Rica": "哥斯大黎加",
    "Cote d'Ivoire": "象牙海岸",
    "Croatia": "克羅埃西亞",
    "Cuba": "古巴",
    "Curacao": "古拉索",
    "Cyprus": "賽普勒斯",
    "Czech Republic": "捷克",
    "Denmark": "丹麥",
    "Djibouti": "吉布地",
    "Dominica": "多米尼克",
    "Dominican Republic": "多明尼加",
    "Ecuador": "厄瓜多",
    "Egypt, Arab Rep.": "埃及",
    "El Salvador": "薩爾瓦多",
    "Equatorial Guinea": "赤道幾內亞",
    "Eritrea": "厄利垂亞",
    "Estonia": "愛沙尼亞",
    "Ethiopia": "衣索比亞",
    "Faroe Islands": "法羅群島",
    "Fiji": "斐濟",
    "Finland": "芬蘭",
    "France": "法國",
    "French Polynesia": "法屬玻里尼西亞",
    "Gabon": "加彭",
    "Gambia, The": "甘比亞",
    "Georgia": "喬治亞",
    "Germany": "德國",
    "Ghana": "迦納",
    "Gibraltar": "直布羅陀",
    "Greece": "希臘",
    "Greenland": "格陵蘭",
    "Grenada": "格瑞那達",
    "Guam": "關島",
    "Guatemala": "瓜地馬拉",
    "Guinea": "幾內亞",
    "Guinea-Bissau": "幾內亞比索",
    "Guyana": "蓋亞那",
    "Haiti": "海地",
    "Honduras": "宏都拉斯",
    "Hong Kong SAR, China": "中國香港特別行政區",
    "Hungary": "匈牙利",
    "Iceland": "冰島",
    "India": "印度",
    "Indonesia": "印尼",
    "Iran, Islamic Rep.": "伊朗",
    "Iraq": "伊拉克",
    "Ireland": "愛爾蘭",
    "Isle of Man": "曼島",
    "Israel": "以色列",
    "Italy": "義大利",
    "Jamaica": "牙買加",
    "Japan": "日本",
    "Jordan": "約旦",
    "Kazakhstan": "哈薩克",
    "Kenya": "肯亞",
    "Kiribati": "吉里巴斯",
    "Korea, Dem. People's Rep.": "北韓",
    "Korea, Dem. People�s Rep.": "北韓",  # 處理編碼問題
    "Korea, Rep.": "南韓",
    "Kosovo": "科索沃",
    "Kuwait": "科威特",
    "Kyrgyz Republic": "吉爾吉斯",
    "Lao PDR": "寮國",
    "Latin America & the Caribbean (IDA & IBRD countries)": "拉丁美洲及加勒比海地區(IDA及IBRD國家)",
    "Latvia": "拉脫維亞",
    "Lebanon": "黎巴嫩",
    "Lesotho": "賴索托",
    "Liberia": "賴比瑞亞",
    "Libya": "利比亞",
    "Liechtenstein": "列支敦斯登",
    "Lithuania": "立陶宛",
    "Luxembourg": "盧森堡",
    "Macao SAR, China": "中國澳門特別行政區",
    "Macedonia, FYR": "北馬其頓",
    "Madagascar": "馬達加斯加",
    "Malawi": "馬拉威",
    "Malaysia": "馬來西亞",
    "Maldives": "馬爾地夫",
    "Mali": "馬利",
    "Malta": "馬爾他",
    "Marshall Islands": "馬紹爾群島",
    "Mauritania": "茅利塔尼亞",
    "Mauritius": "模里西斯",
    "Mexico": "墨西哥",
    "Micronesia, Fed. Sts.": "密克羅尼西亞聯邦",
    "Moldova": "摩爾多瓦",
    "Monaco": "摩納哥",
    "Mongolia": "蒙古",
    "Montenegro": "蒙特內哥羅",
    "Morocco": "摩洛哥",
    "Mozambique": "莫三比克",
    "Myanmar": "緬甸",
    "Namibia": "納米比亞",
    "Nauru": "諾魯",
    "Nepal": "尼泊爾",
    "Netherlands": "荷蘭",
    "New Caledonia": "新喀里多尼亞",
    "New Zealand": "紐西蘭",
    "Nicaragua": "尼加拉瓜",
    "Niger": "尼日",
    "Nigeria": "奈及利亞",
    "Northern Mariana Islands": "北馬里亞納群島",
    "Norway": "挪威",
    "Not classified": "未分類",
    "Oman": "阿曼",
    "Pakistan": "巴基斯坦",
    "Palau": "帛琉",
    "Panama": "巴拿馬",
    "Papua New Guinea": "巴布亞紐幾內亞",
    "Paraguay": "巴拉圭",
    "Peru": "秘魯",
    "Philippines": "菲律賓",
    "Poland": "波蘭",
    "Portugal": "葡萄牙",
    "Puerto Rico": "波多黎各",
    "Qatar": "卡達",
    "Romania": "羅馬尼亞",
    "Russian Federation": "俄羅斯聯邦",
    "Rwanda": "盧安達",
    "Samoa": "薩摩亞",
    "San Marino": "聖馬利諾",
    "Sao Tome and Principe": "聖多美普林西比",
    "Saudi Arabia": "沙烏地阿拉伯",
    "Senegal": "塞內加爾",
    "Serbia": "塞爾維亞",
    "Seychelles": "塞席爾",
    "Sierra Leone": "獅子山",
    "Singapore": "新加坡",
    "Sint Maarten (Dutch part)": "荷屬聖馬丁",
    "Slovak Republic": "斯洛伐克",
    "Slovenia": "斯洛維尼亞",
    "Solomon Islands": "索羅門群島",
    "Somalia": "索馬利亞",
    "South Africa": "南非",
    "South Sudan": "南蘇丹",
    "Spain": "西班牙",
    "Sri Lanka": "斯里蘭卡",
    "St. Kitts and Nevis": "聖克里斯多福及尼維斯",
    "St. Lucia": "聖露西亞",
    "St. Martin (French part)": "法屬聖馬丁",
    "St. Vincent and the Grenadines": "聖文森及格瑞那丁",
    "Sudan": "蘇丹",
    "Suriname": "蘇利南",
    "Swaziland": "史瓦帝尼",
    "Sweden": "瑞典",
    "Switzerland": "瑞士",
    "Syrian Arab Republic": "敘利亞",
    "Tajikistan": "塔吉克",
    "Tanzania": "坦尚尼亞",
    "Thailand": "泰國",
    "Timor-Leste": "東帝汶",
    "Togo": "多哥",
    "Tonga": "東加",
    "Trinidad and Tobago": "千里達及托巴哥",
    "Tunisia": "突尼西亞",
    "Turkey": "土耳其",
    "Turkmenistan": "土庫曼",
    "Turks and Caicos Islands": "土克凱可群島",
    "Tuvalu": "吐瓦魯",
    "Uganda": "烏干達",
    "Ukraine": "烏克蘭",
    "United Arab Emirates": "阿拉伯聯合大公國",
    "United Kingdom": "英國",
    "United States": "美國",
    "Uruguay": "烏拉圭",
    "Uzbekistan": "烏茲別克",
    "Vanuatu": "萬那杜",
    "Venezuela, RB": "委內瑞拉",
    "Vietnam": "越南",
    "Virgin Islands": "美屬維京群島",
    "West Bank and Gaza": "西岸及加薩",
    "Yemen, Rep.": "葉門",
    "Zambia": "尚比亞",
    "Zimbabwe": "辛巴威"
}

def translate_csv():
    """讀取並翻譯 CSV 檔案"""
    print("正在讀取 CSV 檔案...")
    df = pd.read_csv('csv/country_indicators.csv')

    print(f"檔案共有 {len(df)} 筆資料")
    print(f"翻譯對照表共有 {len(translation_dict)} 個項目")

    # 計算需要翻譯的項目
    before_count = df['地區名稱'].isin(translation_dict.keys()).sum()
    print(f"\n找到 {before_count} 筆需要翻譯的地區名稱")

    # 進行翻譯
    print("\n開始翻譯...")
    df['地區名稱'] = df['地區名稱'].replace(translation_dict)

    # 檢查翻譯結果
    import re
    def has_english(text):
        if pd.isna(text):
            return False
        text_without_parens = re.sub(r'\([^)]*\)', '', str(text))
        return bool(re.search(r'[A-Za-z]{3,}', text_without_parens))

    remaining_english = df[df['地區名稱'].apply(has_english)]['地區名稱'].unique()

    if len(remaining_english) > 0:
        print(f"\n[WARNING] 仍有 {len(remaining_english)} 個地區名稱未翻譯：")
        for name in remaining_english[:10]:
            print(f"  - {name}")
    else:
        print("\n[SUCCESS] 所有地區名稱已成功翻譯為繁體中文！")

    # 儲存翻譯後的檔案
    output_file = 'csv/country_indicators.csv'
    print(f"\n正在儲存到 {output_file}...")
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print("[SUCCESS] 檔案已成功更新！")

    return df

if __name__ == "__main__":
    df = translate_csv()
