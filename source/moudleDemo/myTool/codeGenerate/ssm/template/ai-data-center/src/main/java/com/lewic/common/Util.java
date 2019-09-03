package com.lewic.common;

import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;

import java.util.List;

/**
 * @author lewic
 * @since 2019/6/21 20:33
 **/

public class Util {
    /**
     * 检查参数中的错误信息
     * @param bindingResult 校验注解检测出来的错误
     * @return 携带错误信息的msg
     */
    public static Message checkParam(BindingResult bindingResult) {
        Message msg = new Message();
        List<FieldError> oe = bindingResult.getFieldErrors();
        for (int i = 0; i < oe.size(); i++) {
            msg.setMessage(oe.get(i).getDefaultMessage());
        }
        return msg;
    }
}
