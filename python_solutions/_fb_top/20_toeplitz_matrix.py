class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph, visited, email_to_account = defaultdict(set), set(), {}

        # set up graph, visited
        for account in accounts:
            emails = account[1:]
            first_email = emails[0]
            for email in emails:
                # add undirected edges between first node and other nodes
                graph[email].add(first_email)
                graph[first_email].add(email)
                email_to_account[email] = account[0]

        def dfs(node, component):
            if node in visited:
                return
            visited.add(node)

            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        output = []
        for email, account in email_to_account.items():
            if email in visited:
                continue

            nodes = []
            dfs(email, nodes)
            output.append([account] + sorted(nodes))

        return output



