【数组】（20240708-20240709，）
两数之和
买卖股票的最佳时机（以及几个变种题）
存在重复元素（以及几个变种题）
除自身以外数组的乘积
最大子数组和
乘积最大子数组
寻找旋转排序数组中的最小值
搜索旋转排序数组
三数之和
盛最多水的容器
排序（quicksort+mergesort）
【二进制】（20240709-20240710，）
两整数之和
位1的个数
比特位计数
丢失的数字
颠倒二进制位
只出现一次的数字（以及几个变种题）
【动态规划】（20240710-20240711，）
爬楼梯
使用最小花费爬楼梯
零钱兑换I&II（完全背包问题，需要花半天看一下0-1背包和完全背包问题）
单词拆分（完全背包-考虑顺序）
最长递增子序列
最长公共子序列
组合总和（以及几个变种题）
打家劫舍I&II&III
解码方法
不同路径I&II
跳跃游戏（时间复杂度O(n)）
【图】（20240712-20240713，）
克隆图
课程表
岛屿数量
最长连续序列
火星词典(plus会员)
```txt
现有一种使用英语字母的火星语言，这门语言的字母顺序对你来说是未知的。
给你一个来自这种外星语言字典的字符串列表words，words中的字符串已经按这门新语言的字典序
进行了排序。如果这种说法是错误的，并且给出的words不能对应任何字母的顺序，则返回 "" 。
否则，返回一个按新语言规则的字典递增顺序排序的独特字符串。如果有多个解决方案，则返回其中任意一个。

示例 1：
输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"

示例 2：
输入：words = ["z","x"]
输出："zx"

示例 3：
输入：words = ["z","x","z"]
输出：""
解释：不存在合法字母顺序，因此返回 "" 。
 

提示：
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] 仅由小写英文字母组成
```
```python
#方法一：拓扑排序 + 深度优先搜索
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {}
        for c in words[0]:
            g[c] = []
        for s, t in pairwise(words):
            for c in t:
                g.setdefault(c, [])
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    break
            else:
                if len(s) > len(t):
                    return ""

        VISITING, VISITED = 1, 2
        states = {}
        order = []
        def dfs(u: str) -> bool:
            states[u] = VISITING
            for v in g[u]:
                if v not in states:
                    if not dfs(v):
                        return False
                elif states[v] == VISITING:
                    return False
            order.append(u)
            states[u] = VISITED
            return True

        return ''.join(reversed(order)) if all(dfs(u) for u in g if u not in states) else ""
# 方法二：拓扑排序 + 广度优先搜索
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(list)
        inDeg = {c: 0 for c in words[0]}
        for s, t in pairwise(words):
            for c in t:
                inDeg.setdefault(c, 0)
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    inDeg[v] += 1
                    break
            else:
                if len(s) > len(t):
                    return ""

        q = [u for u, d in inDeg.items() if d == 0]
        for u in q:
            for v in g[u]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        return ''.join(q) if len(q) == len(inDeg) else ""
```
以图判树(plus会员)
给定编号从 0 到 n - 1 的 n 个结点。给定一个整数 n 和一个 edges 列表，其中 edges[i] = [ai, bi] 表示图中节点 ai 和 bi 之间存在一条无向边。
如果这些边能够形成一个合法有效的树结构，则返回 true ，否则返回 false 。
[以图判树1](pic/以图判树1.jpg)
输入: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
输出: true
[以图判树2](pic/以图判树2.jpg)
输入: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
输出: false

无向图中连通分量的数目(plus会员)
你有一个包含 n 个节点的图。给定一个整数 n 和一个数组 edges ，其中 edges[i] = [ai, bi] 表示图中 ai 和 bi 之间有一条边。
返回 图中已连接分量的数目 。
示例1：
[无向图中连通分量的数目1](pic/无向图中连通分量的数目1.jpg)
输入: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
输出: 2
[无向图中连通分量的数目2](pic/无向图中连通分量的数目2.jpg)
输入: n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]
输出:  1

