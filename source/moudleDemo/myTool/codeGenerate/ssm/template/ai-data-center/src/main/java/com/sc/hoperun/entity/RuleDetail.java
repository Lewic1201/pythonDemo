package com.sc.hoperun.entity;

import lombok.Data;

/**
 * @ClassName RuleDetail
 * @Description 规则详情
 * @Date 2019/6/14 15:38
 **/
@Data
public class RuleDetail {

    // 编号
    private String ruleId;
    // 规则名称
    private String ruleName;
    // 通知策略
    private String infoScheme;
    // 规则类型
    private String ruleType;
    // 告警策略
    private String alertScheme;
    // 告警规则
    private String alertRule;
    // 阈值及告警级别
    private String threshold;
    // 重大
    private Integer severityValue;
    // 紧急
    private Integer urgencyValue;
    // 一般
    private Integer generalValue;
    // 最大通知数
    private String infoMaxNum;
    // 重复周期
    private String period;
    // 是否开启
    private Integer isUsed;
    // 描述
    private String description;

    public RuleDetail() {
    }

    public RuleDetail(String ruleName, String infoScheme, String ruleType, String alertScheme, String alertRule, String threshold, Integer severityValue, Integer urgencyValue, Integer generalValue, String infoMaxNum, String period, Integer isUsed, String description) {
        this.ruleName = ruleName;
        this.infoScheme = infoScheme;
        this.ruleType = ruleType;
        this.alertScheme = alertScheme;
        this.alertRule = alertRule;
        this.threshold = threshold;
        this.severityValue = severityValue;
        this.urgencyValue = urgencyValue;
        this.generalValue = generalValue;
        this.infoMaxNum = infoMaxNum;
        this.period = period;
        this.isUsed = isUsed;
        this.description = description;
    }

    public RuleDetail(String ruleId, String ruleName, String infoScheme, String ruleType, String alertScheme, String alertRule, String threshold, Integer severityValue, Integer urgencyValue, Integer generalValue, String infoMaxNum, String period, Integer isUsed, String description) {
        this.ruleId = ruleId;
        this.ruleName = ruleName;
        this.infoScheme = infoScheme;
        this.ruleType = ruleType;
        this.alertScheme = alertScheme;
        this.alertRule = alertRule;
        this.threshold = threshold;
        this.severityValue = severityValue;
        this.urgencyValue = urgencyValue;
        this.generalValue = generalValue;
        this.infoMaxNum = infoMaxNum;
        this.period = period;
        this.isUsed = isUsed;
        this.description = description;
    }
}
