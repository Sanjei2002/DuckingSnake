def hasDuplicate(self, nums: list[int]) -> bool:

    collection:  list[int] = []
    for number in enumerate(nums):
        if number[1] in collection:
            return True
        else:
            collection.append(number[1])
    else:
        return False


nums = [1, 2, 3, 4]

print(f"HasDuplicate {hasDuplicate(self=None, nums=nums)}")
