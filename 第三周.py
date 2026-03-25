import math

# ====== 輸入基本資料 ======
student_id = input("請輸入學生證號碼: ")
name = input("請輸入姓名: ")
current_year = int(input("請輸入目前學年度 (例如 113): "))

# ====== 輸入四門成績與學分 ======
scores = []
credits = []

for i in range(4):
    score = float(input(f"請輸入第{i+1}科成績: "))
    credit = float(input(f"請輸入第{i+1}科學分: "))
    scores.append(score)
    credits.append(credit)

# ====== 學籍資訊解析 ======
# 假設學號格式：入學年(3碼)+系所(2碼)+班級(1碼)+座號(2碼)
entry_year = int(student_id[:3])
dept_code = student_id[3:5]
class_code = student_id[5]
seat_number = student_id[6:]

grade = current_year - entry_year + 1
graduation_year = entry_year + 4

# ====== 成績計算 ======
# 平均
average = sum(scores) / len(scores)

# 加權平均
weighted_sum = sum(scores[i] * credits[i] for i in range(4))
total_credits = sum(credits)
weighted_avg = weighted_sum / total_credits

# ====== 進階統計 ======
# 變異數
variance = sum((x - average) ** 2 for x in scores) / len(scores)

# 標準差
std_dev = math.sqrt(variance)

# 幾何平均
geo_mean = (scores[0] * scores[1] * scores[2] * scores[3]) ** (1/4)

# 調和平均
harmonic_mean = len(scores) / sum(1/x for x in scores if x != 0)

# ====== 輸出 ======
print("\n===== 學籍資訊 =====")
print("姓名:", name)
print("學號:", student_id)
print("入學學年度:", entry_year)
print("預計畢業:", graduation_year)
print("當前年級:", grade)
print("系所代碼:", dept_code)
print("班級代碼:", class_code)
print("座號:", seat_number)

print("\n===== 成績資訊 =====")
print("平均成績:", round(average, 2))
print("加權平均:", round(weighted_avg, 2))

print("\n===== 統計資訊 =====")
print("變異數:", round(variance, 2))
print("標準差:", round(std_dev, 2))
print("幾何平均:", round(geo_mean, 2))
print("調和平均:", round(harmonic_mean, 2))