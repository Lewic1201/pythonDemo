package com.lewic.mapper;

import com.lewic.common.Page;
import com.lewic.entity.Teacher;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;


/**
 * @author lewic
 * @since 2019/6/13 15:22
 **/

@Mapper
public interface TeacherMapper {
    List<Teacher> listTeacher(@Param("name") String name,
                              @Param("page") Page page);

    Teacher getTeacher(@Param("infoId") String infoId);

    Integer getTeacherCount();

    Integer getTeacherFilterCount(@Param("name") String name);

    void insertTeacher(Teacher information);

    void updateTeacher(Teacher information);

    void deleteTeacher(@Param("infoIds") String[] infoIds);
}
