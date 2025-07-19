'''
2024/10/25 daily challenge
2025/07/19 daily challenge

Trie + recursion approach
'''


class Trie:
    def __init__(self, folder_name="", terminal_flag=False):
        self.folder_name = folder_name
        self.terminal_flag = terminal_flag
        self.subfolders = dict()


class Solution:
    def removeSubfolders(self, folder_list: List[str]) -> List[str]:
        root = Trie()

        for path in folder_list:
            subs = path.split("/")
            node = root
            for f in subs:
                if not f: continue
                if f not in node.subfolders:
                    new_node = Trie(f)
                    node.subfolders[f] = new_node
                    node = new_node
                else:
                    node = node.subfolders[f]
                # shortcut: a parent path found,
                # no need to iterate another subfolder.
                if node.terminal_flag:
                    break
            else:
                # set end of path flag
                node.terminal_flag = True

        ans = []
        slices = []

        def traverse(node):
            slices.append(node.folder_name)
            if node.terminal_flag:
                ans.append('/'.join(slices))
            else:
                for child in node.subfolders.values():
                    traverse(child)
            slices.pop()

        traverse(root)

        return ans


'''
set approach
'''


class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        fs = set(folders)
        for fname in folders:
            levels = fname.split('/')
            for i in range(2, len(levels)):
                parent = '/'.join(levels[:i])
                if parent in fs:
                    fs.remove(fname)
                    break
        return list(fs)

