from enum import Enum


class FnAction(Enum):
    START, END = 'start', 'end'


class Log:
    def __init__(self, raw_log):
        self.function_id, self.action, self.time = raw_log.split(':')
        self.function_id, self.time = int(self.function_id), int(self.time)
        self.sub_duration = 0  # this will be incremented if additional fn calls are made

    def is_start(self):
        return self.action == FnAction.START.value


class Solution:
    def exclusiveTime_add_on_the_go(self, n: int, logs: List[str]) -> List[int]:

        box_score = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            function_id, action, time = log.split(':')
            function_id, time = int(function_id), int(time)
            if action == 'start':
                # add prev function's runtime to its boxscore
                if stack:
                    last_function_id = stack[-1]
                    runtime = time - prev_time
                    box_score[last_function_id] += runtime
                stack.append(function_id)
                prev_time = time
            elif action == 'end':
                last_function_id = stack.pop()
                runtime = time - prev_time + 1
                box_score[last_function_id] += runtime
                prev_time = time + 1
            else:
                pass

        return box_score

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack = []
        box_score = [0] * n

        for raw_log in logs:
            log = Log(raw_log)

            if log.is_start():
                stack.append(log)
            else:
                # since it's a single thread env, we know that the log belongs to last fn in stack
                start_log = stack.pop()
                score = log.time - start_log.time + 1 - start_log.sub_duration
                box_score[log.function_id] += score

                if stack:
                    # if fn is wrapped, also add score(exclude sub) to wrapping function's context
                    wrapping_function_log = stack[-1]
                    score_without_subduration = log.time - start_log.time + 1
                    wrapping_function_log.sub_duration += score_without_subduration

        return box_score


