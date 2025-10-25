'''
Week 07 | Data Structure - Tuple & Dicionary 
'''

# Exercise 00 Lv: Advanced
thainum = ('๐','๑','๒','๓','๔','๕','๖','๗','๘','๙')
thairead = ('ศูนย์','หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','เก้า')
digit_suffix = ('','สิบ','ร้อย','พัน') 

num = input("Enter any number (up to four digits): ")
thai_num = ''
thai_read = ''

num_length = len(num)
for i, n_char in enumerate(num):
    n = int(n_char)
    thai_num += thainum[n]
    place_value = num_length - 1 - i

    if n == 0:
        if num_length == 1:
            thai_read += thairead[n]
        pass
    elif n == 1 and place_value == 1 and num_length > 1: 
        thai_read += 'สิบ'
    elif n == 1 and place_value == 0 and num_length > 1 and num[-2] != '0': 
        thai_read += 'เอ็ด'
    elif n == 2 and place_value == 1 and num_length > 1:
        thai_read += 'ยี่' + digit_suffix[place_value]
    else:
        thai_read += thairead[n] + digit_suffix[place_value]

    if 'หนึ่งสิบ' in thai_read:
        thai_read = thai_read.replace('หนึ่งสิบ', 'สิบ')
    if 'สองสิบ' in thai_read:
        thai_read = thai_read.replace('สองสิบ', 'ยี่สิบ')
    if 'สิบหนึ่ง' in thai_read:
        thai_read = thai_read.replace('สิบหนึ่ง', 'สิบเอ็ด')

print(f"เลขไทย: {thai_num}")
print(f"คำอ่าน: {thai_read}")


#Exercise 01 Lv: Moderate
constellations = ('ชวด','ฉลู','ขาล','เถาะ','มะโรง','มะเส็ง','มะเมีย','มะแม','วอก','ระกา','จอ','กุน')
symbol = ('หนู','วัว','เสือ','กระต่าย','งูใหญ่','งูเล็ก','ม้า','แพะ','ลิง','ไก่','หมา','หมู')

for year in range(2565,2571):
    i = (year+5)%12
    print(f"ปี {year} ตรงกับปีนักษัตร: {constellations[i]} >> สัญลักษณ์: {symbol[i]}")

#Exercise 02 Lv: Moderate
weekday = {'Mon':'วันจันทร์','Tue':'วันอังคาร','Wed':'วันพุธ','Thu':'วันพฤหัสบดี','Fri':'วันศุกร์','Sat':'วันเสาร์','Sun':'วันอาทิตย์'}
print(weekday.keys())
print(weekday.values())

#Exercise 03 Lv: Moderate
menu = {'Burger':250,'Pizza':199,'Frenchfries':299}
print(f"Menu:\n{menu}")
choice = input("Choose 1 order from Menu: ")
print(f"Food cost = {choice}:{menu.get(choice)} THB")


