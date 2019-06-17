package com.sc.hoperun.mapper;

import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.Alert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface AlertMapper {

    List<Alert> listAlert(@Param("page") Page page);

    Alert getAlert(@Param("alertId") String alertId);

    Integer getAlertCount();

    void insertAlert(Alert alert);

    void updateAlert(Alert alert);

    void deleteAlert(@Param("alertId") String alertId);
}
