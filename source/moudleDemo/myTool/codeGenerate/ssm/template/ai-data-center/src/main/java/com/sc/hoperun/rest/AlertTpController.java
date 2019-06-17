package com.sc.hoperun.rest;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.service.AlertTpService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * @ClassName AlertTpController.java
 * @Description TODO
 * @Date 2019/6/13 15:22
 **/
@RestController
@RequestMapping("/api/v1.0")
public class AlertTpController {
    @Autowired
    AlertTpService alertTpService;


    @ApiOperation("获取告警模板列表")
    @RequestMapping(value = "/alertTp", method = RequestMethod.GET)
    public Message listAlertTp(
            @ApiParam(value = "第几页") @RequestParam(required = false, value = "pageNum", defaultValue = "1") Integer pageNum,
            @ApiParam(value = "每页条数") @RequestParam(required = false, value = "pageSize", defaultValue = "10") Integer pageSize
    ) {
        return alertTpService.listAlertTp(pageNum, pageSize);
    }

    @ApiOperation("根据id获取告警模板")
    @RequestMapping(value = "/alertTp/{id}", method = RequestMethod.GET)
    public Message getAlertTp(@PathVariable(value = "id") String tpId) {
        return alertTpService.getAlertTp(tpId);
    }

    @ApiOperation("新增告警模板")
    @RequestMapping(value = "/alertTp", method = RequestMethod.POST)
    public Message insertAlertTp(
            @ApiParam(value = "模板名称") @RequestParam(value = "tpName") String tpName,
            @ApiParam(value = "是否启用") @RequestParam(value = "isUsed") Integer isUsed,
            @ApiParam(value = "规则") @RequestParam(value = "rules") String rules,
            @ApiParam(value = "更新时间") @RequestParam(value = "updateTime") String updateTime,
            @ApiParam(value = "描述") @RequestParam(value = "description") String description
    ) {
        return alertTpService.insertAlertTp(tpName, isUsed, rules, updateTime, description);
    }

    @ApiOperation("更新告警模板")
    @RequestMapping(value = "/alertTp/{id}", method = RequestMethod.PATCH)
    public Message updateAlertTp(
            @PathVariable(value = "id") String tpId,
            @ApiParam(value = "模板名称") @RequestParam(value = "tpName") String tpName,
            @ApiParam(value = "是否启用") @RequestParam(value = "isUsed") Integer isUsed,
            @ApiParam(value = "规则") @RequestParam(value = "rules") String rules,
            @ApiParam(value = "更新时间") @RequestParam(value = "updateTime") String updateTime,
            @ApiParam(value = "描述") @RequestParam(value = "description") String description
    ) {
        return alertTpService.updateAlertTp(tpId, tpName, isUsed, rules, updateTime, description);
    }

    @ApiOperation("删除告警模板")
    @RequestMapping(value = "/alertTp/{id}", method = RequestMethod.DELETE)
    public Message deleteAlertTp(@PathVariable(value = "id") String tpId) {
        return alertTpService.deleteAlertTp(tpId);
    }

}
