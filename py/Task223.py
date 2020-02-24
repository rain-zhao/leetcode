class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        def area(A: int, B: int, C: int, D: int) -> int:
            return (C-A)*(D-B)
        if A > E:
            A, B, C, D, E, F, G, H = E, F, G, H, A, B, C, D
        # no intersect
        if E > C or F > D or H < B:
            return area(A, B, C, D) + area(E, F, G, H)
        # has intersect
        a, b, c, d = E, max(B, F), min(C, G), min(D, H)
        return area(A, B, C, D) + area(E, F, G, H) - area(a, b, c, d)
