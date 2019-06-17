package com.sc.hoperun.entity;

import lombok.Data;

/**
 * @ClassName ClientLink
 * @Description 客户联系方式
 * @Date 2019/6/14 15:32
 **/

@Data
public class ClientLink {

    // 编号
    private String clientId;
    // 用户名
    private String clientName;
    // 邮箱
    private String email;
    // 手机号
    private String mobile;

    public ClientLink() {
    }

    public ClientLink(String clientName, String email, String mobile) {
        this.clientName = clientName;
        this.email = email;
        this.mobile = mobile;
    }

    public ClientLink(String clientId, String clientName, String email, String mobile) {
        this.clientId = clientId;
        this.clientName = clientName;
        this.email = email;
        this.mobile = mobile;
    }
}
