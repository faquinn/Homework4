#Flammond Quinn
#PSID: 1659392


def selection_sort_descend_trace(nums):
    for x in range(len(nums)):
        max_index = x
        for i in range(x + 1,len(nums)):
            if nums[max_index] < nums[i]:
                max_index = i

        nums[x],nums[max_index]=nums[max_index],nums[x]
        for j in range(len(nums)):
            print(nums[j], end=' ')
            print()


if __name__ == '__main__':
    nums = []
    num_data = input()
    nums = [int(i) for i in num_data.split()]
    selection_sort_descend_trace(nums)
