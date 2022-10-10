input_factor = int(input())
input_count = int(input())
output_list = [element * input_factor for element in range(1,input_count + 1)]
print(output_list)