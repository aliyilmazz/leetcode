package com.mybasepackage.medium.sortingandsearching;

import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;

public class MeetingRoomsTwo {

    public int minMeetingRooms(int[][] intervals) {
        Queue<int[]> sortedIntervals = new PriorityQueue<>((a, b) -> (a[0] - b[0]));

        int maxMeetingRoomCount = 0;

        Collections.addAll(sortedIntervals, intervals);

        Queue<Integer> meetingEndDates = new PriorityQueue<>();


        while (!sortedIntervals.isEmpty()) {
            int[] currentMeeting = sortedIntervals.poll();
            int currentMeetingStartDate = currentMeeting[0];
            int currentMeetingEndDate = currentMeeting[1];

            while (!meetingEndDates.isEmpty()) {
                // fast-forward to NOW: end all meetings with end_date earlier than now.
                // if meetings are already ended, then empty meeting rooms and make space for current meeting.
                int closestEndingDate = meetingEndDates.peek();
                if (closestEndingDate <= currentMeetingStartDate) {
                    meetingEndDates.poll(); // end meeting.
                } else {
                    break; // we run out of already-ended meetings. stop ending ongoing meetings, by `break`ing.
                }
            }
            meetingEndDates.add(currentMeetingEndDate);
            maxMeetingRoomCount = Math.max(maxMeetingRoomCount, meetingEndDates.size());
        }

        return maxMeetingRoomCount;
    }

    public static void main(String[] args) {
        MeetingRoomsTwo cls = new MeetingRoomsTwo();
        int[][] intervals = {{1,13}, {13,15}};
        int minMeetingRooms = cls.minMeetingRooms(intervals);
        System.out.println("Minimum rooms required: " + minMeetingRooms);
    }
}
