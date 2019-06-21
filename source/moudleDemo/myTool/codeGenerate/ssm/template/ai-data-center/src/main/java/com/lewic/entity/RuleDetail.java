package com.lewic.entity;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotNull;


/**
 * @author lewic
 * @apiNote 规则详情
 * @since 2019/6/14 15:38
 **/

@Data
@ApiModel(value = "规则")
public class RuleDetail {

    @ApiModelProperty(value = "编号", name = "ruleName")
    private String ruleId;

    @NotNull(message = "ruleName不能为null")
    @ApiModelProperty(value = "规则名称", name = "ruleName", example = "去僵死")
    private String ruleName;

    @ApiModelProperty(value = "描述", name = "description", example = "test desc")
    private String description;

}
