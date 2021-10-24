package com.mybasepackage.medium.treesandgraphs;

import com.mybasepackage.helpers.Node;

import java.util.LinkedList;
import java.util.Queue;

public class PopulatePointersInBinaryTree {

    Queue<Node> nodeQueue;

    public PopulatePointersInBinaryTree() {
        this.nodeQueue = new LinkedList<>();
    }

    public void _connect(Node node) {
        if (node == null) return;

        this.nodeQueue.add(node);

        Node leftMostNode;
        while (!this.nodeQueue.isEmpty()) {
            Queue<Node> nextLayerQueue = new LinkedList<>();
            leftMostNode = this.nodeQueue.remove();
            if (leftMostNode.left != null && leftMostNode.right != null) {
                nextLayerQueue.add(leftMostNode.left);
                nextLayerQueue.add(leftMostNode.right);
            }
            while (!this.nodeQueue.isEmpty()) {
                leftMostNode.next = this.nodeQueue.remove();
                leftMostNode = leftMostNode.next;
                if (leftMostNode.left != null && leftMostNode.right != null) {
                    nextLayerQueue.add(leftMostNode.left);
                    nextLayerQueue.add(leftMostNode.right);
                }
            }
            leftMostNode.next = null;
            this.nodeQueue = nextLayerQueue;
        }
    }

    public Node connect(Node node) {
        _connect(node);
        return node;
    }

    public static void main(String[] args) {
        PopulatePointersInBinaryTree cls = new PopulatePointersInBinaryTree();
        Node node = new Node(1,
                             new Node(2, new Node(4,
                                        new Node(-9), new Node(-8), null),
                                              new Node(5,
                                        new Node(-7), new Node(-6), null),
                                     null),
                             new Node(3, new Node(6,
                                        new Node(-5), new Node(-4), null),
                                              new Node(7,
                                        new Node(-3), new Node(-2), null),
                                      null),
                             null
                            );
        Node interConnectedNode = cls.connect(node);

    }
}
