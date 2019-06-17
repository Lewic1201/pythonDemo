package com.sc.hoperun.service;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.ClientLink;
import com.sc.hoperun.mapper.ClientLinkMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @ClassName ClientLinkService
 * @Description TODO
 * @Date 2019/6/17 16:52
 **/

@Service
@Slf4j
public class ClientLinkService {

    @Autowired
    ClientLinkMapper clientLinkMapper;


    public Message listClientLink(Integer pageNum, Integer pageSize) {
        Integer total = clientLinkMapper.getClientLinkCount();
        Page page = new Page(pageSize, pageNum, total);
        Map<String, Object> resultMap = new HashMap<>();

        List<ClientLink> clientLinks = clientLinkMapper.listClientLink(page);
        resultMap.put("clientLinkList", clientLinks);
        resultMap.put("page", page);

        Message msg = new Message();
        msg.setData(resultMap);
        return msg;
    }


    public Message getClientLink(String id) {
        ClientLink clientLink = clientLinkMapper.getClientLink(id);

        Message msg = new Message();
        msg.setData(clientLink);
        return msg;
    }


    public Message insertClientLink(String clientName, String email, String mobile) {
        Message msg = new Message();
        try {
            ClientLink clientLink = new ClientLink(clientName, email, mobile);
            clientLinkMapper.insertClientLink(clientLink);
            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateClientLink(String clientId, String clientName, String email, String mobile) {
        Message msg = new Message();
        try {
            ClientLink clientLink = new ClientLink(clientId, clientName, email, mobile);
            clientLinkMapper.updateClientLink(clientLink);
            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteClientLink(String clientId) {
        Message msg = new Message();
        try {
            clientLinkMapper.deleteClientLink(clientId);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