提示：
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
edges中不会出现重复的边
```python
'''
思路和心得：

1.并查集就是针对这个问题设计的（用size进行压缩）

直接默写就ok
（有些函数用不到，但每次都默写全，比较好一点，模块化，肌肉记忆）

（一）size策略
size[node]是每课以node为根结点的树的结点个数。

（二）size策略+Find中扁平化（路径压缩）
size[node]与实际意义可能对不上
但size[root]是对的

（三）rank策略
是size策略的兄弟

（四）Find中扁平化（路径压缩）
比较省心。也只是尽量去扁平化。最后不能保证，最后的树高就是2，也可能碰巧了很高，但概率很小

（*）rank策略+Find中扁平化（路径压缩）。rank[root]对应不上实际
只要find优化了一次，很有可能，这棵树上很多点的rank都变了。rank[root]也与实际对不上了
'''
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]

    def Find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        return self.Find(self.parent[x])

    def Union(self, x: int, y: int) -> bool:
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1
        return True
    
    def in_the_same_part(self, x: int, y: int) -> bool:
        return self.Find(x) == self.Find(y)
    
    def get_part_size(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        UF = UnionFind(n)
        for x, y in edges:
            UF.Union(x, y)
        return UF.part
```
```java
//Java三种解法 并查集+DFS+BFS
//1.并查集
public int countComponents(int n, int[][] edges) {
    int[] parents = new int[n];
    Arrays.fill(parents, -1);

    for (int[] e : edges) {
        int root1 = find(parents, e[0]);
        int root2 = find(parents, e[1]);
        if (root1 != root2) {
            parents[root1] = root2;
            n--;
        }
    }
    return n;
}

private int find(int[] parents, int x) {
    int root = x;
    while (parents[root] != -1) root = parents[root];
    return root;
}

//2.深度优先搜索dfs
public int countComponents(int n, int[][] edges) {
    int count = 0;
    List<List<Integer>> adjList = new ArrayList<>();
    boolean[] visited = new boolean[n];

    for (int i = 0; i < n; i++) adjList.add(new ArrayList<>());
    for (int[] edge : edges) {
        adjList.get(edge[0]).add(edge[1]);
        adjList.get(edge[1]).add(edge[0]);
    }
        
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            count++;
            dfs(visited, i, adjList);
        }
    }
    return count;
}

private void dfs(boolean[] visited, int index, List<List<Integer>> adjList) {
    visited[index] = true;
    for (int i : adjList.get(index)) {
        if (!visited[i]) {
            dfs(visited, i, adjList);
        }
    }
}

//3.广度优先搜索bfs
public int countComponents(int n, int[][] edges) {
    int count = 0;
    List<List<Integer>> adjList = new ArrayList<>();
    boolean[] visited = new boolean[n];
        
    for (int i = 0; i < n; i++) adjList.add(new ArrayList<>());
    for (int[] edge : edges) {
        adjList.get(edge[0]).add(edge[1]);
        adjList.get(edge[1]).add(edge[0]);
    }

    for (int i = 0;  i < n; i++) {
        if (!visited[i]) {
            count++;
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(i);
            while (!queue.isEmpty()) {
                int index = queue.poll();
                visited[index] = true;
                for (int next : adjList.get(index)) {
                    if (!visited[next]) queue.offer(next);
                }
            }
        }
    }
    return count;
}
```
【interval】（20240713-20240714，）
插入区间
合并区间
无重叠区间
会议室(plus会员)
给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够参加这里面的全部会议。
示例 1：
输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
示例 2：
输入：intervals = [[7,10],[2,4]]
输出：true
提示：
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
```python
#方法一：暴力法
class Solution:
   def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
       def overlap(interval1: List[int], interval2: List[int]) -> bool:
           return (interval1[0] >= interval2[0] and interval1[0] < interval2[1]
               or interval2[0] >= interval1[0] and interval2[0] < interval1[1])

       for i in range(len(intervals)):
           for j in range(i + 1, len(intervals)):
               if overlap(intervals[i], intervals[j]):
                   return False
       return True
#方法二：排序
class Solution:
   def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
       intervals.sort()
       for i in range(len(intervals) - 1):
           if intervals[i][1] > intervals[i + 1][0]:
               return False
       return True
```
会议室II(plus会员)
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量 。
示例 1：
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2
示例 2：
输入：intervals = [[7,10],[2,4]]
输出：1
提示：
1 <= intervals.length <= 104
0 <= starti < endi <= 106
```python
#方法一：优先队列
 class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 如果没有要安排的会议，则不需要分配房间。
        if not intervals:
            return 0

        # 堆初始化
        free_rooms = []
        # 按会议开始时间的升序对会议进行排序。
        intervals.sort(key= lambda x: x[0])
        # 添加第一次会议。我们得给第一次会议腾出一间新房间。
        heapq.heappush(free_rooms, intervals[0][1])

        # 对于所有剩余的会议室
        for i in intervals[1:]:
            # 如果最早应该腾出的房间是空闲的，则将该房间分配给本次会议。
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # 如果要分配一个新房间，那么我们也要添加到堆中，
            # 如果分配了一个旧房间，那么我们还必须添加到具有更新的结束时间的堆中。
            heapq.heappush(free_rooms, i[1])

        # 堆的大小告诉我们所有会议所需的最小房间。
        return len(free_rooms)

#方法二：按时间顺序排序
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # 如果没有会议，我们不需要任何房间。
        if not intervals:
            return 0

        used_rooms = 0

        # 将开始计时和结束计时分开，并分别对它们进行排序。
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # 算法中的两个指针：e_ptr 和 s_ptr。
        end_pointer = 0
        start_pointer = 0

        # 直到所有会议都处理完毕
        while start_pointer < L:
            # 如果有一个会议在 `start_pointer` 开始时已经结束
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # 释放一个房间并递增end_pointer。
                used_rooms -= 1
                end_pointer += 1

            # 无论房间是否空闲，我们都会这样做。
            # 如果一个房间是空闲的，那么 used_rooms+=1 将不会有任何效果。 used_rooms 
            # 在这种情况下会保持不变。如果没有空闲的房间，则会增加已用房间数。
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms
```
【链表】（20240715-20240716，）
反转链表I&II
环形链表I&II
合并两个有序链表
合并K个升序链表
删除链表的倒数第N个结点
重排链表
【矩阵】（20240717-20240718，）
矩阵置零
螺旋矩阵I&II
旋转图像
单词搜索
【字符串】（20240718-20240719，）
无重复字符的最长子串
替换后的最长重复字符
最小覆盖子串
有效的字母异位词
字母异位词分组
有效的括号
验证回文串
最长回文子串
回文子串
字符串的编码与解码(plus会员)
请你设计一个算法，可以将一个 字符串列表 编码成为一个 字符串。这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。
```python
#方法一：使用非 ASCII 码的分隔符(最简单的方法就是分隔符连接字符串)
class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: 
            return chr(258)
        
        # encode here is a workaround to fix BE CodecDriver error
        return chr(257).join(strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        if s == chr(258): 
            return []
        return s.split(chr(257))
# 方法二：分块编码
#这种方法基于 HTTP v1.1 使用的编码，它不依赖于输入字符集，因此比方法一更具有通用性和有效性。
#数据流被分成块，每个块前面都有其字节大小。
class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output

```
【树】（20240719-20240723，）
二叉树的最大深度
相同的树
翻转二叉树
二叉树中的最大路径和
二叉树的层序遍历
二叉树的序列化与反序列化
另一棵树的子树
从前序与中序遍历序列构造二叉树
验证二叉搜索树
二叉搜索树中第K小的元素
二叉树的最近公共祖先
实现Trie(前缀树)
添加与搜索单词 - 数据结构设计
【堆】（20240723-20240724，）
前K个高频元素
前K个高频单词
数据流的中位数





Original Link:<br>
[Blind 75 LeetCode Questions](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)
