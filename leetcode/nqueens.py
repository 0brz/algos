class Solution(object):

    def on_diag(self, i, j, n, map):
        x = i
        y = j
        while((x >= 0) | (y >= 0)):
            if (map.count([x, y]) > 0):
                print("DIAG", x, y)
                return True
            x -= 1
            y -= 1
        
        x = i
        y = j
        while((x < n) | (y < n)):
            if (map.count([x, y]) > 0):
                return True
            x += 1
            y += 1

        return False

    def set_queen(self, map, i, j, n):
        map.append([i, j])
        #print("add_v=", i, j)
        for r in range(n):
            map.append([i, r])
            map.append([r, j])

    def solve(self, map, n, ir, jr, k):
        #print(ir, jr)
        if (map.count([ir, jr]) == 0 and self.on_diag(ir, jr, n, map) == False):
            #print(map)
            #print("set_queen", ir, jr)
            self.set_queen(map, ir, jr, n)
            k += 1
            if (k == n):
                return True
            

        if (ir == jr == n-1):
            return k == n

        if (ir >= n-1):
            ir = 0
            jr += 1
        else: ir += 1

        return self.solve(map, n, ir, jr, k)

    def totalNQueens(self, n):
        s = 0
        map = []
        for i in range(n):
            for j in range(n):
                if (self.solve(map, n, i, j, 0)):
                    s+= 1
                else: map = []    
                

        return s
    
s = Solution()
print(s.totalNQueens(4))
