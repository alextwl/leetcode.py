'''
2025/07/20 daily challenge

brute-force hashing subpaths approach
'''


import collections


class Trie:
    def __init__(self):
        self.sub = dict()
        self.subpaths = list()  # list of strings of subdirectories
        self.terminal = False
        self.deleted = False

    def add(self, path):
        if not path:
            self.terminal = True
            return

        curr_folder = path[0]
        if curr_folder not in self.sub:
            self.sub[curr_folder] = Trie()

        self.subpaths.append('/'.join(path))
        self.sub[curr_folder].add(path[1:])
    
    def build_hash(self, global_hash):
        if self.subpaths:
            key = hash(','.join(sorted(self.subpaths)))
            global_hash[key].append(self)
            for subfolder in self.sub.values():
                subfolder.build_hash(global_hash)


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        t = Trie()

        for path in paths:
            t.add(path)

        # scan duplicates
        path_hash = collections.defaultdict(list)
        for folder in t.sub.values():
            folder.build_hash(path_hash)
        # mark duplicates
        for folders in path_hash.values():
            if len(folders) == 1:
                continue
            for folder in folders:
                folder.deleted = True

        ans = []
        def dfs(folder, stack):
            if not folder or folder.deleted:
                return
            if folder.terminal:
                ans.append(stack)
            for subname, subfolder in folder.sub.items():
                dfs(subfolder, stack + [subname])
        
        dfs(t, [])
        return ans

