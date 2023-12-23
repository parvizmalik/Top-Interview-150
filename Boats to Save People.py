class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        hev = len(people)-1
        lig = 0
        boat = 0

        while hev >= lig:
            if people[lig] + people[hev] <= limit:
                boat += 1
                lig += 1 
                hev -= 1
            else:
                boat += 1
                hev -= 1
        return boat