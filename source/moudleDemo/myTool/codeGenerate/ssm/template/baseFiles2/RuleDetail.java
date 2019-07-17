package com.sc.hoperun.entity;

import lombok.Data;

/**
 * @author lewic
 * @apiNote 规则模板
 * @since 2019/6/14 15:38
 **/
@Data
public class RuleDetail {

    @ApiModelProperty(value = "编号", name = "ruleId", example = "1")
    private String ruleId;

    @ApiModelProperty(value = "规则名称", name = "ruleName", example = "test")
    private String ruleName;

    @ApiModelProperty(value = "描述", name = "description", example = "test")
    private String description;

}
