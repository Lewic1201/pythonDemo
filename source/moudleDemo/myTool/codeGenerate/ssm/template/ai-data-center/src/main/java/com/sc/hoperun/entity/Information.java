package com.sc.hoperun.entity;

import lombok.Data;

/**
 * @ClassName Information
 * @Description 通知管理
 * @Date 2019/6/14 16:21
 **/

@Data
public class Information {


    // 编号
    private String infoId;
    // 通知名称
    private String infoName;
    // 选择模板
    private String tpId;
    // 选择用户
    private String clientId;
    // 是否开启
    private Integer isUsed;
    // 更新时间
    private String updateTime;

    public Information() {
    }

    public Information(String infoName, String tpId, String clientId, Integer isUsed, String updateTime) {
        this.infoName = infoName;
        this.tpId = tpId;
        this.clientId = clientId;
        this.isUsed = isUsed;
        this.updateTime = updateTime;
    }

    public Information(String infoId, String infoName, String tpId, String clientId, Integer isUsed, String updateTime) {
        this.infoId = infoId;
        this.infoName = infoName;
        this.tpId = tpId;
        this.clientId = clientId;
        this.isUsed = isUsed;
        this.updateTime = updateTime;
    }
}
