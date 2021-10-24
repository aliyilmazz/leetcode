package com.mybasepackage.medium.dynamicprogramming;

import java.util.HashMap;

public class JumpGame {


    HashMap<Integer, Boolean> jumpingMap;
    int[] nums;

    public JumpGame() {
        jumpingMap = new HashMap<>();
    }

    public boolean _jump(int index) {
        if (jumpingMap.containsKey(index)) {
            return jumpingMap.get(index);
        }


        int maximumJumpLength = this.nums[index];
        if (index+maximumJumpLength >= this.nums.length-1) {
            jumpingMap.put(index, true);
            return true;
        }

        boolean canJump = false;
        int currentJumpLength = 1;
        // if maximumJumpLength = 0, we skip the while-loop and return false right away.
        while (currentJumpLength<=maximumJumpLength && index+currentJumpLength < this.nums.length) {
            canJump = _jump(index+currentJumpLength);
            currentJumpLength++;
            if (canJump) {
                jumpingMap.put(index, canJump);
                return true;
            }
        }

        jumpingMap.put(index, canJump);
        return canJump;
    }

    public boolean canJump(int[] nums) {

        jumpingMap.put(nums.length-1, true);
        this.nums = nums;

        boolean result = _jump(0);
        return result;
    }

    public static void main(String[] args) {
        JumpGame cls = new JumpGame();
        int[] nums = {2,3,1,1,4};
        boolean canJump = cls.canJump(nums);
        System.out.println("Can jump: " + canJump);
    }
}
