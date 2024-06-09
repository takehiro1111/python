nums = [10, 20, 30]
# nums_bak = nums  変数に変数を代入すると新しく同じ値が入るわけではなく、代入元の値を向く
nums_bak = nums.copy()
nums[0] = 100

print(nums) # [100, 20, 30]
print(nums_bak) # [10, 20, 30]
