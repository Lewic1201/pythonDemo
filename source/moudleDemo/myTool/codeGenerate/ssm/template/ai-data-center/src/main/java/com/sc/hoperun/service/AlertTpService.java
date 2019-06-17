package com.sc.hoperun.service;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.AlertTp;
import com.sc.hoperun.mapper.AlertTpMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @ClassName AlertTpService.java
 * @Description TODO
 * @Date 2019/6/13 15:10
 **/
@Service
@Slf4j
public class AlertTpService {
    @Autowired
    AlertTpMapper alertTpMapper;


    public Message listAlertTp(Integer pageNum, Integer pageSize) {
        Integer total = alertTpMapper.getAlertTpCount();
        Page page = new Page(pageSize, pageNum, total);
        Map<String, Object> resultMap = new HashMap<>();

        List<AlertTp> alertTps = alertTpMapper.listAlertTp(page);
        resultMap.put("alertTpList", alertTps);
        resultMap.put("page", page);

        Message msg = new Message();
        msg.setData(resultMap);
        return msg;
    }


    public Message getAlertTp(String id) {
        AlertTp alertTp = alertTpMapper.getAlertTp(id);

        Message msg = new Message();
        msg.setData(alertTp);
        return msg;
    }


    public Message insertAlertTp(String tpName, Integer isUsed, String rules, String updateTime, String description) {
        Message msg = new Message();
        try {
            AlertTp alertTp = new AlertTp(tpName, isUsed, rules, updateTime, description);
            alertTpMapper.insertAlertTp(alertTp);
            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateAlertTp(String tpId, String tpName, Integer isUsed, String rules,
                                 String updateTime, String description) {
        Message msg = new Message();
        try {
            AlertTp alertTp = new AlertTp(tpId, tpName, isUsed, rules, updateTime, description);
            alertTpMapper.updateAlertTp(alertTp);
            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteAlertTp(String tpId) {
        Message msg = new Message();
        try {
            alertTpMapper.deleteAlertTp(tpId);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
