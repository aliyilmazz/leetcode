class Solution:
    def simplifyPath(self, path: str) -> str:

        dirs = path.split('/')
        stack = []
        #print("dirs:%s" % dirs)
        for dir in dirs:
            if dir in ('', '.'):
                continue

            if dir == '..':
                if stack:
                    stack.pop()
                else:
                    # we are already in root path, no need to pop
                    pass
            else:
                stack.append(dir)
        #print("stack: %s" % stack)
        canonical_path = "/%s" % '/'.join(stack)
        return canonical_path


if __name__ == '__main__':
    path = "/home"
    output = Solution().simplifyPath(path)
    print("Path: %s\nOutput: %s" % (path, output))