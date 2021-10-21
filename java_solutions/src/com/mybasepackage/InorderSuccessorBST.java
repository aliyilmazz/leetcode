package com.mybasepackage;

import com.mybasepackage.helpers.TreeNode;

public class InorderSuccessorBST {

    public TreeNode _inorderSuccessor(TreeNode root, Integer pVal, TreeNode greatest) {
        if (root.val > pVal) {
            return _inorderSuccessor(root.left, pVal, root);
        }
        else if (root.val < pVal) {
            return _inorderSuccessor(root.right, pVal, greatest);
        }
        else { // root is P
            if (root.right != null) {
                // find smallest in subtree
                TreeNode rightmostTraverser = root.right;
                while (rightmostTraverser.left != null) { rightmostTraverser = rightmostTraverser.left; }
                return rightmostTraverser;
            }
            else {
                // else, return greatest value
                return greatest;
            }
        }
    }


    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        return _inorderSuccessor(root, p.val, null);
    }

    public static void main(String[] args) {
        InorderSuccessorBST cls = new InorderSuccessorBST();
        TreeNode p = new TreeNode(2);
        TreeNode root = new TreeNode(1, p, new TreeNode(3));
        TreeNode ps = cls.inorderSuccessor(root, p);
        System.out.println("Successor val: " + ps.val);
    }
}
