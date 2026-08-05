import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
money_saved = [50, 100, 50, 100, 500]

plt.plot(days, money_saved)
plt.show()

plt.plot(days, money_saved)
plt.title('Money Saved Each Day')
plt.xlabel('Days')
plt.ylabel('Amount Saved ($)')
plt.grid(True)
plt.ylim(0, 600)
plt.show()

plt.plot(days, money_saved, color='black', marker='o', linestyle='dashed', linewidth=2)
plt.title('Money Saved Each Day')
plt.xlabel('Days')
plt.ylabel('Amount Saved ($)')
plt.grid(True)
plt.ylim(0, 600)
plt.show()

plt.bar(days, money_saved, color='purple')
plt.title('Money Saved Each Day')
plt.xlabel('Days')
plt.ylabel('Amount Saved ($)')
plt.ylim(0, 600)
plt.show()  