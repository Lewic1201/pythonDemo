package com.sc.hoperun.entity;

import lombok.Data;

/**
 * @ClassName Alert
 * @Description TODO
 * @Date 2019/6/17 15:46
 **/
@Data
public class Alert {

    // 告警id
    private String alertId;
    // 告警名称
    private String alertName;
    // 严重程度
    private String severityLevel;
    // 规则类型
    private String ruleType;
    // 描述
    private String description;
    // 用户
    private String clients;
    // 触发时间
    private String triggerTime;

    public Alert() {
    }

    public Alert(String alertName, String severityLevel, String ruleType, String description, String clients, String triggerTime) {
        this.alertName = alertName;
        this.severityLevel = severityLevel;
        this.ruleType = ruleType;
        this.description = description;
        this.clients = clients;
        this.triggerTime = triggerTime;
    }

    public Alert(String alertId, String alertName, String severityLevel, String ruleType, String description, String clients, String triggerTime) {
        this.alertId = alertId;
        this.alertName = alertName;
        this.severityLevel = severityLevel;
        this.ruleType = ruleType;
        this.description = description;
        this.clients = clients;
        this.triggerTime = triggerTime;
    }
}
