class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        i = 0
        j = len(people) - 1
        while i <= j:
            if (people[j] + people[i]) <= limit:
                i += 1
                j -= 1
                boats += 1
            else:
                j -= 1
                boats += 1
        return boats
