package com.mybasepackage;

import com.mybasepackage.helpers.TreeNode;
import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreeZigzagLevelOrderTraversal {

    List<List<Integer>> zigzagIntegers;

    public BinaryTreeZigzagLevelOrderTraversal() {
        this.zigzagIntegers = new ArrayList<>();
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return this.zigzagIntegers;

        List<TreeNode> currentChildren = new ArrayList<>(List.of(root));
        this.zigzagIntegers.add(new ArrayList<>(List.of(root.val)));
        currentChildren = new ArrayList<>();

        if (root.left != null) currentChildren.add(root.left);
        if (root.right != null) currentChildren.add(root.right);


        boolean leftToRight = false;

        while (currentChildren.size() != 0) {
            List<Integer> childrenValues = new ArrayList<>();
            List<TreeNode> nextChildren = new ArrayList<>();
            int childrenCount = currentChildren.size();
            int index;
            for (int i=0; i<childrenCount; i++) {
                if (leftToRight) {
                    index = i;
                }
                else {
                    index = (childrenCount-1) - i; // complementary of `i` w.r.t. size (reverse iteration)
                }
                TreeNode currentChild = currentChildren.get(index);
                childrenValues.add(currentChild.val);
                TreeNode inherentChild = currentChildren.get(i);
                if (inherentChild.left != null) nextChildren.add(inherentChild.left);
                if (inherentChild.right != null) nextChildren.add(inherentChild.right);
            }
            currentChildren = nextChildren;
            this.zigzagIntegers.add(childrenValues);
            leftToRight = !leftToRight; // rotate direction for next iteration
        }
        return this.zigzagIntegers;
    }

    public static void main(String[] args) {
        BinaryTreeZigzagLevelOrderTraversal cls = new BinaryTreeZigzagLevelOrderTraversal();
        TreeNode exampleTree = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3));
        List<List<Integer>> zigzagIntegers = cls.zigzagLevelOrder(exampleTree);
        System.out.println("Integers: " + zigzagIntegers.toString());
    }
}
