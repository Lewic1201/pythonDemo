package com.sc.hoperun.mapper;

import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.Information;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface InformationMapper {
    List<Information> listInformation(@Param("page") Page page);

    Information getInformation(@Param("infoId") String infoId);

    Integer getInformationCount();

    void insertInformation(Information information);

    void updateInformation(Information information);

    void deleteInformation(@Param("infoId") String infoId);
}
