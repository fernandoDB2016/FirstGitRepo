# How to unpack arguments
# Function that calculates the expected age you will live
def suspicious_calculator(age, fruit_ate, cigs_smoke):
    answer = (100 - age) + (fruit_ate * 3.5) - (cigs_smoke * 2)
    print(answer)


data_list = [27, 5, 0]

suspicious_calculator(data_list[0], data_list[1], data_list[2])
# for just one list of data its fine, but if want to do for lots of data (as arguments)
# it will take more lines of code, so a quick way will be using unpacking an arguments list,
# so will take the list and passes each item at the time:

suspicious_calculator(*data_list)