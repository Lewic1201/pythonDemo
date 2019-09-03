package com.lewic.mapper;

import com.lewic.common.Page;
import com.lewic.entity.RuleDetail;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;


/**
 * @author lewic
 * @apiNote 规则模板
 * @since 2019/6/14 15:38
 **/

@Mapper
public interface RuleDetailMapper {

    List<RuleDetail> listRuleDetail(@Param("page") Page page);

    RuleDetail getRuleDetail(@Param("ruleId") String ruleId);

    Integer getRuleDetailCount();

    void insertRuleDetail(RuleDetail ruleDetail);

    void updateRuleDetail(RuleDetail ruleDetail);

    void deleteRuleDetail(@Param("ruleId") String ruleId);
}

