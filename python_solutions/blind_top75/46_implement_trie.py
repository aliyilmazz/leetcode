from collections import defaultdict
from typing import List

from collections import defaultdict


class GNode:
    def __init__(self):
        self.in_degrees = 0
        self.out_nodes = []


class Solution:

    def canFinish_dp_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_dict = defaultdict(list)

        #  construct graph
        for relation in prerequisites:
            next_course, prev_course = relation
            course_dict[prev_course].append(next_course)

        course_cyclic_result = [-1] * numCourses

        def isCyclic(course, visited):
            if course_cyclic_result[course] != -1:
                return course_cyclic_result[course]

            for next_course in course_dict[course]:
                if next_course in visited:
                    return True

                visited.add(course)
                if isCyclic(next_course, visited):
                    return True
                visited.remove(course)

            course_cyclic_result[course] = False
            return False

        for course in range(numCourses):
            if isCyclic(course, set()):
                return False

        return True

    def canFinish(self, numCourses, prerequisites):
        from collections import deque

        graph = defaultdict(GNode)

        # construct graph, set in_degrees
        total_dependencies = len(prerequisites)
        for relation in prerequisites:
            next_course, prev_course = relation
            graph[prev_course].out_nodes.append(next_course)
            graph[next_course].in_degrees += 1

        # outline courses which has no dependency
        no_dependency_courses = deque()
        for index, node in graph.items():
            if node.in_degrees == 0:
                no_dependency_courses.append(index)

        removed_edges = 0
        while no_dependency_courses:
            no_dep_course = no_dependency_courses.pop()
            for out_node in graph[no_dep_course].out_nodes:
                graph[out_node].in_degrees -= 1
                removed_edges += 1

                if graph[out_node].in_degrees == 0:
                    no_dependency_courses.append(out_node)

        return removed_edges == total_dependencies


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0]]
    can_finish = Solution().canFinish(numCourses, prerequisites)
    print("can finish: %s" % can_finish)