class Solution:
    def catMouseGame(self, graph):
        def prestatus(graph, curstatus):
            tmp = []
            m,c,t=curstatus
            if t == 1:
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    tmp.append((m, pc, 2))
            else:
                for pm in graph[m]:
                    tmp.append((pm, c, 1))
            return tmp
        l = len(graph)
        color = [[[0]*3 for _ in range(l)] for _ in range(l)]
        res = []
        for i in range(1,l):
            for t in range(1,3):
                color[0][i][t] = 1
                res.append((0,i,t))
                color[i][i][t] = 2
                res.append((i,i,t))
        while res:
            curstatus = res.pop(0)
            m,c,t = curstatus
            for Prestatus in prestatus(graph, curstatus):
                pm, pc, pt = Prestatus
                if color[pm][pc][pt] != 0:
                    continue
                if color[m][c][t] == pt:
                    color[pm][pc][pt] = pt
                    res.append(Prestatus)
                else:
                    if t == 2:
                        flag = True
                        for nextpremouse in graph[pm]:
                            if color[nextpremouse][pc][t] != t:
                                flag = False
                                break
                        if flag:
                            color[pm][pc][pt] = t
                            res.append(Prestatus)
                    else:
                        flag = True
                        for nextprecat in graph[pt]:
                            if nextprecat == 0:
                                continue
                            if color[pm][nextprecat][t] != t:
                                flag = False
                                break
                        if flag:
                            color[pm][pc][pt] = t
                            res.append(Prestatus)
        return color[1][2][1]


#找不到问题在哪儿，wsl
s = Solution()
print(s.catMouseGame([[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]))