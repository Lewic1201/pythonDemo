package com.sc.hoperun.entity;

import lombok.Data;


/**
 * @ClassName AlertTp
 * @Description 告警模板
 * @Date 2019/6/13 14:32
 **/
@Data
public class AlertTp {
    // 编号
    private String tpId;
    // 模板名称
    private String tpName;
    // 是否启用
    private Integer isUsed;
    // 选择规则
    private String rules;
    // 更新时间
    private String updateTime;
    // 描述
    private String description;

    public AlertTp() {
    }

    public AlertTp(String tpName, Integer isUsed, String rules, String updateTime, String description) {
        this.tpName = tpName;
        this.isUsed = isUsed;
        this.rules = rules;
        this.updateTime = updateTime;
        this.description = description;
    }

    public AlertTp(String tpId, String tpName, Integer isUsed, String rules, String updateTime, String description) {
        this.tpId = tpId;
        this.tpName = tpName;
        this.isUsed = isUsed;
        this.rules = rules;
        this.updateTime = updateTime;
        this.description = description;
    }
}
