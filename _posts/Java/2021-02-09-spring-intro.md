---
title: "스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술"
tags: Java Spring Inflearn
---

<https://www.inflearn.com/course/스프링-입문-스프링부트>

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

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Hello</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
    <p th:text="'안녕하세요. ' + ${data}" >안녕하세요. 손님</p>
</body>
</html>
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

![SPRING#0002](/assets/images/spring/0002_hello-static.png)
- 간단한 구조 설명
    - 내장 톰캣 서버가 스프링 컨테이너 탐색
    - hello-static 관련 컨트롤러가 없으면 resources: static/hello-static.html 탐색
    - hello-static.html 웹 출력

### MVC와 템플릿 엔진

MVC: Model, View, Controller
- 과거에는 View와 Controller가 구분되지 않았음
- 현재는 View와 Controller를 구분하여 역할을 정확하게 나눔
    - View는 화면을 그리는데 집중
    - Controller는 비즈니스 로직, 내부적인 처리에 집중

```java
@Controller
public class HelloController {

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
         model.addAttribute("name", name);
    return "hello-template";
    }

}
```

```html
<html xmlns:th="http://www.thymeleaf.org">
<body>
    <p th:text="'hello ' + ${name}">hello! empty</p>
</body>
</html>
```

![SPRING#0003](/assets/images/spring/0003_hello-mvc.png)
- 간단한 구조 설명

### API

- 정적 컨텐츠 방식을 제외하면 두 가지 방식이 있음
    - HTML
    - API

```java
@Controller
public class HelloController {
	
	@GetMapping("hello-string")
	@ResponseBody	// HTTP의 Body 부분에 내용을 직접 넣어줌
	public String helloString(@RequestParam("name") String name) {
		return "hello " + name;	// "hello spring"
	}
	
	@GetMapping("hello-api")
	@ResponseBody	// JSON 반환 방식이 기본
	public Hello helloAPI(@RequestParam("name") String name) {
		Hello hello = new Hello();
		hello.setName(name);
		return hello;
	}
	
	static class Hello {
		private String name;
		
		public String getName() {
			return name;
		}
		
		public void setName(String name) {
			this.name = name;
		}
	}
    
}
```
- `@ResponseBody`를 사용하고 객체를 반환하면 객체가 JSON(기본)으로 변환

![SPRING#0004](/assets/images/spring/0004_hello-api.png)
- `@ResponseBody`를 사용
    - HTTP의 BODY에 문자 내용을 직접 반환
    - `viewResolver`대신에 `HttpMessageConverter`가 동작
        - 기본 문자처리: `StringHttpMessageConverter`
        - 기본 객체처리: `MappingJackson2HttpMessageConverter`
            - 객체를 JSON으로 바꿔주는 유명한 라이브러리: Jackson, GSON
    - byte 처리 등 기타 여러 `HttpMessageConverter`가 기본으로 등록되어 있음

## 3. 회원 관리 예제 - 백엔드 개발

### 비즈니스 요구사항 정리

단순한 예제 시나리오
- 데이터: 회원 ID, 이름
- 기능: 회원 등록, 조회
- 아직 데이터 저장소가 선정되지 않음

![SPRING#0005](/assets/images/spring/0005_hierarchy.png)
- 일반적인 웹 애플리케이션 계층 구조
    - 도메인: 회원, 주문, 쿠폰 등 주로 데이터베이스에 저장되는 비즈니스 도메인 객체
    - 서비스: 핵심 비즈니스 로직을 구현한 계층
    - 컨트롤러, 리포지토리, DB, ...

![SPRING#0006](/assets/images/spring/0006_class-dependency.png)
- 클래스 의존 관계
    - 회원 정보는 인터페이스로 구현
    - 간단히 메모리 기반 구현체로 만들고 추후 구체적인 기술이 정의되면 DB에 연동

### 회원 도메인과 리포지토리 만들기

```java
public interface MemberRepository {
	
	Member save(Member member);
	Optional<Member> findById(Long id);
	Optional<Member> findByName(String name);
	List<Member> findAll();
	
}
```

```java
public class MemoryMemberRepository implements MemberRepository{
	
	// 실무에서는 동시성 문제가 있을 수 있기 때문에 ConcurrentHashMap, AtomicLong 등 사용...
	private static Map<Long, Member> store = new HashMap<>();
	private static long sequence = 0L;
	
	@Override
	public Member save(Member member) {
		member.setID(++sequence);;
		store.put(member.getId(), member);
		return member;
	}
	
	@Override
	public Optional<Member> findById(Long id) {
		// Null이 출력되어도 Optional로 감싸서 반환
		return Optional.ofNullable(store.get(id));
	}
	
	@Override
	public Optional<Member> findByName(String name) {
		return store.values().stream()
					.filter(member -> member.getName().equals(name))
					.findAny();
	}
	
	@Override
	public List<Member> findAll() {
		return new ArrayList<>(store.values());
	}
	
}
```

### 회원 리포지토리 테스트 케이스 작성

- 개발한 기능을 실행해서 테스트 할 때, 자바는 JUnit이라는 프레임워크로 테스트를 실행

```java
public interface MemberRepository {
	
	Member save(Member member);
	Optional<Member> findById(Long id);
	Optional<Member> findByName(String name);
	List<Member> findAll();
	
}
```

```java
public class MemoryMemberRepository implements MemberRepository{
	
	// 실무에서는 동시성 문제가 있을 수 있기 때문에 ConcurrentHashMap, AtomicLong 등 사용...
	private static Map<Long, Member> store = new HashMap<>();
	private static long sequence = 0L;
	
	@Override
	public Member save(Member member) {
		member.setID(++sequence);;
		store.put(member.getId(), member);
		return member;
	}
	
	@Override
	public Optional<Member> findById(Long id) {
		// Null이 출력되어도 Optional로 감싸서 반환
		return Optional.ofNullable(store.get(id));
	}
	
	@Override
	public Optional<Member> findByName(String name) {
		return store.values().stream()
					.filter(member -> member.getName().equals(name))
					.findAny();
	}
	
	@Override
	public List<Member> findAll() {
		return new ArrayList<>(store.values());
	}
	
	public void clearStore() {
		store.clear();
	}
	
}
```

```java
public class MemoryMemberRepositoryTest {
	MemoryMemberRepository repository = new MemoryMemberRepository();
	
	// 매 테스트가 끝날 때마다 실행
	@AfterEach
	public void afterEach() {
		repository.clearStore();
	}
	
	@Test
	public void save() {
		Member member = new Member();
		member.setName("Spring");
		
		repository.save(member);
		
		Member result = repository.findById(member.getId()).get();
		// System.out.println("result = " + (result == member));
		// Assertions.assertEquals(member, result);
		assertThat(member).isEqualTo(result);
	}
	
	@Test
	public void findByName() {
		Member member1 = new Member();
		member1.setName("spring1");
		repository.save(member1);
		
		Member member2 = new Member();
		member2.setName("spring2");
		repository.save(member2);
		
		Member result = repository.findByName("spring1").get();
		
		assertThat(result).isEqualTo(member1);
	}
	
	@Test
	public void findAll() {
		Member member1 = new Member();
		member1.setName("spring1");
		repository.save(member1);
		
		Member member2 = new Member();
		member2.setName("sprint2");
		repository.save(member2);
		
		List<Member> result = repository.findAll();
		
		assertThat(result.size()).isEqualTo(2);
	}
	
}
```
- `@AfterEach`는 각 테스트가 종료될 때마다 실행되는 기능
- 모든 테스트는 독립적으로 실행되어야 함

### 회원 서비스 개발

### 회원 서비스 테스트