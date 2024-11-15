import matplotlib.pyplot as plt

label = ["a", "b", "c", "d"]
num = [20, 17, 25, 9]
plt.bar(label, num)
plt.savefig('./bar.png')