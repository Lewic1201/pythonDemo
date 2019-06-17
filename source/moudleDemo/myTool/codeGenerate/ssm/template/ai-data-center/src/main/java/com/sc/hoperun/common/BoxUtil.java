package com.sc.hoperun.common;


import lombok.Data;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BoxUtil {

    public Map<String, List<String>> transBox(List<SecondBox> secondBoxes) {
        // 转换为二级下拉菜单
        Map<String, List<String>> result = new HashMap<>();
        for (SecondBox secondBox : secondBoxes) {
            String psu = secondBox.getFirstParam();
            if (result.containsKey(psu)) {
                result.get(psu).add(secondBox.getSecondParam());
            } else {
                List<String> pss = new ArrayList<>();
                pss.add(secondBox.getSecondParam());
                result.put(psu, pss);
            }
        }
        return result;
    }

}


@Data
class SecondBox {//二级下拉框,可调用common中dealBox进行转换
    // 一级菜单
    private String firstParam;
    // 二级菜单
    private String secondParam;


}
