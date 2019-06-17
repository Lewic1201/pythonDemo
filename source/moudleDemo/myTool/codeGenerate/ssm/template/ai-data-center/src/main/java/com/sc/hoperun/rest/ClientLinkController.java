package com.sc.hoperun.rest;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.service.ClientLinkService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * @ClassName ClientLinkController
 * @Description TODO
 * @Date 2019/6/14 19:55
 **/

@RestController
@RequestMapping("/api/v1.0")
public class ClientLinkController {
    @Autowired
    ClientLinkService clientLinkService;


    @ApiOperation("获取告警模板列表")
    @RequestMapping(value = "/clientLink", method = RequestMethod.GET)
    public Message listClientLink(
            @ApiParam(value = "第几页") @RequestParam(required = false, value = "pageNum", defaultValue = "1") Integer pageNum,
            @ApiParam(value = "每页条数") @RequestParam(required = false, value = "pageSize", defaultValue = "10") Integer pageSize
    ) {
        return clientLinkService.listClientLink(pageNum, pageSize);
    }

    @ApiOperation("根据id获取告警模板")
    @RequestMapping(value = "/clientLink/{id}", method = RequestMethod.GET)
    public Message getClientLink(@PathVariable(value = "id") String clientId) {
        return clientLinkService.getClientLink(clientId);
    }

    @ApiOperation("新增用户联系")
    @RequestMapping(value = "/clientLink", method = RequestMethod.POST)
    public Message insertClientLink(
            @ApiParam(value = "用户名") @RequestParam(value = "clientName") String clientName,
            @ApiParam(value = "邮箱") @RequestParam(value = "email") String email,
            @ApiParam(value = "手机号") @RequestParam(value = "mobile") String mobile
    ) {
        return clientLinkService.insertClientLink(clientName, email, mobile);
    }

    @ApiOperation("更新告警模板")
    @RequestMapping(value = "/clientLink/{id}", method = RequestMethod.PATCH)
    public Message updateClientLink(
            @PathVariable(value = "id") String clientId,
            @ApiParam(value = "用户名") @RequestParam(value = "clientName") String clientName,
            @ApiParam(value = "邮箱") @RequestParam(value = "email") String email,
            @ApiParam(value = "手机号") @RequestParam(value = "mobile") String mobile
    ) {
        return clientLinkService.updateClientLink(clientId, clientName, email, mobile);
    }

    @ApiOperation("删除告警模板")
    @RequestMapping(value = "/clientLink/{id}", method = RequestMethod.DELETE)
    public Message deleteClientLink(@PathVariable(value = "id") String clientId) {
        return clientLinkService.deleteClientLink(clientId);
    }

}
