---
title: "스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술"
tags: Java Spring
---

## 0. 강의 소개

간단한 웹 애플리케이션 개발
- 스프링 프로젝트 생성
- 스프링 부트로 웹 서버 실행
- 회원 도메인 개발
- 웹 MVC 개발
- DB 연동 - JDBC, JPA, 스프링 데이터 JPA
- 테스트 케이스 작성

## 1. 프로젝트 환경 설정

### 프로젝트 생성

- Java 11 설치
- Eclipse 설치
    - 라이선스......
- 스프링 부트 스타터 사이트로 이동해서 프로젝트 생성
    - <https://start.spring.io>
    - Project: Gradle Project
    - Language: Java
    - Spring Boot: 2.3.x
    - Dependencies: Spring Web, Thymeleaf
- src/main/java/HelloSpringApplication.java 실행
    - 톰캣이 실행되며 localhost:8080 이 접속되면 성공

### 라이브러리 살펴보기

- Gradle이나 Maven 툴은 의존 관계를 관리
- 스프링 부트 라이브러리
    - spring-boot-starter-web
        - spring-boot-starter-tomcat: 톰캣 (웹서버)
        - spring-webmvc: 스프링 웹 MVC
    - spring-boot-starter-thymeleaf: 타임리프 템플릿 엔진(View)
    - spring-boot-starter(공통): 스프링 부트 + 스프링 코어 + 로깅
        - spring-boot
            - spring-core
        - spring-boot-starter-logging
            - logback, slf4j
- 테스트 라이브러리
    - spring-boot-starter-test
        - junit: 테스트 프레임워크
        - mockito: 목 라이브러리
        - assertj: 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리
        - spring-test: 스프링 통합 테스트 지원

### View 환경 설정

- src/main/resource/static에 index.html 생성 (정적 페이지)
    - 작성 후 서버 재부팅하면 생성한 페이지 출력
- 템플릿 엔진!! 동적 페이지 - 강의는 Thymeleaf 사용
    - <https://www.thymeleaf.org>

- 스프링은 내용이 방대하므로 모든 내용을 다 알 수 없음
    - 검색의 생활화: <https://spring.io>
    - Welcome Page 검색: 첫 페이지를 어떻게 출력하는가

- 스프링 공식 튜토리얼: <https://spring.io/guides/gs/serving-web-content/>
- 스프링부트 메뉴얼: <https://docs.spring.io/spring-boot/docs/2.3.8.RELEASE/reference/html/spring-boot-features.html#boot-features-spring-mvc-template-engines>

- resources/templates/hello.html 생성
- com.hello.hellospring 하위에 컨트롤러 패키지 생성 후 컨트롤러 파일 생성

```java
@Controller
public class HelloController {
    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data", "hello!!");
        return "hello";
    }
}
```

![SPRING#0001](/assets/images/spring/0001_thymeleaf.png)
- 간단한 구조 설명
    - 컨트롤러에서 리턴 값으로 문자를 반환하면 뷰 리졸버(viewResolver)가 화면을 찾아서 처리
        - 스프링 부트 템플릿엔진 기본 viewName 매핑
        - resources:templates/ +{ViewName}+ .html

- spring-boot-devtools 라이브러리를 추가하면, html 파일을 컴파일만 해주면 서버 재시작 없이 View 파일 변경 가능

### 빌드하고 실행하기

- 윈도우 사용자
```bash
gradlew build / gradlew clean build
java -jar  build/libs/hello-spring-0.0.1-SNAPSHOT.jar
```

## 2. 스프링 웹 개발 기초

### 정적 컨텐츠

- 스프링 부트 정적 컨텐츠 기능
    - Reference에서 Static 검색
    - `src/main/resource/static` 에 생성
![SPRING#0002](0002_hello-static.png)
- 간단한 구조 설명
    - 내장 톰캣 서버가 스프링 컨테이너 탐색
    - hello-static 관련 컨트롤러가 없으면 resources: static/hello-static.html 탐색
    - hello-static.html 웹 출력