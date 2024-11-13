# 問題1-1
"""
scores = {"数学":82, "国語":74, "英語":60, "理科":92, "社会":70}

diff = scores["理科"] - scores["社会"]

print(f"{diff}点")
"""
# 問題1-2
"""
scores = [82, 74, 60, 92, 70]
avg_score = sum(scores) / len(scores)
print(avg_score)    
"""
scores = {"数学":82, "国語":74, "英語":60, "理科":92, "社会":70}
"""
scores_values = list(scores.values())
avg_score = sum(scores_values) / len(scores_values)
print(f'{avg_score}点')
"""
avg_score = sum(scores.values()) / len(scores.values())
print(f'{avg_score}点')