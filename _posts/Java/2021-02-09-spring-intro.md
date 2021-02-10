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
- 모든 테스트는 독립적으로 실행되어야 함

### 회원 서비스 개발

```java
public class MemberService {
	private final MemberRepository memberRepository = new MemoryMemberRepository();
	
	/**
	 * 회원가입
	 * @param member
	 * @return
	 */
	public Long join(Member member) {
		/**
		 * // 같은 이름이 있는 중복 회원은 불가
		 * Optional<Member> result = memberRepository.findByName(member.getName());
		 * result.ifPresent(m -> {
		 *     throw new IllegalStateException("이미 존재하는 회원입니다.");
		 * });
		*/
		
		/**
         * // Extract Method -> validateDuplicateMember 생성
		 * memberRepository.findByName(member.getName())
		 * 	.ifPresent(m -> {
		 * 		throw new IllegalStateException("이미 존재하는 회원입니다.");
		 * 	});
		 */
		
		validateDuplicateMember(member); // 중복 회원 검증
		
		memberRepository.save(member);
		
		return member.getId();
	}

	private void validateDuplicateMember(Member member) {
		memberRepository.findByName(member.getName())
			.ifPresent(m -> {
				throw new IllegalStateException("이미 존재하는 회원입니다.");
			});
	}
	
	/**
	 * 전체 회원 조회
	 * @return
	 */
	public List<Member> findMembers() {
		return memberRepository.findAll();
	}
	
	public Optional<Member> findOne(Long memberId) {
		return memberRepository.findById(memberId);
	}
}
```
- Extract Method: 그룹으로 함께 묶을 코드 블럭이 있으면 Method로 생성

### 회원 서비스 테스트

```java
public class MemberService {
	// 오직 한 번만 사용할 수 있는 entity에 final 사용 -> 상속 불가, 초기화 단 한 번
	private final MemberRepository memberRepository;
	
    // 회원 서비스 코드를 DI(의존성 주입)가 가능하게 변경
	public MemberService(MemberRepository memberRepository) {
		this.memberRepository = memberRepository;
	}
    ...
}
```

```java
class MemberServiceTest {
	MemberService memberService;
	MemoryMemberRepository memberRepository;
	
    // 각 테스트 이전에 실행되는 코드
	@BeforeEach
	public void beforeEach() {
		memberRepository = new MemoryMemberRepository();
		memberService = new MemberService(memberRepository);
	}

	@AfterEach
	public void afterEach() {
		memberRepository.clearStore();
	}

	@Test
	// 빌드될 때 포함되지 않으므로 한글로 만들기도 함
	void 회원가입() {
		// Given
		Member member = new Member();
		member.setName("spring");
		
		// When
		Long saveId = memberService.join(member);
		
		// Then
		Member findMember = memberService.findOne(saveId).get();
		assertThat(member.getName()).isEqualTo(findMember.getName());
	}
	
	@Test
	public void 중복_회원_예약() {
		// Given
		Member member1 = new Member();
		member1.setName("spring");
		
		Member member2 = new Member();
		member2.setName("spring");
		
		// When

		memberService.join(member1);
		IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));
		
		assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
/*
		try {
			memberService.join(member2);
			fail();
		} catch (IllegalStateException e) {
			Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
		}
*/
		
		// Then
	}
}
```

## 4. 스프링 빈과 의존관계

### 컴포넌트 스캔과 자동 의존관계 설정

멤버 컨트롤러가 멤버 서비스를 통해서 회원가입하고 조회 

