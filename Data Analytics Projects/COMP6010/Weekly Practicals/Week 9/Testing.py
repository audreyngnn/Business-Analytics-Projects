def longest_ascending_sequence (lst):
    current_seq = [lst[0]]
    longest_seq = current_seq
    
    for i in range (0, len(lst)-1):
        # this pair of elements is ascending
        if lst [i] <= lst [i+1]:
            current_seq.append(lst[i+1])
        else:
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq
            current_seq = [lst[i+1]]
        print("current:", current_seq, "longest:", longest_seq)

    if len(current_seq) > len(longest_seq):
        longest_seq = current_seq
    
    return longest_seq

print(longest_ascending_sequence([10, 70, 80, 20, 10, 10, 30, 50]))