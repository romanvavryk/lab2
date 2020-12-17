from tabulate import tabulate

f_string = [i.strip('\n').split(',') for i in open('data.txt')]
all_predictions = []


for i in range(0, 2):
	for j in range(0,5):
		f_string[i][j] = float(f_string[i][j])

for i in range(2,3):
	for j in range(0,4):
		f_string[i][j] = float(f_string[i][j])

for i in range (3,4):
	for j in range(0, 1):
		f_string[i][j] = float(f_string[i][j])

print(tabulate([f_string], headers=['A','B','C', 'D', 'E', 'F'], tablefmt='orgtbl'))

term = f_string[3][0]

big_factory_values = f_string[0]
big_factory_demands_possibility = [big_factory_values[2], big_factory_values[4]]
big_factory_cost = big_factory_values[0]
big_factory_demands = [big_factory_values[1], big_factory_values[3]]					
def big_factory():
	big_factory_prediction = 0
	
	for i in range(0, 2):
		big_factory_prediction += term * big_factory_demands[i] * big_factory_demands_possibility[i]

	big_factory_prediction = big_factory_prediction - big_factory_cost
	
	all_predictions.append(big_factory_prediction)

small_factory_values = f_string[1]
small_factory_demands_possibility = [small_factory_values[2], small_factory_values[4]]
small_factory_cost = small_factory_values[0]
small_factory_demands = [small_factory_values[1], small_factory_values[3]]
def small_factory():
	small_factory_prediction = 0

	for i in range(0, 2):
		small_factory_prediction += term * small_factory_demands[i] * small_factory_demands_possibility[i]

	small_factory_prediction = small_factory_prediction - small_factory_cost
	
	all_predictions.append(small_factory_prediction)


new_term = term - 1

def analyse():
	new_predictions = []
	def new_big_factory():
		new_big_factory_demands_possibility = [f_string[2][2], f_string[2][3]]
		new_big_factory_prediction = 0

		for i in range(0, 2):
			new_big_factory_prediction += new_term * big_factory_demands[i] * new_big_factory_demands_possibility[i]

		new_big_factory_prediction = new_big_factory_prediction - big_factory_cost
		new_predictions.append(new_big_factory_prediction)
		all_predictions.append(new_big_factory_prediction)
	
	def new_small_factory():
		new_small_factory_demands_possibility = [f_string[2][2], f_string[2][3]]
		new_small_factory_prediction = 0

		for i in range(0, 2):
			new_small_factory_prediction += new_term * small_factory_demands[i] * new_small_factory_demands_possibility[i]

		new_small_factory_prediction = new_small_factory_prediction - small_factory_cost
		new_predictions.append(new_small_factory_prediction)
		all_predictions.append(new_small_factory_prediction)

	new_big_factory()
	new_small_factory()

	possitive_prediction_value = max(new_predictions)

	negative_prediction_value = 0
	all_predictions.append(negative_prediction_value)

	f_factory_demands_possibility = [f_string[2][0], f_string[2][1]]
	f_factory_demands = [possitive_prediction_value, negative_prediction_value]

	f_prediction = 0
	for i in range(0,2):
		f_prediction += f_factory_demands_possibility[i] * f_factory_demands[i]

	all_predictions.insert(2, f_prediction)

big_factory()
small_factory()
analyse()

result = max(all_predictions)
result_index = all_predictions.index(result)
alp = ['A', 'B', 'C', 'D', 'E', 'F']
alp_index = alp[result_index]

solution = f'{alp_index} : {result}'

all_predictions.append(solution)

print()
print(tabulate([all_predictions], headers=['A','B','C', 'D', 'E', 'F', 'Solution'], tablefmt='orgtbl'))