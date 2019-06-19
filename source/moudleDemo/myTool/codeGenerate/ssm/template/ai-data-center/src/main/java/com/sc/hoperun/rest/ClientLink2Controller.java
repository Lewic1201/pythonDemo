package com.sc.hoperun.rest;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.service.ClientLink2Service;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


/**
 * @ClassName ClientLink2Controller.java
 * @Description 客户资料
 * @Date 2019/6/13 15:22
 **/
@RestController
@RequestMapping("/api/v1.0")
public class ClientLink2Controller {
    @Autowired
    ClientLink2Service clientLink2Service;


    @ApiOperation("获取客户资料列表")
    @RequestMapping(value = "/clientLink2", method = RequestMethod.GET)
    public Message listClientLink2(
            @ApiParam(value = "第几页") @RequestParam(required = false, value = "pageNum", defaultValue = "1") Integer pageNum,
            @ApiParam(value = "每页条数") @RequestParam(required = false, value = "pageSize", defaultValue = "10") Integer pageSize
    ) {
        return clientLink2Service.listClientLink2(pageNum, pageSize);
    }

    @ApiOperation("根据id查询客户资料")
    @RequestMapping(value = "/clientLink2/{id}", method = RequestMethod.GET)
    public Message getClientLink2(
            @PathVariable(value = "id") String clientId
    ) {
        return clientLink2Service.getClientLink2(clientId);
    }

    @ApiOperation("新建客户资料")
    @RequestMapping(value = "/clientLink2", method = RequestMethod.POST)
    public Message insertClientLink2(
            @ApiParam(value = "用户名") @RequestParam(value = "userName") String userName,
            @ApiParam(value = "密码") @RequestParam(value = "password") String password,
            @ApiParam(value = "创建时间") @RequestParam(value = "createTime") String createTime,
            @ApiParam(value = "权限级别") @RequestParam(value = "level") Integer level
    ) {
        return clientLink2Service.insertClientLink2(userName, password, createTime, level);
    }


    @ApiOperation("更新客户资料")
    @RequestMapping(value = "/clientLink2/{id}", method = RequestMethod.PUT)
    public Message updateClientLink2(
            @PathVariable(value = "id") String clientId,
            @ApiParam(value = "用户名") @RequestParam(value = "userName") String userName,
            @ApiParam(value = "密码") @RequestParam(value = "password") String password,
            @ApiParam(value = "创建时间") @RequestParam(value = "createTime") String createTime,
            @ApiParam(value = "权限级别") @RequestParam(value = "level") Integer level
    ) {
        return clientLink2Service.updateClientLink2(clientId, userName, password, createTime, level);
    }

    @ApiOperation("删除客户资料")
    @RequestMapping(value = "/clientLink2/{id}", method = RequestMethod.DELETE)
    public Message deleteClientLink2(@PathVariable(value = "id") String clientId) {
        return clientLink2Service.deleteClientLink2(clientId);
    }

}

