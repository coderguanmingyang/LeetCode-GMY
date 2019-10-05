# -*- coding:utf-8 -*-
'''
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
示例 2:

输入: [[7,10],[2,4]]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        s = []
        e = []
        for meeting in intervals:
            s.append(meeting[0])
            e.append(meeting[1])
        s_e = zip(s, e)
        s_e.sort()
        rooms = [0]
        for item in s_e:
            s, e = item[0], item[1]
            rooms.sort()
            if s >= rooms[0]:
                rooms[0] = e
            else:
                rooms.append(e)
        return len(rooms)

## 找到最小值，可以用最小堆来实现
class SolutionV2(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        s = []
        e = []
        for meeting in intervals:
            s.append(meeting[0])
            e.append(meeting[1])
        s_e = zip(s, e)
        s_e.sort()
        rooms = [0]
        for item in s_e:
            s, e = item[0], item[1]
            #rooms.sort()
            min_end = heapq.heappop(rooms)
            if s >= min_end:
                heapq.heappush(rooms, e)
            else:
                heapq.heappush(rooms, e)
                heapq.heappush(rooms, min_end)
        return len(rooms)

s = Solution()
print s.minMeetingRooms(intervals=[[0, 30],[10, 40],[15, 20]])