package com.mybasepackage;
import com.mybasepackage.helpers.TreeNode;
import com.mybasepackage.helpers.BTreePrinter;

import java.util.*;
import java.util.stream.IntStream;

public class ConstructBinaryTreeFromInorderAndPreorder {



    public TreeNode buildTree(int[] preorder, int[] inorder) {

        if (preorder == null && inorder == null) return new TreeNode();
        if (preorder.length==1 && inorder.length==1) return new TreeNode(preorder[0]);

        if (preorder.length==2 && inorder.length==2) {
            if (preorder[0] == inorder[1] && inorder[0] == preorder[1]) {
                return new TreeNode(preorder[0], new TreeNode(preorder[1]), null);
            }
            else if (Arrays.equals(preorder, inorder)) {
                return new TreeNode(preorder[0], null, new TreeNode(preorder[1]));
            }
        }

        TreeNode root = new TreeNode(preorder[0]);

        int index = 0;
        while (inorder[index] != root.val) {
            index++;
        }

        if (index != 0) {
            root.left = buildTree(
                    Arrays.copyOfRange(preorder, 1, 1+index),
                    Arrays.copyOfRange(inorder, 0, index)
            );
        }

        if (index < inorder.length-1) {
            root.right = buildTree(
                    Arrays.copyOfRange(preorder, 1+index, preorder.length),
                    Arrays.copyOfRange(inorder, index+1, inorder.length)
            );
        }


        return root;
    }

    public static void main(String[] args) {
        ConstructBinaryTreeFromInorderAndPreorder cls = new ConstructBinaryTreeFromInorderAndPreorder();

        // root, left, right
        int[] preorder = new int[]{1,2,3};

        // left, root, right
        int[] inorder = new int[]{3,2,1};

        TreeNode treeNode = cls.buildTree(preorder, inorder);

        System.out.println("New Tree: ");
        BTreePrinter.printNode(treeNode);
    }
}
