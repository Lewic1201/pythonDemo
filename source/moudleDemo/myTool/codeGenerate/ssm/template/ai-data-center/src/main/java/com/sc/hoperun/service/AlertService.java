package com.sc.hoperun.service;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.Alert;
import com.sc.hoperun.mapper.AlertMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @ClassName AlertService.java
 * @Description TODO
 * @Date 2019/6/13 15:10
 **/
@Service
@Slf4j
public class AlertService {
    @Autowired
    AlertMapper alertMapper;


    public Message listAlert(Integer pageNum, Integer pageSize) {
        Integer total = alertMapper.getAlertCount();
        Page page = new Page(pageSize, pageNum, total);
        Map<String, Object> resultMap = new HashMap<>();

        List<Alert> alerts = alertMapper.listAlert(page);
        resultMap.put("alertList", alerts);
        resultMap.put("page", page);

        Message msg = new Message();
        msg.setData(resultMap);
        return msg;
    }


    public Message getAlert(String id) {
        Alert alert = alertMapper.getAlert(id);

        Message msg = new Message();
        msg.setData(alert);
        return msg;
    }


    public Message insertAlert(String alertName, String severityLevel, String ruleType, String description,
                               String clients, String triggerTime) {
        Message msg = new Message();
        try {
            Alert alert = new Alert(alertName, severityLevel, ruleType, description, clients, triggerTime);
            alertMapper.insertAlert(alert);
            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateAlert(String alertId, String alertName, String severityLevel, String ruleType,
                               String description, String clients, String triggerTime) {
        Message msg = new Message();
        try {
            Alert alert = new Alert(alertId, alertName, severityLevel, ruleType, description, clients, triggerTime);
            alertMapper.updateAlert(alert);
            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteAlert(String tpId) {
        Message msg = new Message();
        try {
            alertMapper.deleteAlert(tpId);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