![SPRING#0003](/assets/images/spring/0003_hello-mvc.png)
- `@Controller` Notation을 기입하면 스프링 컨테이너에 해당 컨트롤러에 대한 스프링 빈이 생성됨

```java
@Controller
public class MemberController {
//	private final MemberService memberService = new MemberService();
	private final MemberService memberService;
	
	@Autowired
	public MemberController(MemberService memberService) {
		this.memberService = memberService;
	}
}
```
- `@Autowired`가 있으면 스프링이 연관된 객체들을 스프링 컨테이너에 찾아서 넣음

스프링 빈을 등록하는 2가지 방법
- 컴포넌트 스캔과 자동 의존 관계 설정
- 자바 코드로 직접 스프링 빈 등록하기

컴포넌트 스캔과 자동 의존 관계 설정
- `@Component` 애노테이션이 있으면 스프링 빈으로 자동 등록
- 컴포넌트 스캔 덕분에 자동으로 등록
    - `@Component` 를 포함하는 다음 애노테이션도 스프링 빈으로 자동 등록된다.
    - `@Controller`, `@Service`, `@Repository`

![SPRING#0007](/assets/images/spring/0007_spring-bean.png)
- 컴포넌트 스캔을 활용한 스프링 빈 등록
- 스프링 컨테이너에 스프링 빈을 등록할 때, 기본으로 싱글톤으로 등록(유일하게 하나만 등록해서 공유)
    - 같은 스프링 빈이면 모두 같은 인스턴스
    - 싱글톤이 아니게 설정할 수 있지만, 특별한 경우를 제외하면 대부분 싱글톤 사용

### 자바 코드로 직접 스프링 빈 등록하기

```java
@Configuration
public class SpringConfig {
	@Bean
	public MemberService memberService() {
		return new MemberService(memberRepository());
	}
	
	@Bean
	public MemberRepository memberRepository() {
		return new MemoryMemberRepository();
	}
}
```
- 우리는 향후 메모리 리포지토리를 다른 리포지토리로 변경할 예정이므로, 컴포넌트 스캔 방식 대신에 자바 코드로 스프링 빈을 설정
- DI에는 필드 주입, setter 주입, 생성자 주입 이렇게 3가지 방법이 있음
    - 의존관계가 실행중에 동적으로 변하는 경우는 거의 없으므로 생성자 주입을 권장
- 실무에서는 주로 정형화된 컨트롤러, 서비스, 리포지토리 같은 코드는 컴포넌트 스캔을 사용
- 정형화 되지 않거나, 상황에 따라 구현 클래스를 변경해야 하면 설정을 통해 스프링 빈으로 등록
- `@Autowired`를 통한 DI는 `helloConroller`, `memberService` 등과 같이 스프링이 관리하는 객체에서만 동작
    - 스프링 빈으로 등록하지 않고 내가 직접 생성한 객체(예: `new MemberService();`)에서는 동작하지 않음

## 5. 회원 관리 예제 - 웹 MVC 개발

### 회원 웹 기능 - 홈 화면 추가

```java
@Controller
public class HomeController {
    @GetMapping("/")
    public String home() {
        return "home";
    }
}
```

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>
    <div class="container">
        <div>
        <h1>Hello Spring</h1>
        <p>회원기능</p>
        <p>
            <a href="/members/new">회원가입</a>
            <a href="/members">회원목록</a>
        </p>
        </div>
    </div>  <!-- /container -->
</body>
</html>
```
- 컨트롤러가 정적 파일보다 우선되므로 `home.html`이 출력됨

### 화면 웹 기능 - 등록

```java
@Controller
public class MemberController {
    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new")
    public String createForm() {
        return "members/createMemberForm";
    }

    @PostMapping("/members/new")
    public String create(MemberForm form) {
        Member member = new Member();
        member.setName(form.getName());

        memberService.join(member);

        return "redirect:/";
    }
}
```

```java
public class MemberForm {
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    private String name;
}
```

```html
<!DOCTYPE HTML><html xmlns:th="http://www.thymeleaf.org">
<body>

<div class="container">
    <form action="/members/new"method="post">
        <div class="form-group">
            <label for="name">이름</label>
            <input type="text"id="name" name="name"placeholder="이름을입력하세요">
        </div>
        <button type="submit">등록</button>
    </form>
</div><!-- /container -->

</body>
</html>
```
- `form` 태그 내에서 post 방식으로 `/members/new`에 데이터 전송
    - `input` 태그에 입력받은 정보를 전송.
    - `name="name"`: 전송되는 값의 key 값
- URL이 같아도 `@GetMapping`, `@PostMapping`을 통해 다르게 사용 가능

### 회원 웹 기능 - 조회

```java
@Controller
public class MemberController {
    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new")
    public String createForm() {
        return "members/createMemberForm";
    }

    @PostMapping("/members/new")
    public String create(MemberForm form) {
        Member member = new Member();
        member.setName(form.getName());

        memberService.join(member);

        return "redirect:/";
    }

    @GetMapping("/members")
    public String list(Model model) {
        List<Member> members = memberService.findMembers();
        model.addAttribute("members", members);
        return "members/memberList";
    }
}
```

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>

<div class="container">
    <div>
        <table>
            <thead>
            <tr>
                <th>#</th>
                <th>이름</th>
            </tr>
            </thead>
            <tbody>
            <tr th:each="member : ${members}">
                <td th:text="${member.id}"></td>
                <td th:text="${member.name}"></td>
            </tr>
            </tbody>
        </table>
    </div>
</div><!-- /container -->

</body>
</html>
```
- `model`에 저장된 `members`를 읽어서 출력
    - `th:each`(thymeleaf 문법)를 사용해 `members` 리스트를 반복해서 읽고 출력
- 현재는 메모리에 저장했기 때문에 서버를 내리면 데이터가 모두 지워짐

## 6. 스프링 DB 접근 기술

### H2 데이터베이스 설치

- 다운로드 및 설치
- DB 파일 생성
    - 최초 한 번: JDBC URL `jdbc:h2:~/test`
        - `~/test.mv.db` 파일 생성 확인
	- 이후: JDBC URL `jdbc:h2:tcp://localhost/~/test`로 접속

```sql
drop table if exists member CASCADE;
create table member
(
/**
 * Java: Long == bigint
 * generated by default as identity: Null 값이 들어오면 고유값으로 채워줌
 */
    id bigint generated by default as identity, 
    name varchar(255),
    primary key (id)
);
```
- 테이블 관리를 위해 프로젝트 루트에 `sql/ddl.sql` 파일을 생성
- H2 데이터베이스에 접근해서 `member` 테이블 생성
- 프로젝트에 ddl.sql 파일 만들어서 로그 관리해주면 좋음

### 순수 JDBC

```java
public class JdbcMemberRepository implements MemberRepository {
	private final DataSource dataSource;
	
	public JdbcMemberRepository(DataSource dataSource) {
		this.dataSource = dataSource;
	}
	
	@Override
	public Member save(Member member) {
		String sql = "insert into member(name) values(?)";
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			conn = getConnection();
			pstmt = conn.prepareStatement(sql,
					Statement.RETURN_GENERATED_KEYS);
			pstmt.setString(1, member.getName());
			pstmt.executeUpdate();
			rs = pstmt.getGeneratedKeys();
			
			if (rs.next()) {
				member.setId(rs.getLong(1));
			} else {
				throw new SQLException("id 조회 실패");
			}
			
			return member;
			
		} catch (Exception e) {
			throw new IllegalStateException(e);
		} finally {
			close(conn, pstmt, rs);
		}
	}
	
	@Override
	public Optional<Member> findById(Long id) {
		String sql = "select * from member where id = ?";
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			conn = getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setLong(1, id);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				Member member = new Member();
				member.setId(rs.getLong("id"));
				member.setName(rs.getString("name"));
				
				return Optional.of(member);
				
			} else {
				return Optional.empty();
			}
		} catch (Exception e) {
			throw new IllegalStateException(e);
		} finally {
			// 사용이 끝나면 꼭 close
			close(conn, pstmt, rs);
		}
	}
	
	@Override
	public List<Member> findAll() {
		String sql = "select * from member";
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			conn = getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			List<Member> members = new ArrayList<>();
			
			while(rs.next()) {
				Member member = new Member();
				member.setId(rs.getLong("id"));
				member.setName(rs.getString("name"));
				members.add(member);
			}
			return members;
		
		} catch (Exception e) {
			throw new IllegalStateException(e);
		} finally {
			close(conn, pstmt, rs);
		}
	}
	
	@Override
	public Optional<Member> findByName(String name) {
		String sql = "select * from member where name = ?";
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			conn = getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, name);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				Member member = new Member();
				member.setId(rs.getLong("id"));
				member.setName(rs.getString("name"));
				
				return Optional.of(member);
				
			}
			
			return Optional.empty();
			
		} catch (Exception e) {
			throw new IllegalStateException(e);
		} finally {
			close(conn, pstmt, rs);
		}
	}
	
	private Connection getConnection() {
		return DataSourceUtils.getConnection(dataSource);
	}
	
	private void close(Connection conn, PreparedStatement pstmt, ResultSet rs) {
		try {
			if (rs != null) {
				rs.close();
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		try {
			if (pstmt != null) {
				pstmt.close();
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		try {
			if (conn != null) {
				close(conn);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
	private void close(Connection conn) throws SQLException {
		DataSourceUtils.releaseConnection(conn, dataSource);
	}
}
```
- 옛날에 했던 방법...
- 필요하면 나중에 찾아서 공부할 것

```java
@Configuration
public class SpringConfig {
	
	private DataSource dataSource;
	
	@Autowired
	public SpringConfig(DataSource dataSource) {
		this.dataSource = dataSource;
	}
	
    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        // return new MemoryMemberRepository();
    	return new JdbcMemberRepository(dataSource);
    }
}
```
- `JdbcMemberRepository`를 사용하도록 `SpringConfig` 수정
    - `interface`를 사용해 구현했기 때문에 간단히 교체 가능

### 스프링 통합 테스트

### 스프링 JdbcTemplate

### JPA

### 스프링 데이터 JPA

## 7. AOP

### AOP가 필요한 상황

### AOP 적용

## 8. 다음으로