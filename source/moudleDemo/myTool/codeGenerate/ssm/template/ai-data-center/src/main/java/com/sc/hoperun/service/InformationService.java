package com.sc.hoperun.service;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.Information;
import com.sc.hoperun.mapper.InformationMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @ClassName InformationService.java
 * @Description TODO
 * @Date 2019/6/13 15:10
 **/

@Service
@Slf4j
public class InformationService {
    @Autowired
    InformationMapper informationMapper;


    public Message listInformation(Integer pageNum, Integer pageSize) {
        Integer total = informationMapper.getInformationCount();
        Page page = new Page(pageSize, pageNum, total);
        Map<String, Object> resultMap = new HashMap<>();

        List<Information> informations = informationMapper.listInformation(page);
        resultMap.put("informationList", informations);
        resultMap.put("page", page);

        Message msg = new Message();
        msg.setData(resultMap);
        return msg;
    }


    public Message getInformation(String id) {
        Information information = informationMapper.getInformation(id);

        Message msg = new Message();
        msg.setData(information);
        return msg;
    }


    public Message insertInformation(String infoName, String tpId, String clientId, Integer isUsed, String updateTime) {
        Message msg = new Message();
        try {
            Information information = new Information(infoName, tpId, clientId, isUsed, updateTime);
            informationMapper.insertInformation(information);
            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateInformation(String infoId, String infoName, String tpId, String clientId, Integer isUsed,
                                     String updateTime) {
        Message msg = new Message();
        try {
            Information information = new Information(infoId, infoName, tpId, clientId, isUsed, updateTime);
            informationMapper.updateInformation(information);
            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteInformation(String tpId) {
        Message msg = new Message();
        try {
            informationMapper.deleteInformation(tpId);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
