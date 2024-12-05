def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Pair smallest with smallest and calculate distances
    total_distance = 0
    for left, right in zip(left_sorted, right_sorted):
        total_distance += abs(left - right)
    
    return total_distance

def read_input(file_path):
    left_list = []
    right_list = []
    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())  # Split each line into two integers
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def get_score(left_list, right_list):
    match_ctr = 0
    sim_score = 0
    
    # Iterate through the left list
    for left_num in left_list:
        # Count number of occerrences of left_num in right_list
        matches = right_list.count(left_num)        
        match_ctr += matches
        # Calculate similarity score
        sim_score += left_num * matches
    return sim_score

if __name__ == "__main__":
    # Input file
    input_file = "input.txt"
    
    # Read input data
    left_list, right_list = read_input(input_file)
    
    # Calculate total distance
    # total_distance = calculate_total_distance(left_list, right_list)
    # print("Total Distance:", total_distance)

    # Get the similarity score
    score = get_score(left_list, right_list)
    print("Total similarity score:", score)
    
