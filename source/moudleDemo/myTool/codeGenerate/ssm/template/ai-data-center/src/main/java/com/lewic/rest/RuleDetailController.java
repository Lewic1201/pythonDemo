package com.lewic.rest;

import com.lewic.common.Message;
import com.lewic.common.Util;
import com.lewic.entity.RuleDetail;
import com.lewic.service.RuleDetailService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;


/**
 * @author lewic
 * @apiNote 规则模板
 * @since 2019/6/14 15:38
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
            @ApiParam(value = "告警模板") @RequestBody @Valid RuleDetail ruleDetail,
            BindingResult bindingResult
    ) {
        if (bindingResult.hasErrors()) {
            return Util.checkParam(bindingResult);
        }
        return ruleDetailService.insertRuleDetail(ruleDetail);
    }


    @ApiOperation("更新规则详情")
    @RequestMapping(value = "/ruleDetail/{id}", method = RequestMethod.PUT)
    public Message updateRuleDetail(
            @PathVariable(value = "id") String ruleId,
            @ApiParam(value = "告警模板") @RequestBody @Valid RuleDetail ruleDetail,
            BindingResult bindingResult
    ) {
        ruleDetail.setRuleId(ruleId);
        if (bindingResult.hasErrors()) {
            return Util.checkParam(bindingResult);
        }
        return ruleDetailService.updateRuleDetail(ruleDetail);
    }

    @ApiOperation("删除规则详情")
    @RequestMapping(value = "/ruleDetail/{id}", method = RequestMethod.DELETE)
    public Message deleteRuleDetail(@PathVariable(value = "id") String ruleId) {
        return ruleDetailService.deleteRuleDetail(ruleId);
    }

}

