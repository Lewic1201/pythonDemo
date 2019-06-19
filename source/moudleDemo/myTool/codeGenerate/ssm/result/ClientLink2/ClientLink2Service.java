package com.sc.hoperun.service;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.ClientLink2;
import com.sc.hoperun.mapper.ClientLink2Mapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @ClassName ClientLink2Service.java
 * @Description 客户资料
 * @Date 2019/6/13 15:10
 **/
@Service
@Slf4j
public class ClientLink2Service {
    @Autowired
    ClientLink2Mapper clientLink2Mapper;


    public Message listClientLink2(Integer pageNum, Integer pageSize) {
        Integer total = clientLink2Mapper.getClientLink2Count();
        Page page = new Page(pageSize, pageNum, total);
        Map<String, Object> resultMap = new HashMap<>();

        List<ClientLink2> clientLink2s = clientLink2Mapper.listClientLink2(page);
        resultMap.put("clientLink2List", clientLink2s);
        resultMap.put("page", page);

        Message<Map> msg = new Message<>();
        msg.setData(resultMap);
        return msg;
    }


    public Message getClientLink2(String id) {
        ClientLink2 clientLink2 = clientLink2Mapper.getClientLink2(id);

        Message<ClientLink2> msg = new Message<>();
        msg.setData(clientLink2);
        return msg;
    }


    public Message insertClientLink2(String userName, String password, String createTime, Integer level) {
        Message<String> msg = new Message<>();
        try {
            ClientLink2 clientLink2 = new ClientLink2(userName, password, createTime, level);
            clientLink2Mapper.insertClientLink2(clientLink2);
            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateClientLink2(String clientId, String userName, String password, String createTime, Integer level) {
        Message<String> msg = new Message<>();
        try {
            ClientLink2 clientLink2 = new ClientLink2(clientId, userName, password, createTime, level);
            clientLink2Mapper.updateClientLink2(clientLink2);
            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteClientLink2(String tpId) {
        Message<String> msg = new Message<>();
        try {
            clientLink2Mapper.deleteClientLink2(tpId);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
