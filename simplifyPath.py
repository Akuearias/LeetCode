class Solution:
    def simplifyPath(self, path: str) -> str:
        while path.startswith('/..'):
            if len(path) == 3 or path[3] == '/':
                path = path[3:]
            else:
                break
        n = len(path)
        if n == 0:
            return '/'

        if path[-1] == '/':
            path = path[:n - 1]

        path_list = path.split('/')
        S = []
        for p in path_list:
            if p != '' and p != '.':
                if p != '..':
                    S.append('/')
                    S.append(p)
                else:
                    if S:
                        S.pop()
                    if S:
                        S.pop()
            else:
                continue

        return "/" if not S else ''.join(S)


