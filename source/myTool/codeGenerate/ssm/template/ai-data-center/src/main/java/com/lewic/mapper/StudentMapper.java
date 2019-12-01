package com.lewic.mapper;

import com.lewic.common.Page;
import com.lewic.entity.Student;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;


/**
 * @author lewic
 * @apiNote StudentMapper
 * @since 2019/6/14 19:49
 **/

@Mapper
public interface StudentMapper {
    List<Student> listStudent(@Param("page") Page page);

    Student getStudent(@Param("sid") Integer sid);

    Integer getStudentCount();

    void insertStudent(Student student);

    void updateStudent(Student student);

    void deleteStudent(@Param("sid") String sid);
}
