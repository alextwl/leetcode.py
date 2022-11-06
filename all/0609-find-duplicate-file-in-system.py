'''
2022/09/19 daily challenge

quite easy when code in python and use dict as hash map

it's worth to do more follow ups in different low-level langs later.
'''

from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_file_map = defaultdict(list)
        
        for dir_str in paths:
            dir_table = iter(dir_str.split(' '))
            # extract directory path first
            dir_path = next(dir_table)
            
            # and then extract files in the directory
            for file_content in dir_table:
                file_name, content_body = file_content[:-1].split('(')  # strip ')' and split by '('
                content_file_map[content_body].append("%s/%s" % (dir_path, file_name))
        
        # find duplicates
        ans = list()
        for file_list in content_file_map.values():
            if len(file_list) > 1:
                ans.append(file_list)
        
        return ans
