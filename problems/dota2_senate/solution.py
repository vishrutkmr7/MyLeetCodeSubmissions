class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Radiant = []
        Dire = []
        n = len(senate)

        for i in range(n):
            if senate[i] == "R":
                Radiant.append(i)
            else:
                Dire.append(i)

        if Radiant and not Dire:
            return "Radiant"
        if Dire and not Radiant:
            return "Dire"

        while True:
            if Radiant[0] < Dire[0]:
                Dire.pop(0)
                if not Dire:
                    return "Radiant"
                Radiant.pop(0)
                Radiant.append(n)
            else:
                Radiant.pop(0)
                if not Radiant:
                    return "Dire"
                Dire.pop(0)
                Dire.append(n)

            n += 1
