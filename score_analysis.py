# 我的第一个数据分析小练习：学生成绩统计
# 目标：计算数学成绩的平均分，并找出最高分

# 1. 模拟从数据库或表格中获取的一组数学成绩数据
scores = [82, 86, 75, 91, 68, 88, 95, 79, 84]

print("--- 数据读取成功 ---")
print(f"当前共有 {len(scores)} 条成绩记录。\n")

# 2. 计算平均分
# 使用 sum() 求和，len() 求数量
average_score = sum(scores) / len(scores)

# 3. 找出最高分和最低分
max_score = max(scores)
min_score = min(scores)

# 4. 输出结果，保留两位小数
print("--- 数据分析结果 ---")
print(f"✅ 平均分: {average_score:.2f}")
print(f"✅ 最高分: {max_score}")
print(f"✅ 最低分: {min_score}")

# 5. 简单的业务判断逻辑
if average_score > 80:
    print("\n结论：该班级整体成绩良好。")
else:
    print("\n结论：该班级整体成绩需加强辅导。")
