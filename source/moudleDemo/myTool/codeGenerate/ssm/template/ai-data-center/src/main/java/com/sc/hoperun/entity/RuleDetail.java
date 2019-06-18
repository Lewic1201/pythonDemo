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
    // 描述
    private String description;

    public RuleDetail() {
    }

    public RuleDetail(String ruleName, String description) {
        this.ruleName = ruleName;
        this.description = description;
    }

    public RuleDetail(String ruleId, String ruleName, String description) {
        this.ruleId = ruleId;
        this.ruleName = ruleName;;
        this.description = description;
    }
}
