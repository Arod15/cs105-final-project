import matplotlib.pyplot as plt

def graph(attributes, values):
	plt.plot(attributes, values, 'bo', linewidth=2)
	plt.axis([-1, 5, -1, 50])
	plt.show()


graph(["Gunshot", "Taser", "Death in Custody", "Struck by Vehicle", "Unknown"], [46, 1, 0, 0, 0])
# graph(["Hispanic/Latino", "Native American", "Black", "White", "Asian/Pacific Islander", "Unknown"], [8, 3, 12, 20, 1, 3])