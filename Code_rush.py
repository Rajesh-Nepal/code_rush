# Question 1 

input_value = [[0, 30], [5, 10], [15, 20]]
initial_room = 1

for index in range(len(input_value) - 1):
    current_starting_value = input_value[index][0]
    current_ending_value = input_value[index][1]

    current_count = 1

    for secondIndex in range(index+1, len(input_value)- 1):
        next_starting_value = input_value[secondIndex][0]
        next_ending_value = input_value[secondIndex][0]


        if(current_starting_value <= next_starting_value and current_ending_value >= next_starting_value) or (current_starting_value <= next_ending_value and current_ending_value >= next_ending_value):
            current_count += 1
    if(current_count>initial_room):
        initial_room = current_count


print(initial_room)



# Question 2


matrix = [[0,30],[5,10],[15,20]]

kth_column = int(input("Enter kth value")) -1

for index in range(0, int(len(matrix)/2)):
    [matrix[index][kth_column], matrix[-1 - index][kth_column]] = [matrix[-1 - index][kth_column],matrix[index][kth_column]]


print(matrix)
