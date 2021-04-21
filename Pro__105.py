observations=[60,61,65,63,98,99,90,95,91,96]
sum=0
for i in range(len(observations)):
    sum+=observations[i]
mean=sum/len(observations)
sum_of_squared_deviation=0
for i in range (len(observations)):
    sum_of_squared_deviation+=(observations[i] - mean)**2
standard_deviation=((sum_of_squared_deviation)/len(observations))**0.5
print("Standard Deviation " + str(standard_deviation))
