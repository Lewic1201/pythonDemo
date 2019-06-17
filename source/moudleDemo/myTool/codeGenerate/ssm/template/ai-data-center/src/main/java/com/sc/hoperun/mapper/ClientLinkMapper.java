package com.sc.hoperun.mapper;

import com.sc.hoperun.common.Page;
import com.sc.hoperun.entity.ClientLink;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 * @ClassName ClientLinkMapper
 * @Description TODO
 * @Date 2019/6/14 19:49
 **/

@Mapper
public interface ClientLinkMapper {
    List<ClientLink> listClientLink(@Param("page") Page page);

    ClientLink getClientLink(@Param("clientId") String clientId);

    Integer getClientLinkCount();

    void insertClientLink(ClientLink clientLink);

    void updateClientLink(ClientLink clientLink);

    void deleteClientLink(@Param("clientId") String clientId);
}
