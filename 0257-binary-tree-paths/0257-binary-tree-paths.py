# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node, current_path):
            if not node:
                return
            current_path += str(node.val)
            if not node.left and not node.right:
                result.append(current_path)
            else:
                current_path += "->"
                if node.left:
                    dfs(node.left, current_path)
                if node.right:
                    dfs(node.right, current_path)
                    
        dfs(root, "")
        return result
        