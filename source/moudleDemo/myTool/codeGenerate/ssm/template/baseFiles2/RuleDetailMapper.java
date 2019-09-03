package com.sc.hoperun.mapper;

import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.RuleDetail;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;


/**
 * @author lewic
 * @apiNote 规则模板
 * @since 2019/6/14 16:37
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

