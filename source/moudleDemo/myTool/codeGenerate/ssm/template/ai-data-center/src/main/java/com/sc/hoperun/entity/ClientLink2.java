package com.sc.hoperun.entity;

import lombok.Data;

/**
 * @ClassName ClientLink2
 * @Description 客户资料
 * @Date 2019/06/19 11:25
 **/
@Data
public class ClientLink2 {

    // 编号
    private String clientId;
    // 用户名
    private String userName;
    // 密码
    private String password;
    // 创建时间
    private String createTime;
    // 权限级别
    private Integer level;


    public ClientLink2() {
    }

    public ClientLink2(String userName, String password, String createTime, Integer level) {
        this.userName = userName;
        this.password = password;
        this.createTime = createTime;
        this.level = level;

    }

    public ClientLink2(String clientId, String userName, String password, String createTime, Integer level) {
        this.clientId = clientId;
        this.userName = userName;
        this.password = password;
        this.createTime = createTime;
        this.level = level;

    }
}
