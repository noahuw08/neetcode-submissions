class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if k = 2 -> return 2 most frequent ele in the arr
        # want a count freq for each element in the num array
            # hashmap, since as we continue going thru the arr if we encounter the same ele again then we wanna accumulate by 1

        # after traversing thru the array we get the count freq for each unique ele in the num arr inside our hashmap

        hashmap = {}
        output = []

        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        
        # how to sort n get the k most freq element in the hashmap?
        # sort the hashmap by value (count freq) before proceeding
        sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))    # dict() wrapped around since sorted() returns a list
        
        for i, key in enumerate(sorted_dict):
            output.append(key)
            if i == k - 1:
                break
        return output


