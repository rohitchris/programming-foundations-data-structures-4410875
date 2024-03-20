''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

NUM_OF_STUDENTS = len(student_pet_count_list)

# to access the last element in the array we can use negative index
# print(student_pet_count_list[-1])

pet_count_sum = 0;
for ind_pet_count in student_pet_count_list:
    pet_count_sum += ind_pet_count

print(pet_count_sum)



# average = sum / number of items
avg = pet_count_sum / NUM_OF_STUDENTS

print(avg)
