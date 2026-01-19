package com.shopflag.chrisrathana main;

public class DecisionEngine {
    public String decide(SystemStatus status) {
        if (status.cpuUsage > 80 || status.memoryUsage > 85) {
            return "RESTART_SERVICE";
        } else if (status.cpuUsage < 20 && status.memoryUsage < 30) {
            return "IDLE_MODE";
        } else {
            return "NORMAL";
        }
    }
}