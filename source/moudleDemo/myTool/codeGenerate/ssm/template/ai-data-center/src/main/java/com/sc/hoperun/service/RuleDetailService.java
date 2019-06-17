package com.sc.hoperun.service;

import com.sc.hoperun.common.Message;
import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.RuleDetail;
import com.sc.hoperun.mapper.RuleDetailMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @ClassName RuleDetailService.java
 * @Description TODO
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

        Message msg = new Message();
        msg.setData(resultMap);
        return msg;
    }


    public Message getRuleDetail(String id) {
        RuleDetail ruleDetail = ruleDetailMapper.getRuleDetail(id);

        Message msg = new Message();
        msg.setData(ruleDetail);
        return msg;
    }


    public Message insertRuleDetail(String ruleName, String infoScheme, String ruleType,
                                    String alertScheme, String alertRule, String threshold, Integer severityValue,
                                    Integer urgencyValue, Integer generalValue, String infoMaxNum, String period,
                                    Integer isUsed, String description) {
        Message msg = new Message();
        try {
            RuleDetail ruleDetail = new RuleDetail(ruleName, infoScheme, ruleType, alertScheme, alertRule,
                    threshold, severityValue, urgencyValue, generalValue, infoMaxNum, period, isUsed, description);
            ruleDetailMapper.insertRuleDetail(ruleDetail);
            msg.setData("insert success");
        } catch (Exception e) {
            msg.setMessage("insert failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message updateRuleDetail(String ruleId, String ruleName, String infoScheme, String ruleType,
                                    String alertScheme, String alertRule, String threshold, Integer severityValue,
                                    Integer urgencyValue, Integer generalValue, String infoMaxNum, String period,
                                    Integer isUsed, String description) {
        Message msg = new Message();
        try {
            RuleDetail ruleDetail = new RuleDetail(ruleId, ruleName, infoScheme, ruleType, alertScheme, alertRule,
                    threshold, severityValue, urgencyValue, generalValue, infoMaxNum, period, isUsed, description);
            ruleDetailMapper.updateRuleDetail(ruleDetail);
            msg.setData("update success");
        } catch (Exception e) {
            msg.setMessage("update failed, because: " + e.getMessage());
        }
        return msg;
    }

    public Message deleteRuleDetail(String tpId) {
        Message msg = new Message();
        try {
            ruleDetailMapper.deleteRuleDetail(tpId);
            msg.setData("delete success");
        } catch (Exception e) {
            msg.setMessage("delete failed, because:" + e.getMessage());
        }
        return msg;
    }

}
