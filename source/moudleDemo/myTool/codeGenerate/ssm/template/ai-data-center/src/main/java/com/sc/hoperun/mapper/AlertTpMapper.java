package com.sc.hoperun.mapper;

import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.AlertTp;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface AlertTpMapper {

    List<AlertTp> listAlertTp(@Param("page") Page page);

    AlertTp getAlertTp(@Param("tpId") String tpId);

    Integer getAlertTpCount();

    void insertAlertTp(AlertTp alertTp);

    void updateAlertTp(AlertTp alertTp);

    void deleteAlertTp(@Param("tpId") String tpId);
}
