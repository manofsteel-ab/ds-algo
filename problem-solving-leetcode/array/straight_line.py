
class Solution:

    def checkStraightLine(self, points: List[List[int]]) -> bool:
        x0,y0  = points[0]
        points = [ (x,y) for x,y in points if x != x0 or y != y0 ]      # Other points
        slopes = [ (y-y0)/(x-x0) if x!=x0 else None for x,y in points ] # None for vertical Line
        return all( s == slopes[0] for s in slopes)
