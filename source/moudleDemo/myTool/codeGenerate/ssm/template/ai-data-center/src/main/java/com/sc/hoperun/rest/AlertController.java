package com.sc.hoperun.rest;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.service.AlertService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * @ClassName AlertController
 * @Description TODO
 * @Date 2019/6/17 15:38
 **/

@RestController
@RequestMapping("/api/v1.0")
public class AlertController {
    @Autowired
    AlertService alertService;


    @ApiOperation("获取告警模板列表")
    @RequestMapping(value = "/alert", method = RequestMethod.GET)
    public Message listAlert(
            @ApiParam(value = "第几页") @RequestParam(required = false, value = "pageNum", defaultValue = "1") Integer pageNum,
            @ApiParam(value = "每页条数") @RequestParam(required = false, value = "pageSize", defaultValue = "10") Integer pageSize
    ) {
        return alertService.listAlert(pageNum, pageSize);
    }

    @ApiOperation("根据id获取告警模板")
    @RequestMapping(value = "/alert/{id}", method = RequestMethod.GET)
    public Message getAlert(@PathVariable(value = "id") String alertId) {
        return alertService.getAlert(alertId);
    }

    @ApiOperation("新增告警模板")
    @RequestMapping(value = "/alert", method = RequestMethod.POST)
    public Message insertAlert(
            @ApiParam(value = "告警名称") @RequestParam(value = "alertName") String alertName,
            @ApiParam(value = "严重程度") @RequestParam(value = "severityLevel") String severityLevel,
            @ApiParam(value = "规则类型") @RequestParam(value = "ruleType") String ruleType,
            @ApiParam(value = "描述") @RequestParam(value = "description") String description,
            @ApiParam(value = "用户") @RequestParam(value = "clients") String clients,
            @ApiParam(value = "触发时间") @RequestParam(value = "triggerTime") String triggerTime
    ) {
        return alertService.insertAlert(alertName, severityLevel, ruleType, description, clients, triggerTime);
    }

    @ApiOperation("更新告警模板")
    @RequestMapping(value = "/alert/{id}", method = RequestMethod.PATCH)
    public Message updateAlert(
            @PathVariable(value = "id") String alertId,
            @ApiParam(value = "告警名称") @RequestParam(value = "alertName") String alertName,
            @ApiParam(value = "严重程度") @RequestParam(value = "severityLevel") String severityLevel,
            @ApiParam(value = "规则类型") @RequestParam(value = "ruleType") String ruleType,
            @ApiParam(value = "描述") @RequestParam(value = "description") String description,
            @ApiParam(value = "用户") @RequestParam(value = "clients") String clients,
            @ApiParam(value = "触发时间") @RequestParam(value = "triggerTime") String triggerTime
    ) {
        return alertService.updateAlert(alertId, alertName, severityLevel, ruleType, description, clients, triggerTime);
    }

    @ApiOperation("删除告警模板")
    @RequestMapping(value = "/alert/{id}", method = RequestMethod.DELETE)
    public Message deleteAlert(@PathVariable(value = "id") String alertId) {
        return alertService.deleteAlert(alertId);
    }

}
