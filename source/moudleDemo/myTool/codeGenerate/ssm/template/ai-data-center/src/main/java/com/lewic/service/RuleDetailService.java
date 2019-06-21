package com.lewic.service;

import com.lewic.common.Message;
import com.lewic.common.Page;
import com.lewic.entity.RuleDetail;
import com.lewic.mapper.RuleDetailMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @ClassName RuleDetailService.java
 * @Description 规则模板
 * @Date 2019/6/13 15:10
 **/
@Service
@Slf4j
public class RuleDetailService {
    @Autowired
    RuleDetailMapper ruleDetailMapper;


    public Message listRuleDetail(Integer pageNum, Integer pageSize) {
        Integer total = ruleDetailMapper.getRuleDetailCount();
        Page page = new Page(pageSize, pageNum, total);
        Map<String, Object> resultMap = new HashMap<>();

        List<RuleDetail> ruleDetails = ruleDetailMapper.listRuleDetail(page);
        resultMap.put("ruleDetailList", ruleDetails);
        resultMap.put("page", page);

        Message<Map> msg = new Message<>();
        msg.setData(resultMap);
        return msg;
    }


    public Message getRuleDetail(String id) {
        RuleDetail ruleDetail = ruleDetailMapper.getRuleDetail(id);

        Message<RuleDetail> msg = new Message<>();
        msg.setData(ruleDetail);
        return msg;
    }


    public Message insertRuleDetail(RuleDetail ruleDetail) {
        Message<String> msg = new Message<>();
        try {
            ruleDetailMapper.insertRuleDetail(ruleDetail);
            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateRuleDetail(RuleDetail ruleDetail) {
        Message<String> msg = new Message<>();
        try {
            ruleDetailMapper.updateRuleDetail(ruleDetail);
            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteRuleDetail(String tpId) {
        Message<String> msg = new Message<>();
        try {
            ruleDetailMapper.deleteRuleDetail(tpId);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
