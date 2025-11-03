from collections import defaultdict, deque

def alien_order(words):
    graph = defaultdict(set)
    indeg = {c:0 for w in words for c in w}
    for i in range(len(words)-1):
        w1,w2 = words[i], words[i+1]
        minlen = min(len(w1), len(w2))
        if w1[:minlen]==w2[:minlen] and len(w1)>len(w2):
            return ""
        for j in range(minlen):
            if w1[j]!=w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indeg[w2[j]]+=1
                break
    q = deque([c for c in indeg if indeg[c]==0])
    res = []
    while q:
        c = q.popleft()
        res.append(c)
        for nei in graph[c]:
            indeg[nei]-=1
            if indeg[nei]==0:
                q.append(nei)
    return "".join(res) if len(res)==len(indeg) else ""