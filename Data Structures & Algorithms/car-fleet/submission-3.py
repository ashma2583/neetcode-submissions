class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = [[p, s] for p, s in zip(position, speed)]
        posSpeed.sort(reverse=True)
        print(posSpeed)

        # time = (target - pos) / speed
        fleet = 1
        prevTime = (target - posSpeed[0][0]) / posSpeed[0][1]
        for i in range(1, len(posSpeed)):
            ps = posSpeed[i]
            currTime = (target - ps[0]) / ps[1]
            if currTime > prevTime:
                fleet += 1
                prevTime = currTime

        return fleet


