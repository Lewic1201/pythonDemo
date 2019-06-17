package com.sc.hoperun.common;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

@Configuration
public class Swagger2 {


    @Bean
    public Docket createRestApi() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.sc.hoperun"))
                .paths(PathSelectors.any())
                .build();
    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("ai智能平台数据中心")
                .description("ai智能平台数据中心RESTful")
                .termsOfServiceUrl("http://blog.csdn.net/saytime")
                .version("1.0")
                .build();


//        return new ApiInfo(appName, appDesc, appVersion, termsOfServiceUrl,
//                new Contact(contactName, contactUrl, contactEmail),
//                license, licenseUrl);
    }
}
