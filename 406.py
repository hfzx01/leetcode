class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        people.sort(key=lambda x: (x[0],-x[1]), reverse=True)

        for i in people:
            result.insert(i[1], i)
        return result