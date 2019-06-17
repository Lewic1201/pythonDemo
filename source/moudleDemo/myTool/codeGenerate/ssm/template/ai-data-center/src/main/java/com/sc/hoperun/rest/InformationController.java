package com.sc.hoperun.rest;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.service.InformationService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import io.swagger.models.auth.In;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * @ClassName InformationController.java
 * @Description TODO
 * @Date 2019/6/13 15:22
 **/
@RestController
@RequestMapping("/api/v1.0")
public class InformationController {
    @Autowired
    InformationService informationService;


    @ApiOperation("获取告警模板列表")
    @RequestMapping(value = "/information", method = RequestMethod.GET)
    public Message listInformation(
            @ApiParam(value = "第几页") @RequestParam(required = false, value = "pageNum", defaultValue = "1") Integer pageNum,
            @ApiParam(value = "每页条数") @RequestParam(required = false, value = "pageSize", defaultValue = "10") Integer pageSize
    ) {
        return informationService.listInformation(pageNum, pageSize);
    }

    @ApiOperation("根据id获取告警模板")
    @RequestMapping(value = "/information/{id}", method = RequestMethod.GET)
    public Message getInformation(@PathVariable(value = "id") String infoId) {
        return informationService.getInformation(infoId);
    }

    @ApiOperation("新增告警模板")
    @RequestMapping(value = "/information", method = RequestMethod.POST)
    public Message insertInformation(
            @ApiParam(value = "通知名称") @RequestParam(value = "infoName") String infoName,
            @ApiParam(value = "选择模板") @RequestParam(value = "tpId") String tpId,
            @ApiParam(value = "选择用户") @RequestParam(value = "clientId") String clientId,
            @ApiParam(value = "是否开启") @RequestParam(value = "isUsed") Integer isUsed,
            @ApiParam(value = "更新时间") @RequestParam(value = "updateTime") String updateTime
    ) {
        return informationService.insertInformation(infoName, tpId, clientId, isUsed, updateTime);
    }

    @ApiOperation("更新告警模板")
    @RequestMapping(value = "/information/{id}", method = RequestMethod.PATCH)
    public Message updateInformation(
            @PathVariable(value = "id") String infoId,
            @ApiParam(value = "通知名称") @RequestParam(value = "infoName") String infoName,
            @ApiParam(value = "选择模板") @RequestParam(value = "tpId") String tpId,
            @ApiParam(value = "选择用户") @RequestParam(value = "clientId") String clientId,
            @ApiParam(value = "是否开启") @RequestParam(value = "isUsed") Integer isUsed,
            @ApiParam(value = "更新时间") @RequestParam(value = "updateTime") String updateTime
    ) {
        return informationService.updateInformation(infoId, infoName, tpId, clientId, isUsed, updateTime);
    }

    @ApiOperation("删除告警模板")
    @RequestMapping(value = "/information/{id}", method = RequestMethod.DELETE)
    public Message deleteInformation(@PathVariable(value = "id") String infoId) {
        return informationService.deleteInformation(infoId);
    }

}
