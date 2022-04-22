class two_sum():
    def sum(num_arr, pair_sum):
        for i in range(len(num_arr) - 1):
            for j in range(i + 1, len(num_arr)):
                if num_arr[i] + num_arr[j] == pair_sum:
                    return True
                    #it's my solution with time O(n^2)     
        '''
        it's solution i found in internet with time == O(n)
        hashTable = {}
        for i in range(len(num_arr)):
            complement = pair_sum - num_arr[i]
            if complement in hashTable:
                return True
            hashTable[num_arr[i]] = num_arr[i]
        '''

print(two_sum.sum(num_arr= [0, -2, 4, -4, -6, -11, 7], pair_sum = 11))