package com.sc.hoperun.mapper;

import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.ClientLink2;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * @Description 客户资料
 * @Date 2019/6/14 16:37
 **/
@Mapper
public interface ClientLink2Mapper {

    List<ClientLink2> listClientLink2(@Param("page") Page page);

    ClientLink2 getClientLink2(@Param("clientId") String clientId);

    Integer getClientLink2Count();

    void insertClientLink2(ClientLink2 clientLink2);

    void updateClientLink2(ClientLink2 clientLink2);

    void deleteClientLink2(@Param("clientId") String clientId);
}

