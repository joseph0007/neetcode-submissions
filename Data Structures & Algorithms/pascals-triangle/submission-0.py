class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for num in range(numRows):
            if num == 0:
                result.append([1])
            elif num == 1:
                result.append([1,1])
            else:
                prev_row = result[len(result) - 1]
                curr_num = num + 1
                new_row = [None] * curr_num
                curr_sum = 0
                for idx,row_val in enumerate(prev_row):
                    new_row[idx] = curr_sum + row_val
                    if idx / 2 == 0:
                        curr_sum += row_val
                    else:
                        curr_sum = row_val
                new_row[curr_num-1] = 1
                new_row[len(new_row) - 1] = 1
                result.append(new_row)
        return result