package com.mybasepackage.medium.sortingandsearching;

import com.mybasepackage.helpers.TreeNode;
import com.mybasepackage.helpers.BTreePrinter;


public class KthSmallestElementInBST {


    public void leftify(TreeNode root) {
        TreeNode rootTraverser = root;
        TreeNode pre;
        TreeNode previousParent = null;
        while (rootTraverser != null) {
            if (rootTraverser.left == null) {
                previousParent = rootTraverser;
                rootTraverser = rootTraverser.right;
            }
            else {
                pre = rootTraverser.left;
                while (pre.right != null) {
                    pre = pre.right;
                }
                pre.right = rootTraverser;
                TreeNode temp = rootTraverser;
                rootTraverser = rootTraverser.left;
                temp.left = null;
                if (previousParent != null) {
                    previousParent.right = rootTraverser;
                }
            }
        } // attach until there's no more in left.
    }


    public TreeNode leftOrientedTree(TreeNode root) {
        if (root == null) return null;
        TreeNode leftMostRoot = root;
        while (leftMostRoot.left != null) {
            leftMostRoot = leftMostRoot.left;
        }
        leftify(root);
        return leftMostRoot;
    }

    public int kthSmallest(TreeNode root, int k) {
        root = leftOrientedTree(root);
        //BTreePrinter.printNode(root);
        TreeNode desiredNode = root;
        for (int i=1; i<k; i++) {
            desiredNode = desiredNode.right;
        }
        return desiredNode.val;
    }


    public static void main(String[] args) {
        KthSmallestElementInBST cls = new KthSmallestElementInBST();
        TreeNode exampleTree = new BTreePrinter().buildTree(new Integer[]{
                41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23

        });
        //BTreePrinter.printNode(exampleTree);
        int k = 25;
        int kthSmallest = cls.kthSmallest(exampleTree, k);
        System.out.println(k + "th smallest: " + kthSmallest);
    }
}
