package com.lewic.mapper;

import com.lewic.entity.Student;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;


/**
 * @author lewic
 * @since 2019/6/13 15:22
 **/

@Mapper
public interface Teacher2StudentMapper {

    void removeAllStudent(@Param("tid") Integer tid);

    void addStudent(@Param("tid") Integer tid, @Param("students") List<Student> students);

    void addOneStudent(@Param("tid") Integer tid, @Param("sid") Integer sid);

}
