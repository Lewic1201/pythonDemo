package com.sc.hoperun.rest;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.service.RuleDetailService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


/**
 * @ClassName RuleDetailController.java
 * @Description TODO
 * @Date 2019/6/13 15:22
 **/
@RestController
@RequestMapping("/api/v1.0")
public class RuleDetailController {
    @Autowired
    RuleDetailService ruleDetailService;


    @ApiOperation("获取规则模板列表")
    @RequestMapping(value = "/ruleDetail", method = RequestMethod.GET)
    public Message listRuleDetail(
            @ApiParam(value = "第几页") @RequestParam(required = false, value = "pageNum", defaultValue = "1") Integer pageNum,
            @ApiParam(value = "每页条数") @RequestParam(required = false, value = "pageSize", defaultValue = "10") Integer pageSize
    ) {
        return ruleDetailService.listRuleDetail(pageNum, pageSize);
    }

    @ApiOperation("根据id查询规则模板")
    @RequestMapping(value = "/ruleDetail/{id}", method = RequestMethod.GET)
    public Message getRuleDetail(
            @PathVariable(value = "id") String ruleId
    ) {
        return ruleDetailService.getRuleDetail(ruleId);
    }

    @ApiOperation("新建规则详情")
    @RequestMapping(value = "/ruleDetail", method = RequestMethod.POST)
    public Message insertRuleDetail(
            @ApiParam(value = "规则名称") @RequestParam(value = "ruleName") String ruleName,
            @ApiParam(value = "通知策略") @RequestParam(value = "infoScheme") String infoScheme,
            @ApiParam(value = "规则类型") @RequestParam(value = "ruleType") String ruleType,
            @ApiParam(value = "告警策略") @RequestParam(value = "alertScheme") String alertScheme,
            @ApiParam(value = "告警规则") @RequestParam(value = "alertRule") String alertRule,
            @ApiParam(value = "阈值及告警级别") @RequestParam(value = "threshold") String threshold,
            @ApiParam(value = "重大") @RequestParam(value = "severityValue") Integer severityValue,
            @ApiParam(value = "紧急") @RequestParam(value = "urgencyValue") Integer urgencyValue,
            @ApiParam(value = "一般") @RequestParam(value = "generalValue") Integer generalValue,
            @ApiParam(value = "最大通知数") @RequestParam(value = "infoMaxNum") String infoMaxNum,
            @ApiParam(value = "重复周期") @RequestParam(value = "period") String period,
            @ApiParam(value = "是否开启") @RequestParam(value = "isUsed") Integer isUsed,
            @ApiParam(value = "描述") @RequestParam(value = "description") String description
    ) {
        return ruleDetailService.insertRuleDetail(ruleName, infoScheme, ruleType, alertScheme, alertRule,
                threshold, severityValue, urgencyValue, generalValue, infoMaxNum, period, isUsed, description);
    }


    @ApiOperation("更新规则详情")
    @RequestMapping(value = "/ruleDetail/{id}", method = RequestMethod.PUT)
    public Message updateRuleDetail(
            @PathVariable(value = "id") String ruleId,
            @ApiParam(value = "规则名称") @RequestParam(value = "ruleName") String ruleName,
            @ApiParam(value = "通知策略") @RequestParam(value = "infoScheme") String infoScheme,
            @ApiParam(value = "规则类型") @RequestParam(value = "ruleType") String ruleType,
            @ApiParam(value = "告警策略") @RequestParam(value = "alertScheme") String alertScheme,
            @ApiParam(value = "告警规则") @RequestParam(value = "alertRule") String alertRule,
            @ApiParam(value = "阈值及告警级别") @RequestParam(value = "threshold") String threshold,
            @ApiParam(value = "重大") @RequestParam(value = "severityValue") Integer severityValue,
            @ApiParam(value = "紧急") @RequestParam(value = "urgencyValue") Integer urgencyValue,
            @ApiParam(value = "一般") @RequestParam(value = "generalValue") Integer generalValue,
            @ApiParam(value = "最大通知数") @RequestParam(value = "infoMaxNum") String infoMaxNum,
            @ApiParam(value = "重复周期") @RequestParam(value = "period") String period,
            @ApiParam(value = "是否开启") @RequestParam(value = "isUsed") Integer isUsed,
            @ApiParam(value = "描述") @RequestParam(value = "description") String description
    ) {
        return ruleDetailService.updateRuleDetail(ruleId, ruleName, infoScheme, ruleType, alertScheme, alertRule,
                threshold, severityValue, urgencyValue, generalValue, infoMaxNum, period, isUsed, description);
    }

    @ApiOperation("删除规则详情")
    @RequestMapping(value = "/ruleDetail/{id}", method = RequestMethod.DELETE)
    public Message deleteRuleDetail(@PathVariable(value = "id") String ruleId) {
        return ruleDetailService.deleteRuleDetail(ruleId);
    }

}

