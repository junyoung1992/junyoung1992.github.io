---
title: "스프링 핵심 원리 - 기본편"
tags: Java Spring Backend Inflearn
---

<https://www.inflearn.com/course/스프링-핵심-원리-기본편>

## 0. 강의 소개

스프링 핵심 원리
- IoC, DI, 컨테이너, SOLID, SRP, OCP, DIP

스프링의 핵심 가치
- 객체 지향 프로그래밍

## 1. 객체 지향 설계와 스프링

### 스프링이란?

스프링 구성 요소
- 필수: 스프링 프레임워크, 스프링 부트
- 선택: 스프링 데이터, 스프링 세션, 스프링 시큐리티, 스프링 Rest Docs, 스프링 배치, 스프링 클라우드

스프링 프레임워크
- 핵심 기술: 스프링 DI 컨테이너, AOP, 이벤트, 기타
- 웹 기술: 스프링 MVC, 스프링 WebFlux
- 데이터 접근 기술: 트랜잭션, JDBC, ORM 지원, XML 지원
- 기술 통합: 캐시, 이메일, 원격 접근, 스케줄링
- 테스트: 스프링 기반 테스트 지원
- 언어: 코틀린, 그루비
- 최근에는 스프링 부트를 통해 스프링 프레임워크의 기술을 편리하게 사용

스프링 부트
- 스프링을 편리하게 사용할 수 있도록 지원
    - 최근에는 기본으로 사용
- 단독으로 실행할 수 있는 스프링 애플리케이션을 쉽게 생성
- Tomcat 같은 웹 서버를 내장해서 별도의 웹서버를 설치하지 않아도 됨
- 손쉬운 빌드 구성을 위한 starter 종속성 제공
- 스프링과 3rd parthy 라이브러리 자동 구성
- 메트링, 상태 확인, 외부 구성 같은 프로덕션 준비 기능 제공
- 관례에 의한 간결한 설정

스프링을 왜 만들었는가?
- 핵심 개념
    - 이 기술을 왜 만들었는가?
    - 이 기술의 핵심 컨셉은?
- 스프링의 핵심
    - 스프링은 자바 언어 기반의 프레임워크
    - 자바 언어의 가장 큰 특징: **객체 지향 언어**
    - 스프링은 객체 지향 언어가 가진 강력한 특징을 살려내는 프레임워크
    - 스프링은 **좋은 객체 지향** 애플리케이션을 개발할 수 있게 도와주는 프레임워크

### 좋은 객체 지향 프로그래밍이란?

객체 지향의 특징<br />
*추상화, 캡슐화, 상속, 다형성*
- 객체 지향 프로그래밍은 컴퓨터 프로그램을 명려어의 목록으로 보는 사각에서 벗어나 여러 개의 독립된 단위, 즉 객체들의 모임으로 파악하고자 하는 것
    - 각각의 객체는 메시지를 주고 받고, 데이터를 처리할 수 있음
- 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 떄문에 대규모 소프트웨어 개발에서 많이 사용

유연하고 변경이 용이하다?
- 레고 블럭을 조립하듯, 컴포넌트를 쉽고 유연하게 변경하면서 개발할 수 있는 방법 → 다형성(Polymorphism)
- 다형성: 역할과 구현으로 프로그래밍을 구분

역할과 구현을 분리
- 역할과 구현으로 구분하면 단순해지고, 유연해지며 수정도 편리해짐
- 장점
    - 클라이언트는 대상의 역할(인터페이스)만 알면 됨
    - 클라이언트는 구현 대상의 내부 구조를 몰라도 됨
    - 클라이언트는 구현 대상의 내부 구조가 변경되어도 영향을 받지 않음
    - 클라이언트는 구현 대상 자체를 변경해도 영향을 받지 않음
- 자바 언어
    - 자바 언어의 다형성을 활용
        - 역할: 인터페이스
        - 구현: 인터페이스를 구현한 클래스, 구현 객체
    - 객체를 설계할 때 역할과 구현을 명확히 분리
    - 객체 설계시 역할(인터페이스)를 먼저 부여하고, 그 역할을 수행하는 구현 객체를 만듬

객체의 협력이라는 관계부터 생각
- 혼자 있는 객체는 없음
- 클라이언트: 요청 → 서버: 응답
- 수많은 객체 클라이언트와 객체 서버는 서로 협력 관계를 가짐

자바 언어의 다형성
- 오버라이딩
    - 오버라이딩은 자바 기본 문법
    - 오버라이딩 된 매서드가 실행
    - 다형성으로 인터페이스를 구현한 객체를 실행 시점에 유연하게 변경할 수 있음
        - 물론 클래스 상속 관계도 다형성, 오버라이딩 적용 가능

![SPRING#0000](/assets/images/spring-core/0000-overriding.png)

다형성의 본질
- 인터페이스를 구현한 객체 인스턴스를 실행 시점에 유연하게 변경할 수 있음
- 다형성의 본질을 이해하려면 협력이라는 객체 사이의 관계에서 시작해야 함
- 클라이언트를 변경하지 않고, 서버의 구현 기능을 유연하게 변경할 수 있음

역할과 구현을 분리
- 정리
    - 실세계의 역할과 구현이라는 편리한 컨셉을 다형성을 통해 객체 세상으로 가져올 수 있음
    - 유연하고 변경이 용이
    - 확장 가능한 설계
    - 클라이언트에 영향을 주지 않는 변경 가능
    - 인터페이스를 안정적으로 잘 설계하는 것이 중요
- 한계
    - 역할(인터페이스) 자체가 변하면, 클라이언트, 서버 모두에 큰 변경이 발생
    - 인터페이스를 안정적으로 잘 설계하는 것이 중요

스프링과 객체 지향
- 다형성이 가장 중요
- 스프링은 다형성을 극대화해서 이용할 수 있게 보조
- 스프링에서 이야기하는 제어의 역전(IoC), 의존관계 주입(DI)은 다형성을 활용해서 역할과 구현을 편리하게 다룰 수 있도록 지원

### 좋은 객체 지향 설계의 5가지 원칙 (SOLID)

SOLID<br />
*클린코드로 유명한 로버트 마틴이 좋은 객체 지향 설계의 5가지 원칙을 정리*
- **S**RP, Single Responsibility Principle: 단일 책임 원칙
- **O**CP, Open/Closed Principle: 개방-폐쇄 원칙
- **L**SP, Liskov Substitution Principle: 리스코프 치환 원칙
- **I**SP, Interface Segregation Principle: 인터페이스 분리 원칙
- **D**IP, Dependency Inversion Principle: 의존관계 역전 원칙

SRP 단일 책임 원칙<br />
Single Responsibility Principle
- 한 클래스는 하나의 책임만 가져야 한다.
- 하나의 책임이라는 것은 모호함
    - 클 수도 있고 작을 수도 있음
    - 문맥과 상황에 따라 다름
- 중요한 기준은 변경
    - 변경이 있을 때 파급 효과가 적으면 단일 책임 원칙을 잘 따른 것
- 예) UI 변경, 객체의 생성과 사용을 분리

OCP 개방-폐쇄 원칙<br />
Open/Clodes Principle
- 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀있어야 함
    - 다형성을 활용
- 인터페이스를 구현한 새로운 클래스를 하나 만들어서 새로운 기능을 구현
- **문제점**
    - 구현 객체를 변경하려면 클라이언트 코드를 변경해야 함
    - 분명 다형성을 사용했지만 OCP 원칙을 지킬 수 없음
- **해결책**
    - 객체를 생성하고 연관 관계를 맺어주는 별도의 조립, 설정자가 필요 → Spring 배우면서!!

LSP 리스코프 치환 원칙<br />
Liskov Substitution Principle
- 프로그램의 객체는 프로그램의 정확성을 깨뜨리지 안흥면서 하위 타입의 인스턴스로 바꿀 수 있어야 함
- 다형성에서 하위 클래스는 인터페이스 규약을 다 지켜야 함
    - 다형성을 지원하기 위한 원칙
    - 인터페이스를 구현한 구현체를 믿고 사용하여면 이 원칙이 필요
    - 단순히 컴파일 성공을 넘어서는 개념

ISP 인터페이스 분리 원칙<br />
Interface Segregation Principle
- 특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 낫다
    - 인터페이스가 명확해지고 대체 가능성이 높아짐

DIP 의존관계 역전 원칙<br />
Dependency Inversion Principle
- 프로그래머는 "추상화에 의존해야지, 구체화에 의존하면 안된다."
    - 의존성 주입은 이 원칙을 따르는 방법 중 하나
    - 구현 클래스에 의존하지 말고, 인터페이스에 의존하라는 뜻

정리
- 객체 지향의 핵심은 다형성
- 그러나 다형성만으로는 쉽게 부품을 교체하듯 개발할 수 없음
    - 다형성만으로는 구현 객체를 변경할 대 클라이언트 코드도 함께 변경됨
    - 다형성만으로는 OCP, DIP를 지킬 수 없음
- 무언가 더 필요함

### 객체 지향 설계와 스프링

스프링과 객체 지향
- 스프링은 다음 기술을 통해 다형성과 OCP, DIP를 모두 지원
    - DI(Dependency Injection): 의존 관계, 의존성 주입
    - DI 컨테이너 제공
- 클라이언트 코드의 변경 없이 기능 확장
- 순수하게 자바로 OCP, DIP 원칙들을 지키면서 개발을 해보면, 결국 스프링 프레임워크를 만들게 됨
    - 정확하게는 DI 컨테이너

정리
- 모든 설계에 역할과 구현을 분리
- 이상적으로는 모든 설계에 인터페이스를 부여하는 것

실무적 고민
- 인터페이스를 도입하면 추상화라는 비용이 발생
- 기능을 확장할 가능성이 없다면 구체 클래스를 직접 사용
    - 향후 꼭 필요할 때 리팩터링해서 인터페이스를 도입

## 2. 스프링 핵심 원리 이해 1 - 예제 만들기

### 프로젝트 생성

스프링 부트를 사용하여 프로젝트 생성<br />
<https://start.spring.io>

![SPRING#0001](/assets/images/spring-core/0001-project-setting.png)

### 비즈니스 요구사항과 설계

회원 요구사항
- 회원 가입과 조회가 가능
- 회원의 등급은 일반과 VIP가 존재
- 회원 데이터는 자체 DB를 구축할 수 있고, 외부 시스템과 연동할 수 있음(미확정)

주문과 할인 정책
- 회원은 상품을 주문할 수 있음
- 회원 등급에 따라 할인 정책을 적용할 수 있음
    - 모든 VIP는 1,000원 할인(추후 변경 가능)
- 할인 정책은 변경 가능성이 높음
    - 회사의 기본 할인 정책은 정해지지 않음

### 회원 도메인 설계

회원 도메인 요구사항
- 회원 가입 및 조회
- 회원은 일반과 VIP 두 가지 등급이 있음
- 회원 데이터는 자체 DB를 구축할 수 있고, 외부 시스템과 연동할 수 있음

**회원 도메인 협력 관계**
![SPRING#0002](/assets/images/spring-core/0002-member-domain.png)

**회원 클래스 다이어그램**
![SPRING#0003](/assets/images/spring-core/0003-member-class.png)

**회원 객체 다이어그램**
![SPRING#0004](/assets/images/spring-core/0004-member-object.png)
- 회원 서비스: **MemberServicempl**

### 회원 도메인 개발

회원 엔티티
- 회원 등급
    ```java
    public enum Grade {
        BASIC,
        VIP
    }
    ```
- 회원 엔티티
    ```java
    public class Member {
        private Long id;
        private String name;
        private Grade grade;
    
        public Member(Long id, String name, Grade grade) {
            this.id = id;
            this.name = name;
            this.grade = grade;
        }
    
        public Long getId() {
            return id;
        }
    
        public void setId(Long id) {
            this.id = id;
        }
    
        public String getName() {
            return name;
        }
    
        public void setName(String name) {
            this.name = name;
        }
    
        public Grade getGrade() {
            return grade;
        }
    
        public void setGrade(Grade grade) {
            this.grade = grade;
        }
    }
    ```

회원 저장소
- 회원 저장소 인터페이스
    ```java
    public interface MemberRepository {
        void save(Member member);
        Member findById(Long memberId);
    }
    ```
- 회원 저장소 구현체(메모리)
    ```java
    public class MemoryMemberRepository implements MemberRepository{
        private  static Map<Long, Member> store = new HashMap<>();
    
        @Override
        public void save(Member member) {
            store.put(member.getId(), member);
        }
    
        @Override
        public Member findById(Long memberId) {
            return store.get(memberId);
        }
    }
    ```
    - `HashMap`은 동시성 이슈가 발생할 수 있으므로, `ConcurrentHashMap`을 사용
        - 교육이므로 그냥 `HashMap` 사용

회원 서비스
- 회원 서비스 인터페이스
    ```java
    public interface MemberService {
        void join(Member member);
        Member findMember(Long memberId);
    }
    ```
- 회원 서비스 구현체
    ```java
    public class MemberServiceImpl implements MemberService{
        private final MemberRepository memberRepository = new MemoryMemberRepository();
    
        @Override
        public void join(Member member) {
            memberRepository.save(member);
        }
    
        @Override
        public Member findMember(Long memberId) {
            return memberRepository.findById(memberId);
        }
    }
    ```

### 회원 도메인 실행과 테스트

회원 도메인
- 회원 가입 실행
    ```java
    public class MemberApp {
        public static void main(String[] args) {
            MemberService memberService = new MemberServiceImpl();
            Member member = new Member(1L, "memberA", Grade.VIP);
            memberService.join(member);
    
            Member findMember = memberService.findMember(1L);
            System.out.println("new member = " + member.getName());
            System.out.println("find member = " + findMember.getName());
        }
    }
    ```
    - 애플리케이션 로직으로 테스트를 하는 것은 좋은 방법이 아님 → JUnit 테스트 활용
- 회원 가입 테스트
    ```java
    public class MemberServiceTest {
        MemberService memberService = new MemberServiceImpl();
    
        @Test
        void join() {
            // Given
            Member member = new Member(1L, "memberA", Grade.VIP);
    
            // When
            memberService.join(member);
            Member findMember = memberService.findMember(1L);
    
            // Then
            Assertions.assertThat(member).isEqualTo(findMember);
        }
    }
    ```
    - 테스트를 위해 `src\test`에 따로 분리된 디렉토리가 있음
    - 배포에는 포함되지 않는 코드

회원 도메인 설계의 문제점
- OCP, DIP 원칙을 잘 준수하고 있는가?
- 인터페이스 뿐만 아니라 구현까지 의존하는 형태로 의존관계가 구현됨

### 주문과 할인 도메인 설계

주문과 할인 정책
- 회원은 상품을 주문할 수 있음
- 회원 등급에 따라 할인 정책을 적용할 수 있음
- 모든 VIP는 1000원을 할인해주는 고정 금액 할인이 적용(추후 변경 가능)
- 할인 정책은 변경 가능성이 높음

**주문 도메인 협력, 역할 책임**<br />
![SPRING#0005](/assets/images/spring-core/0005-order-domain.png)
1. 주문 생성: 클라이언트는 주문 서비스에 주문 생성을 요청
1. 회원 조회: 할인을 위해 주문 서비스는 회원 저장소에서 회원을 조회
1. 할인 적용: 주문 서비스는 회원 등급에 따른 할인 여부를 할인 정책에 위임
1. 주문 결과 반환: 주문 서비스는 할인 결과를 포함한 주문 결과를 반환
    - DB에 저장하면 예제가 복잡해지므로 그냥 반환

**주문 도메인 전체**<br />
![SPRING#0006](/assets/images/spring-core/0006-order-domain-all.png)
- 역할과 구현을 분리해서 자유롭게 객체를 조힙할 수 있도록 설계

**주문 도메인 클래스 다이어그램**<br />
![SPRING#0007](/assets/images/spring-core/0007-order-class.png)

**주문 도메인 객체 다이어그램**<br />
![SPRING#0008](/assets/images/spring-core/0008-order-object-1.png)
![SPRING#0009](/assets/images/spring-core/0009-order-object-2.png)

### 주문과 할인 도메인 개발

할인 정책 인터페이스
```java
public interface DiscountPolicy {
    /**
     * @return 할인 대상 금액
     */
    int discount(Member member, int price);
}
```

정액 할인 정책 구현체
```java
public class FixDiscountPolicy implements DiscountPolicy{
    private int discountFixAmout = 1000;
    @Override
    public int discount(Member member, int price) {
        if (member.getGrade() == Grade.VIP) {
            return discountFixAmout;
        } else {
            return 0;
        }
    }
}
```

주문 엔티티
```java
public class Order {
    private Long memberId;
    private String itemName;
    private int itemPrice;
    private int discountPrice;

    public Order(Long memberId, String itemName, int itemPrice, int discountPrice) {
        this.memberId = memberId;
        this.itemName = itemName;
        this.itemPrice = itemPrice;
        this.discountPrice = discountPrice;
    }

    ... (getter and setter)

    @Override
    public String toString() {
        return "Order{" +
                "memberId=" + memberId +
                ", itemName='" + itemName + '\'' +
                ", itemPrice=" + itemPrice +
                ", discountPrice=" + discountPrice +
                '}';
    }
}
```

주문 서비스 인터페이스
```java
public interface OrderService {
    Order createOrder(Long memberId, String itemName, int itemPrice);
}
```

주문 서비스 구현체
```java
public class OrderServiceImpl implements OrderService{
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    private final DiscountPolicy discountPolicy = new FixDiscountPolicy();

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}
```
- 주문 생성 요청이 들어오면 회원 정보를 조회하고 할인 정책을 적용한 다음 주문 객체를 생성하여 반환
    - `MemoryMemberRepository`와 `FixDiscountPolicy`를 구현체로 생성

### 주문과 할인 도메인 실행과 테스트

주문과 할인 정책
- 주문과 할인 정책 실행
    ```java
    public class OrderApp {
        public static void main(String[] args) {
            MemberService memberService = new MemberServiceImpl();
            OrderService orderService = new OrderServiceImpl();
    
            Long memberId = 1L;
            Member member = new Member(memberId, "memberA", Grade.VIP);
            memberService.join(member);
    
            Order order = orderService.createOrder(memberId, "itemA", 10000);
    
            System.out.println("order = " + order);
            System.out.println("order.calculatePrice = " + order.calculatePrice());
        }
    }
    ```
    - 애플리케이션 로직으로 테스트하는 것은 좋은 방법이 아님
- 주문과 할인 정책 테스트
    ```java
    public class OrderServiceTest {
        MemberService memberService = new MemberServiceImpl();
        OrderService orderService = new OrderServiceImpl();
    
        @Test
        void createOrder() {
            // Given
            Long memberId = 1L;
            Member member= new Member(memberId, "memberA", Grade.VIP);
    
            // When
            memberService.join(member);
            Order order = orderService.createOrder(memberId, "itemA", 10000);
    
            // Then
            Assertions.assertThat(order.getDiscountPrice()).isEqualTo(1000);
        }
    }
    ```

## 3. 스프링 핵심 원리 이해 2 - 객체 지향 원리 이용

### 새로운 할인 정책 개발

할인 정책 수정
- 할인률을 10%로 지정

**RateDiscountPolicy**<br />
![SPRING#0010](/assets/images/spring-core/0010-rate-discount-policy.png)

```java
public class RateDiscountPolicy implements DiscountPolicy{
    private int discountPercent = 10;

    @Override
    public int discount(Member member, int price) {
        if (member.getGrade() == Grade.VIP) {
            return price * discountPercent / 100;
        } else {
            return 0;
        }
    }
}
```

**RateDiscountPolicy 테스트**<br />
```java
class RateDiscountPolicyTest {
    RateDiscountPolicy discountPolicy = new RateDiscountPolicy();

    @Test
    @DisplayName("VIP는 10% 할인이 적용되어야 한다")
    void vip_o() {
        // Given
        Member member = new Member(1L, "memberVIP", Grade.VIP);

        // When
        int discount = discountPolicy.discount(member, 10000);

        // Then
        assertThat(discount).isEqualTo(1000);
    }

    @Test
    @DisplayName("VIP가 아니면 할인이 적용되지 않아야 한다")
    void vip_x() {
        // Given
        Member member = new Member(2L, "memberVIP", Grade.BASIC);

        // When
        int discount = discountPolicy.discount(member, 10000);

        // Then
        assertThat(discount).isEqualTo(1000);
    }
}
```

### 새로운 할인 정책 적용과 문제점

새로운 할인 정책을 적용하려면 클라이언트인 `OrderServiceImpl`을 수정해야 함
```java
public class OrderServiceImpl implements OrderService{
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    // private final DiscountPolicy discountPolicy = new FixDiscountPolicy();
    private final DiscountPolicy discountPolicy = new RateDiscountPolicy();

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}
```
- 객체지향 설계 원칙인 OCP, DIP 위반
    - 추상 인터페이스 뿐만 아니라 구현 클래스도 의존하고 있으므로 DIP 위반
    - 기능을 확장하면 클라이언트 코드에 영향을 주므로 OCP 위반

인터페이스에만 의존하도록 코드 변경
```java
public class OrderServiceImpl implements OrderService{
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    // private final DiscountPolicy discountPolicy = new FixDiscountPolicy();
    // private final DiscountPolicy discountPolicy = new RateDiscountPolicy();
    private DiscountPolicy discountPolicy;

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}
```
- 지금은 구현체가 할당되지 않아 코드가 실행되지 않음
    - NPE(Null Pointer Error) 발생
- 이 문제를 해결하려면 누군가가 클라이언트인 OrderServiceImple에 DiscountPolicy의 구현 객체를 대신 생성하고 주입해야 함

### 관심사의 분리

AppConfig의 등장
- 애플리케이션의 전체 동작 방식을 구성
- 구현 객체를 생성하고 연결하는 책임을 갖는 별도의 설정 클래스
```java
public class AppConfig {

    public MemberService memberService() {
        return new MemberServiceImpl(new MemoryMemberRepository());
    }

    public OrderService orderService() {
        return new OrderServiceImpl(new MemoryMemberRepository(), new FixDiscountPolicy());
    }

}
```
- AppConfig는 애플리케이션의 실제 동작에 필요한 구현 객체를 생성
- AppConfig는 생성된 객체 인스턴스의 참조를 생성자를 통해 주입

생성자 주입: MemberServiceImpl
```java
public class MemberServiceImpl implements MemberService{

    private final MemberRepository memberRepository;

    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Override
    public void join(Member member) {
        memberRepository.save(member);
    }

    @Override
    public Member findMember(Long memberId) {
        return memberRepository.findById(memberId);
    }

}
```
- 설계 변경을 통해 더이상 구현 객체인 MemoryMemberRepository에 의존하지 않음
    - MemberRepository 인터페이스에만 의존
- 의존 관계는 외부(AppConfig)에서 결정

클래스 다이어그램<br />
![SPRING#0011](/assets/images/spring-core/0011-appconfig-class.png)
- 객체의 생성과 연결은 `AppConfig`가 담당
- DIP의 완성: `MemberServiceImpl`은 `MemberRepository`에만 의존하면 됨
    - 구체 클래스에 대해서는 몰라도 됨
- 관심사의 분리 → 객체를 생성하고 연결하는 역할과 실행하는 역할이 명확히 분리됨

회원 객체 인스턴스 다이어그램<br />
![#SPRING#0012](/assets/images/spring-core/0012-member-object-instance.png)
- `appConfig` 객체는 `memoryMemberRepository` 객체를 생성하고 그 참조값을 `memberServiceImpl`에 생성, 주입
- 클라이언트인 `memberServiceImpl` 입장에서 보면 의존관계를 마치 외부에서 주입해주는 것 같다고 해서 DI(Dependency Injection)이라고 함

생성자 주입: OrderServiceImpl
```java
public class OrderServiceImpl implements OrderService{

    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }

}
```

연계된 다른 클래스 수정
```java
public class MemberApp {
    public static void main(String[] args) {

        AppConfig appConfig = new AppConfig();
        MemberService memberService = appConfig.memberService();
        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        Member findMember = memberService.findMember(1L);
        System.out.println("new member = " + member.getName());
        System.out.println("find member = " + findMember.getName());
    }

}
```

```java
public class OrderApp {
    
    public static void main(String[] args) {
        AppConfig appConfig = new AppConfig();
        MemberService memberService = appConfig.memberService();
        OrderService orderService = appConfig.orderService();

        Long memberId = 1L;
        Member member = new Member(memberId, "memberA", Grade.VIP);
        memberService.join(member);

        Order order = orderService.createOrder(memberId, "itemA", 10000);

        System.out.println("order = " + order);
        System.out.println("order.calculatePrice = " + order.calculatePrice());
    }
    
}
```

```java
public class MemberServiceTest {

    MemberService memberService;

    @BeforeEach
    public void beforeEach(){
        AppConfig appConfig = new AppConfig();
        memberService = appConfig.memberService();
    }

    @Test
    void join() {
        // Given
        Member member = new Member(1L, "memberA", Grade.VIP);

        // When
        memberService.join(member);
        Member findMember = memberService.findMember(1L);

        // Then
        Assertions.assertThat(member).isEqualTo(findMember);
    }

}
```

```java
public class OrderServiceTest {

    MemberService memberService;
    OrderService orderService;

    @BeforeEach
    public void beforeEach() {
        AppConfig appConfig = new AppConfig();
        memberService = appConfig.memberService();
        orderService = appConfig.orderService();
    }

    @Test
    void createOrder() {
        // Given
        Long memberId = 1L;
        Member member= new Member(memberId, "memberA", Grade.VIP);

        // When
        memberService.join(member);
        Order order = orderService.createOrder(memberId, "itemA", 10000);

        // Then
        Assertions.assertThat(order.getDiscountPrice()).isEqualTo(1000);
    }

}
```

정리
- `AppConfig`를 통해 관심사를 명확하게 분리
- `AppConfig`는 구체 클래스를 선택 - 애플리케이션이 동작하는 전체 구성을 책임짐
- `MemberServiceImpl`과 `OrderServiceImpl`은 기능의 실행을 책임짐

### AppConfig 리팩터링

기대하는 형태<br />
![SPRING#0013](/assets/images/spring-core/0013-appconfig-hope.png)

```java
public class AppConfig {

    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    public OrderService orderService() {
        return new OrderServiceImpl(memberRepository(), discountPolicy());
    }

    public DiscountPolicy discountPolicy() {
        return new FixDiscountPolicy();
    }

}
```
- 중복을 제거하고 역할에 따른 구현이 보이도록 리팩터링

### 새로운 구조와 할인 정책 적용

정액 할인 정책을 정률 할인 정책으로 변경
- `FixDiscountPolicy` → `RateDiscountPolicy`

사용, 구성의 분리<br />
![SPRING#0014](/assets/images/spring-core/0014-revise-discount-policy-1.png)

할인 정책 변경<br />
![SPRING#0014](/assets/images/spring-core/0015-revise-discount-policy-2.png)

```java
public class AppConfig {

    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    public OrderService orderService() {
        return new OrderServiceImpl(memberRepository(), discountPolicy());
    }

    public DiscountPolicy discountPolicy() {
        // return new FixDiscountPolicy();
        return new RateDiscountPolicy();
    }

}
```
- `AppConfig`에서 할인 정책 역할을 담당하는 구현을 `FixDiscountPolicy`에서 `RateDiscountPolicy` 객체로 변경
- 할인 정책을 변경해도, 애플리케이션의 구성 역할을 담당하는 `AppConfig`만 변경하면 됨
    - 클라이언트 코드는 수정할 필요 없음

### 전체 흐름 정리

**새로운 할인 정책 개발**<br />
다형성 덕분에 새로운 정률 할인 정책 코드를 추가로 개발하는 것 자체는 문제 없음

**새로운 할인 정책의 적용과 문제점**<br />
새로 개발한 정률 할인 정책을 적용하려면 클라이언트 코드인 주문 서비스 구현체도 함께 수정해야 함<br />
주문 서비스 클라이언트가 인터페이스인 `DiscountPolicy` 뿐만 아니라, 구체 클래스인 `FixDiscountPolicy`도 함께 의존<br />
→ DIP 위반

**관심사의 분리**<br />
- 기존에는 클라이언트가 의존하는 서버 구현 객체를 직접 생성하고 실행
- `AppConfig`의 등장
- `AppConfig`는 애플리케이션의 전체 동작 방식을 구성하기 위해, 구현 객체를 생성하고 연결하는 역할을 함
- 이제 클라이언트 객체는 자신의 역할을 실행하는 것에만 집중 → 책임이 명확해짐

**AppConfig** 리팩터링<br />
- 구성 정보에서 역할과 구현을 명확하게 분리
- 중복 제거

**새로운 구조와 할인 정책 적용**

### 좋은 객체 지향 설계의 5가지 원칙의 적용

여기서는 SRP, DIP, OCP 적용

**SRP 단일 책임 원칙**<br />
한 클래스는 하나의 책임만 가져야 한다.
- 클라이언트 객체는 직접 구현 객체를 생성하고, 연결하고, 실행하는 다양한 책임을 가지고 있음
- SRP 단일 책임 원칙에 따라 관심사를 분리
- 구현 객체를 생성하고 연결하는 책임은 `AppConfig`가 담당
- 클라이언트 객체는 실행하는 책임만 담당

**DIP 의존관계 역전 원칙**<br />
프로그래머는 "추상화에 의존해야지, 구체화에 의존하면 안된다."<br />
의존성 주입은 이 원칙을 따르는 방법 중 하나
- 새로운 할인 정책을 개발하고, 적용하려고 하니 클라이언트 코드도 함께 변경해야 했음
    - 기존 클라이언트 코드는 DIP를 지키며 추상화 인터페이스에 의존하는 것 같았지만, 구체화 구현 클래스에도 함께 의존
- 클라이언트 코드가 추상화 인터페이스에만 의존하도록 코드를 변경
    - 그러나 클라이언트 코드는 인터페이스만으로는 아무것도 실행할 수 없음
- `AppConfig`가 객체 인스턴스를 클라이언트 코드 대신 생성해서 클라이언트 코드에 의존관계를 주입
    - DIP 원칙을 따르면서 문제도 해결했다.

**OCP 개방-폐쇄 원칙**<br />
소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.
- 다형성을 사용하고 클라이언트가 DIP를 지킴
- 애플리케이션을 사용 영역과 구성 영역으로 나눔
- AppConfig가 의존관계를 변경하여 클라이언트 코드에 주입하므로 클라이언트 코드를 변경하지 않아도 됨

### IoC, DI, 그리고 컨테이너

**제어의 역전 IOC(Inversion of Control)**<br />
- 기존 프로그램은 클라이언트 구현 객체가 스스로 필요한 서버 구현 객체를 생성하고 연결하고 실행함
    - 구현 객체가 프로그램의 제어 흐름을 스스로 조종
- `AppConfig`가 등장한 이후, 구현 객체는 자신의 로직을 실행하는 역할만 담당하고 프로그램의 제어 흐름은 `AppConfig`가 가져감
    - 프로그램의 제어 흐름에 대한 권한은 모두 `AppConfig`가 보유
    - 구현 객체의 생성과 실행도 제어
- 프로그램의 제어 흐름을 직접 게어하는 것이 아니라 외부에서 관리하는 것을 제어의 역전(IoC)라고 부름

프레임워크 vs. 라이브러리<br />
- 프레임워크: 내가 작성한 코드를 제어하고 대신 실행
- 라이브러리: 내가 작성한 코드가 직접 제어의 흐름을 담당

**의존관계 주입 DI(Dependency Injection)**<br />
- 의존관계는 정적인 클래스 의존관계와, 실행 시점에 결정되는 동적인 객체(인스턴스) 의존관계를 분리해서 생각해야 한다.

정적인 클래스 의존관계
- 클래스가 사용하는 import 코드만 보고 의존관계를 쉽계 판단할 수 있음
- 정적인 의존관계는 애플리케이션을 실행하지 않아도 분석할 수 있음

![SPRING#0016](/assets/images/spring-core/0016-dependency-static.png)

동적인 객체 인스턴스 의존관계
- 애플리케이션 실행 시점에 실제 생성된 객체 인스턴스의 참조가 연결된 의존관계

![SPRING#0017](/assets/images/spring-core/0017-dependency-dynamic.png)
- 의존관계 주입: 애플리케이션 실행 시점(런타임)에 외부에서 실제 구현 객체를 생성하고 클라이언트에 전달해서 클라이언트와 서버의 실제 의존관계가 연결되는 것
    - 객체 인스턴스를 생성하고, 그 찹조값을 전달해서 연결
- 의존관계 주입을 통해 클라이언트 코드를 변경하지 않고, 클라이언트가 호출하는 대상의 타입 인스턴스 변경 가능
- 의존관계 주입을 사용하면 정적인 클래스 의존관계를 변경하지 않고, 동적인 객체 인스턴스 의존관계를 쉽게 변경할 수 있음

**IoC 컨테이너, DI 컨테이너**
- `AppConfig`처럼 객체를 생성하고 관리하면서 의존관계를 연결해주는 것
- 의존관계 주입에 초점을 맞춰 최근에는 주로 DI 컨테이너라고 부름

### 스프링으로 전환하기

순수한 자바 코드 → 스프링

```java
@Configuration
public class AppConfig {

    @Bean
    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    @Bean
    public OrderService orderService() {
        return new OrderServiceImpl(memberRepository(), discountPolicy());
    }

    @Bean
    public DiscountPolicy discountPolicy() {
//        return new FixDiscountPolicy();
        return new RateDiscountPolicy();
    }

}
```
- `AppConfig`에 스프링 설정을 구성한다는 의미로 `@Configuration`을 붙임
- 각 메서드에 `@Bean`을 붙여 스프링 컨테이너의 스프링 빈으로 등록

```java
public class MemberApp {

    public static void main(String[] args) {
//        AppConfig appConfig = new AppConfig();
//        MemberService memberService = appConfig.memberService();

        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberService memberService = applicationContext.getBean("memberService", MemberService.class);

        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        Member findMember = memberService.findMember(1L);
        System.out.println("new member = " + member.getName());
        System.out.println("find member = " + findMember.getName());
    }

}
```

```java
public class OrderApp {

    public static void main(String[] args) {
//        AppConfig appConfig = new AppConfig();
//        MemberService memberService = appConfig.memberService();
//        OrderService orderService = appConfig.orderService();

        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberService memberService = applicationContext.getBean("memberService", MemberService.class);
        OrderService orderService = applicationContext.getBean("orderService", OrderService.class);

        Long memberId = 1L;
        Member member = new Member(memberId, "memberA", Grade.VIP);
        memberService.join(member);

        Order order = orderService.createOrder(memberId, "itemA", 20000);

        System.out.println("order = " + order);
    }

}
```

**스프링 컨테이너**
- `ApplicationContext`를 스프링 컨테이너라고 함
    - 기존에는 개발자가 `AppConfig`를 사용해서 직접 객체를 생성하고 DI를 함
    - 지금부터는 스프링 컨테이너를 사용
- 스프링 컨테이너는 `@Configuration`이 붙은 `AppConfig`를 설정 정보로 사용
    - `@Bean`이라 적힌 메서드를 모두 호출해서 반환된 객체를 스프링 컨테이너에 등록
    - 스프링 컨테이너에 등록된 객체를 스프링 빈이라고 함
- 스프링 빈은 `@Bean`이 붙은 메서드의 이름을 스프링 빈의 이름으로 사용
- 스프링 빈은 `applicationContext.getBean()` 매서드를 통해 찾을 수 있음
- 기존에는 개발자가 직접 자바 코드로 모든 것을 했다면, 지금부터는 스프링 컨테이너에 객체를 스프링 빈으로 등록하고 스프링 컨테이너에서 스프링 빈을 찾아서 사용

*코드가 좀 더 복잡해졌는데, 스프링 컨테이너를 사용하면 어떤 장점이 있는가?*

## 4. 스프링 컨테이너와 스프링 빈

### 스프링 컨테이너 생성

**스프링 컨테이너의 생성**<br />
```java
ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
```
- `ApplicationContext`는 스프링 컨테이너
- `ApplicationContext`는 인터페이스
- 스프링 컨테이너트투 XML 또는 Annotation 기반의 자바 설정 클래스로 만들 수 있음
    - 상기 `AppConfig`는 Annotation 기반의 자바 설정 클래스로 스프링 컨테이너를 만든 것

**스프링 컨테이너의 생성 과정**

1. 스프링 컨테이너 생성

![SPRING#0018](/assets/images/spring-core/0018-create-spring-core.png)
- `new AnnotationConfigApplicationContext(AppConfig.class)`
- 스프링 컨테이너를 생성할 때는 구성 정보를 지정해야 함
    - `AppConfig.Class`

2. 스프링 빈 등록

![SPRING#0019](/assets/images/spring-core/0019-enroll-spring-bean.png)
- 스프링 컨테이너는 파라미터로 넘어온 클래스 정보를 사용해서 스프링 빈을 등록한다.

빈 이름<br />
- 빈 이름은 메서드 이름을 사용
- 빈 이름을 직접 부여할 수도 있음
    - `@Bean(name="memberService2")`
- 빈 이름은 항상 다른 이름을 부여해야 함
    - 빈 이름이 중복되면 다른 빈이 무시되거나 기존 빈을 덮어버리거나 오류가 발생할 수 있음

3. 스프링 빈 의존관계 설정 - 준비

![SPRING#0020](/assets/images/spring-core/0020-appconfig.png)

4. 스프링 빈 의존관계 설정 - 완료

![SPRING#0021](/assets/images/spring-core/0021-spring-bean-dependency.png)
- 스프링 컨테이너는 설정 정보를 참고해서 의존관계를 주입(DI)
- 단순히 자바 코드를 호춣하는 것 같지만, 차이가 있음

- 스프링은 빈을 생성하고 의존관계를 주입하는 단계가 나누어져 있음
- 자바 코드로 스프링 빈을 등록하면 생성자를 호출하면서 의존관계 주입도 한 번에 처리됨

### 컨테이너에 등록된 모든 빈 조회

```java
class ApplicationContextInfoTest {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("모든 빈 출력하기")
    void findAllBean() {
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();

        for (String beanDefinitionName: beanDefinitionNames) {
            Object bean = ac.getBean(beanDefinitionName);
            System.out.println("name = " + beanDefinitionName + " object = " + bean);
        }
    }

    @Test
    @DisplayName("애플리케이 빈 출력하기")
    void findApplicationBean() {
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();

        for (String beanDefinitionName: beanDefinitionNames) {
            BeanDefinition beanDefinition = ac.getBeanDefinition(beanDefinitionName);

            // Role ROLE_APPLICATION: 직접 등록한 빈 애플리케이션
            // Role ROLE_INFRASTRUCTURE: 스프링이 내부에서 사용하는 빈
            if(beanDefinition.getRole() == BeanDefinition.ROLE_APPLICATION) {
                Object bean = ac.getBean(beanDefinitionName);
                System.out.println("name = " + beanDefinitionName + " object = " + bean);
            }
        }
    }

}
```
- 모든 빈 출력하기
    - 실행하면 스프링에 등록된 모든 빈 정보를 출력
    - `ac.getBeanDefinitionNames()`: 스프링에 등록된 모든 빈 이름을 조회
    - `ac.getBean()`: 빈 이름으로 빈 객체(인스턴스)를 조회
- 애플리케이션 빈 출력하기
    - 스프링이 내부에서 사용하는 빈은 제외하고, 내가 등록한 빈만 출력
    - 스프링이 내부에서 사용하는 빈은 `getRole()`로 구분
        - `ROLE_APPLICATION`: 일반적으로 사용자가 정의한 빈
        - `ROLE_INFRASTRUCTURE`: 스프링이 내부에서 사용하는 빈

### 스프링 빈 조회 - 기본

스프링 컨테이너에서 스프링 빈을 찾는 가장 기본적인 조회 방법
- `ac.getBean(빈 이름, 타입)`
- `ac.getBean(타입)`
- 조회 대상 스프링 빈이 없으면 예외 발생
    - `NoSuchBeanDefinitionException: No bean named 'xxxxx' available`

```java
class ApplicationContextBasicFindTest {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("빈 이름으로 조회")
    void findBeanByName() {
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("이름 없이 타입으로만 조회")
    void  findBeanByType() {
        MemberService memberService = ac.getBean(MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    // 구체 타입으로 조회하면 유연성이 떨어짐
    @Test
    @DisplayName("구체 타입으로 조회")
    void  findBeanByType2() {
        MemberService memberService = ac.getBean("memberService", MemberServiceImpl.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("빈 이름으로 조회 X")
    void findBeanByNameX() {
//        ac.getBean("xxxxx", MemberService.class);
        assertThrows(NoSuchBeanDefinitionException.class,
                () -> ac.getBean("xxxxx", MemberService.class));
    }

}
```

### 스프링 빈 조회 - 동일한 타입이 둘 이상

- 타입으로 조회시 같은 타입의 스프링 빈이 둘 이상이면 오류 발생
    - 이 때는 빈 이름을 지정
- `ac.getBeansOfType()`을 사용하면 해당 타입의 모든 빈을 조회할 수 있음

```java
public class ApplicationContextSameBeanFindTest {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(SameBeanConfig.class);

    @Test
    @DisplayName("타입으로 조회시 같은 타입이 둘 이상 있으면, 중복 오류가 발생한다.")
    void findBeanByTypeDuplicate() {
        assertThrows(NoUniqueBeanDefinitionException.class,
                () -> ac.getBean(MemberRepository.class));
    }

    @Test
    @DisplayName("타입으로 조회시 같은 타입이 둘 이상 있으면, 빈 이름을 지정하면 된다.")
    void findBeanByName() {
        MemberRepository memberRepository = ac.getBean("memberRepository1", MemberRepository.class);
        assertThat(memberRepository).isInstanceOf(MemberRepository.class);
    }

    @Test
    @DisplayName("특정 타입을 모두 조회하기")
    void findBeanByType() {
        Map<String, MemberRepository> beansOfType = ac.getBeansOfType(MemberRepository.class);

        for (String key: beansOfType.keySet()) {
            System.out.println("key = " + key + " value = " + beansOfType.get(key));
        }

        System.out.println("beansOfType = " + beansOfType);
        assertThat(beansOfType.size()).isEqualTo(2);
    }

    @Configuration
    static class SameBeanConfig {

        @Bean
        public MemberRepository memberRepository1() {
            return new MemoryMemberRepository();
        }

        @Bean
        public MemberRepository memberRepository2() {
            return new MemoryMemberRepository();
        }

    }

}
```

### 스프링 빈 조회 - 상속 관계

![SPRING#0021](/assets/images/spring-core/0021-spring-bean-search.png)
- 부모 타입으로 조회하면 자식 타입도 함께 조회
- 모든 자바 객체인 최고 부모인 `Object` 타입으로 조회하면, 모든 스프링 빈이 조회됨

```java
class ApplicationContextExtendsFindTest {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(TestConfig.class);

    @Test
    @DisplayName("부모 타입으로 조회 시 자식이 둘 이상 있으면, 중복 오류가 발생한다.")
    void findBeanByParentTypeDuplicate() {
        assertThrows(NoUniqueBeanDefinitionException.class,
                () -> ac.getBean(DiscountPolicy.class));
    }

    @Test
    @DisplayName("부모 타입으로 조회 시 자식이 둘 이상 있으면, 빈 이름을 지정하면 된다.")
    void findBeanByParentTypeBeanName() {
        DiscountPolicy rateDiscountPolicy = ac.getBean("rateDiscountPolicy", DiscountPolicy.class);
        assertThat(rateDiscountPolicy).isInstanceOf(RateDiscountPolicy.class);
    }

    @Test
    @DisplayName("특정 하위 타입으로 조회")
    void findBeanBySubType() {
        RateDiscountPolicy rateDiscountPolicy = ac.getBean(RateDiscountPolicy.class);
        assertThat(rateDiscountPolicy).isInstanceOf(RateDiscountPolicy.class);
    }

    @Test
    @DisplayName("부모 타입으로 모두 조회하기")
    void findAllBeanByParentType() {
        Map<String, DiscountPolicy> beansOfType = ac.getBeansOfType(DiscountPolicy.class);
        assertThat(beansOfType.size()).isEqualTo(2);
        for (String key: beansOfType.keySet()) {
            System.out.println("key = " + key + " value " + beansOfType.get(key));
        }
    }

    @Test
    @DisplayName("부모 타입으로 모두 조회하기 - Object")
    void findAllBeanByObjectType() {
        Map<String, Object> beansOfType = ac.getBeansOfType(Object.class);
        for (String key: beansOfType.keySet()) {
            System.out.println("key = " + key + " value " + beansOfType.get(key));
        }
    }

    @Configuration
    static class TestConfig {

        @Bean
        public DiscountPolicy rateDiscountPolicy() {
            return new RateDiscountPolicy();
        }

        @Bean
        public DiscountPolicy fixDiscountPolicy() {
            return new FixDiscountPolicy();
        }
    }
    
}
```

### BeanFactory와 ApplicationContext

![SPRING#0023](/assets/images/spring-core/bean-factory.png)

**BeanFactory**<br />
- 스프링 컨테이너의 최상위 인터페이스
- 스프링 빈을 관리하고 조회하는 역할을 담당
- `getBean()`을 제공
- 지금까지 우리가 사용한 대부분의 기능은 BeanFactory가 제공하는 기능

**ApplicationContext**<br />
- BeanFactory의 기능을 모두 상속받아서 제공
- 빈을 관리하고 검색하는 기능을 BeanFactory가 제공해주는데, 둘의 차이는?
    - 애플리케이션을 개발할 때는 빈을 관리하고 조회하는 기능 외에도 수많은 부가 기능이 필요함

**ApplicationContext**가 제공하는 부가 기능<br />
![SPRING#0024](/assets/images/spring-core/0024-application-context.png)
- 메시지 소스를 활용한 국제화 기능
- 환경 변수
    - 로컬, 개발, 운영 등의 환경을 구분해서 처리
- 애플리케이션 이벤트
    - 이벤트를 발행하고 구독하는 모델을 편리하게 지원
- 편리한 리소스 조회
    - 파일, 클래스 패스, 외부 등에서 리소스를 편리하게 조회

### 다양한 설정 형식 지원 - 자바 코드, XML

스프링 컨테이너는 다양한 형식의 설정 정보를 받아드릴 수 있게 유연하게 설계되어 있음
- Java, XML, Groovy 등

![SPRING#0025](/assets/images/spring-core/0025-xml-config.png)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="memberService" class="hello.core.member.MemberServiceImpl">
        <constructor-arg name="memberRepository" ref="memberRepository" />
    </bean>

    <bean id="memberRepository" class="hello.core.member.MemoryMemberRepository" />

    <bean id="orderService" class="hello.core.order.OrderServiceImpl">
        <constructor-arg name="memberRepository" ref="memberRepository" />
        <constructor-arg name="discountPolicy" ref="discountPolicy" />
    </bean>

    <bean id="discountPolicy" class="hello.core.discount.RateDiscountPolicy" />

</beans>
```

```java
class XmlAppContext {

    @Test
    void xmlAppContext() {
        ApplicationContext ac = new GenericXmlApplicationContext("appConfig.xml");
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        assertThat(memberService).isInstanceOf(MemberService.class);
    }

}
```

### 스프링 빈 설정 메타 정보 - BeanDefinition

- 스프링이 다양한 설정 형식을 지원하는 방법 → `BeanDefinition`
- 역할과 구현을 개념적으로 나눈 것
    - XML을 읽어서 BeanDefinition을 만듦
    - Java 코드를 읽어서 BeanDefinition을 만듦
    - 스프링 컨테이너는 Java인지 XML인지 몰라도 됨 → 오직 BeanDefinition만 알면 됨
- `BeanDefinition`을 빈 설정 메타정보라고 함
    - `@Bean`, `<bean>` 당 하나의 메타 정보가 생성
- 스프링 컨테이너는 이 메타 정보를 기반으로 스프링 빈을 생성

![SPRING#0026](/assets/images/spring-core/0026-bean-definition.png)
![SPRING#0027](/assets/images/spring-core/0027-application-context.png)
- `AnnotationConfigApplicationContext`는 `AnnotatedBeanDefinitionReader`를 사용해서 `AppConfig.class`를 읽고 `BeanDefinition`을 생성
- `GenericXmlApplicationContext`는 `XmlBeanDefinitionReader`를 사용해서 `appConfig.xml` 설정 정보를 읽고 `BeanDefinition`을 생성
- 새로운 형식의 설정 정보가 추가되면, `XxxBeanDefinitionReader`를 만들어서 `BeanDefinition` 을 생성

**BeanDefinition 정보**<br />
- BeanClassName: 생성할 빈의 클래스 명(자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)
- factoryBeanName: 팩토리 역할의 빈을 사용할 경우 이름, `appConfig`
- factoryMethodName: 빈을 생성할 팩토리 메서드 지정, `memberService`
- Scope: 싱글톤(기본값)
- lazyInit: 스프링 컨테이너를 생성할 때 빈을 생성하는 것이 아니라, 실제 빈을 사용할 때 까지 최대한 생성을 지연처리 하는지 여부
- InitMethodName: 빈을 생성하고, 의존관계를 적용한 뒤에 호출되는 초기화 메서드 명
- DestroyMethodName: 빈의 생명주기가 끝나서 제거하기 직전에 호출되는 메서드 명
- Constructor arguments, Properties: 의존관계 주입에서 사용 (자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)

```java
public class BeanDefinitionTest {

//    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
    GenericXmlApplicationContext ac = new GenericXmlApplicationContext("appConfig.xml");

    @Test
    @DisplayName("빈 설정 메타정보 확인")
    void findApplicationBean() {
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();
        for (String beanDefinitionName: beanDefinitionNames) {
            BeanDefinition beanDefinition = ac.getBeanDefinition(beanDefinitionName);

            if (beanDefinition.getRole() == BeanDefinition.ROLE_APPLICATION) {
                System.out.println("beanDefinitionName = " + beanDefinitionName + " beanDefinition = " + beanDefinition);
            }
        }
    }

}
```
- `BeanDefinition`을 직접 생성해서 스프링 컨테이너에 등록할 수 도 있음
    - 하지만 실무에서 `BeanDefinition`을 직접 정의하거나 사용할 일은 거의 없음
- `BeanDefinition`에 대해서는 너무 깊이있게 이해하기 보다는, 스프링이 다양한 형태의 설정 정보를 `BeanDefinition`으로 추상화해서 사용하는 것 정도만 이해하면 됨

## 5. 싱글톤 컨테이너

### 웹 애플리케이션과 싱글톤

- 스프링은 기업용 온라인 서비스 기술을 지원하기 위해 탄생
- 대부분의 스프링 애플리케이션은 웹 애플리케이션
    - 웹이 아닌 애플리케이션 개발도 할 수 있음
- 웹 애플리케이션은 보통 여러 고객들이 동시에 요청을 함

```java
public class pureContainer {
    
    @Test
    @DisplayName("스프링 없는 순수한 DI 컨테이너")
    void pureContainer() {
        AppConfig appConfig = new AppConfig();

        // 1. 조회: 호출할 때마다 객체를 생성
        MemberService memberService1 = appConfig.memberService();

        // 2. 조회: 호출할 때마다 객체를 생성
        MemberService memberService2 = appConfig.memberService();

        // 참조값이 다른 것을 확인
        System.out.println("memberService1 = " + memberService1);
        System.out.println("memberService2 = " + memberService2);

        assertThat(memberService1).isNotSameAs(memberService2);
    }

}
```
- 스프링 없는 순수한 DI 컨테이너인 `AppConfig`는 요청을 할 때마다 객체를 새로 생성
- 고객 트래픽이 초당 100이 나오면 초당 100개의 객체가 생성되고 소멸됨 → 메모리 낭비
- 해결 방안: 해당 객체가 단 한 개만 생성되고 공유하도록 설계하면 됨 → 싱글톤 패턴 

### 싱글톤 패턴

**싱글톤 패턴**<br />
- 클래스의 인스턴스가 단 한 개만 생성되는 것을 보장하는 디자인 패턴
- 객체 인스턴스가 2개 이상 생성되지 못하도록 막아야 함
    - private 생성자를 사용해 외부에서 임의로 new 키워드를 사용하지 못하도록 막아야 함

```java
public class SingletonService {

    private static final SingletonService instance = new SingletonService();

    public static SingletonService getInstance() {
        return instance;
    }

    private SingletonService() {

    }

    public void logic() {
        System.out.println("싱글톤 객체 로직 호출");
    }
    
}
```
- static 영역에 객체 인스턴스를 미리 하나 생성해서 올려둠
- 이 객체 인스턴스가 필요하면 getInstance() 메서드를 통해서만 조회할 수 있음
    - 항상 같은 인스턴스를 반환
- 단 하나의 객체 인스턴스만 존재해야 하므로, 생성자를 private으로 막아서 혹시라도 외부에서 new 키워드로 객체 인스턴스가 생성되는 것을 막음

```java
public class SingletonTest {

    @Test
    @DisplayName("싱글톤 패턴을 적용한 객체 사용")
    void singletonServiceTest() {
        // private으로 생성자 생성을 막아두어 컴파일 오류 발생
//        new SingletonService();

        // 1. 조회: 호출할 때마다 같은 객체를 반환
        SingletonService singletonService1 = SingletonService.getInstance();
        // 2. 조회: 호출할 때마다 같은 객체를 반환
        SingletonService singletonService2 = SingletonService.getInstance();

        // 참조 값이 같은 것을 확인
        System.out.println("singletonService1 = " + singletonService1);
        System.out.println("singletonService2 = " + singletonService2);

        // singletonService1 == singletonService2
        assertThat(singletonService1).isSameAs(singletonService2);
        // same: ==
        // equal: equals 비교

        singletonService1.logic();
    }

}
```
- 싱글톤 패턴을 구현하는 방법은 다양함
- 상기 코드는 객체를 미리 생성해두는 가장 단순하고 안전한 방법을 선택

싱글톤 패턴을 적용하면 이미 만들어진 객체를 공유해서 고객의 요청에 효율적으로 적용할 수 있음<br />
그러나 싱글톤 패턴은 여러 문제점을 함께 가지고 있음

**싱글톤 패턴의 문제점**<br />
- 싱글톤 패턴을 구현하는 코드 자체가 많이 들어감
- 의존관계상 클라이언트가 구체 클래스에 의존
    - DIP를 위반
- 클라이언트가 구체 클래스에 의존해 OCP 원칙을 위반할 가능성이 높음
- 테스트하기 어려움
- 내부 속성을 변경하거나 초기화 하기 어려움
- private 생성자로 자식 클래스를 만들기 어려움
- 유연성이 떨어짐
- 안티패턴으로 불리기도 함

### 싱글톤 컨테이너

스프링 컨테이너는 싱글톤 패턴의 문제점을 해결하면서, 객체 인스턴스를 싱글톤으로 관리함<br />
지금까지 학습한 스프링 빈이 싱글톤으로 관리되고 있음

**싱글톤 컨테이너**<br />
- 스프링 컨테이너는 싱글톤 패턴을 적용하지 않아도, 객체 인스턴스를 싱글톤으로 관리함
    - 컨테이너는 객체를 하나만 생성해서 관리함
- 스프링 컨테이너는 싱글톤 컨테이너의 역할을 함
    - 싱글톤 객체를 생성하고 관리하는 기능을 싱글톤 레지스트리라고 함
- 스프링은 이러한 기능을 통해 싱글톤 패턴의 단점을 해결하면서 객체를 싱글톤으로 유지함
    - 싱글톤 패턴을 위한 코드 작성이 불필요
    - DIP, OCP, 테스트, private 생성자로부터 자유롭게 싱글톤을 사용할 수 있음

```java
public class SingletonTest {

    @Test
    @DisplayName("스프링 컨테이너와 싱글톤")
    void springContainer() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberService memberService1 = ac.getBean("memberService", MemberService.class);
        MemberService memberService2 = ac.getBean("memberService", MemberService.class);

        // 참조값이 다른 것을 확인
        System.out.println("memberService1 = " + memberService1);
        System.out.println("memberService2 = " + memberService2);

        assertThat(memberService1).isSameAs(memberService2);
    }

}
```

**싱글톤 컨테이너 적용 후**<br />
![SPRING#0029](/assets/images/spring-core/0029-spring-di-container.png)
- 스프링 컨테이너를 통해 이미 만들어진 객체를 공유해서 효율적으로 재사용할 수 있음

스프링 빈의 기본 빈 등록 방식은 싱글톤이지만, 싱글톤 방식만 지원하는 것은 아님<br />
요청할 때 마다 새로운 객체를 생성해서 반환하는 기능 역시 제공함

### 싱글톤 방식의 주의점

- 싱글톤 방식은 여러 클라이언트가 하나의 같은 객체 인스턴스를 공유하기 때문에 싱글톤 객체는 stateful하게 설계하면 안됨
    - Stateless로 설계해야 함
    - 특정 클라이언트에 의존적인 필드가 있으면 안됨
    - 특정 클라이언트가 값을 변경할 수 있는 필드가 있으면 안됨
    - 가급적 읽기만 가능해야 함
    - 필드 대신에 자바에서 공유되지 않는, 지역변수, 파라미터, ThreadLocal 등을 사용해야 함

```java
class StatefulServiceTest {

    @Test
    void statefulServiceSingleton() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(TestConfig.class);
        StatefulService statefulService1 = ac.getBean(StatefulService.class);
        StatefulService statefulService2 = ac.getBean(StatefulService.class);

        // Thread A: A 사용자가 10000원 주문
        statefulService1.order("userA", 10000);
        // Thread B: B 사용자가 20000원 주문
        statefulService1.order("userB", 20000);

        // Thread A: A 사용자 주문 금액 조회
        int price = statefulService1.getPrice();
        System.out.println("price = " + price);

        assertThat(statefulService1.getPrice()).isEqualTo(20000);
    }

    static class TestConfig {

        @Bean
        public StatefulService statefulService() {
            return new StatefulService();
        }

    }

}
```
- 최대한 단순히 설명하기 위해, 실제 쓰레드는 사용하지 않음
- ThreadA가 사용자A 코드를 호출하고 ThreadB가 사용자B 코드를 호출한다 가정
- `StatefulService` 의 `price` 필드는 공유되는 필드인데, 특정 클라이언트가 값을 변경
    - 사용자A의 주문금액은 10000원이 되어야 하는데, 20000원이라는 결과가 나옴
    - 공유필드는 조심해야 함! 스프링 빈은 항상 무상태(stateless)로 설계하자.

### @Configuration과 싱글톤

```java
@Configuration
public class AppConfig {

    @Bean
    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    @Bean
    public OrderService orderService() {
        return new OrderServiceImpl(memberRepository(), discountPolicy());
    }

    @Bean
    public DiscountPolicy discountPolicy() {
//        return new FixDiscountPolicy();
        return new RateDiscountPolicy();
    }

}
```
- `memberService` 빈을 만드는 코드를 보면 `memberRepository()`를 호출
    - 이 메서드를 호출하면 `new MemoryMemberRepository()`를 호출
- `orderService` 빈을 만드는 코드도 동일하게 `memberRepository()`를 호출
    - 이 메서드를 호출하면 `new MemoryMemberRepository()`를 호출

각각 다른 두 개의 `MemoryMemberRepository가` 생성되면서 싱글톤이 깨지는 것처럼 보이는데, 스프링은 이 문제를 어떻게 해결하는가?

```java
public class MemberServiceImpl implements MemberService{

    ...

    // 테스트용
    public MemberRepository getMemberRepository() {
        return memberRepository;
    }

}
```

```java
public class OrderServiceImpl implements OrderService{

    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }

    // 테스트용
    public MemberRepository getMemberRepository() {
        return memberRepository;
    }

}
```
- 검증을 위한 테스트용 코드 추가

```java
public class ConfigurationSingletonTest {

    @Test
    void configurationTest() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

        MemberServiceImpl memberService = ac.getBean("memberService", MemberServiceImpl.class);
        OrderServiceImpl orderService = ac.getBean("orderService", OrderServiceImpl.class);
        MemberRepository memberRepository = ac.getBean("memberRepository", MemberRepository.class);

        MemberRepository memberRepository1 = memberService.getMemberRepository();
        MemberRepository memberRepository2 = memberService.getMemberRepository();

        System.out.println("memberService --> memberRepository = " + memberRepository1);
        System.out.println("orderService --> memberRepository = " + memberRepository2);
        System.out.println("memberRepository = " + memberRepository);

        assertThat(memberService.getMemberRepository()).isSameAs(memberRepository);
        assertThat(orderService.getMemberRepository()).isSameAs(memberRepository);
    }

}
```
- 테스트 결과 `memberRepository` 인스턴스는 모두 같은 인스턴스가 공유되어 사용
- `AppConfig`를 보면 직관적으로 `new MemoryMemberRepository` 호출해서 두 개의 다른 인스턴스가 생성되어야 하는데 그렇지 않음

```java
@Configuration
public class AppConfig {

    @Bean
    public MemberService memberService() {
        System.out.println("call AppConfig.memberService");
        return new MemberServiceImpl(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        System.out.println("call AppConfig.memberRepository");
        return new MemoryMemberRepository();
    }

    @Bean
    public OrderService orderService() {
        System.out.println("call AppConfig.orderService");
        return new OrderServiceImpl(memberRepository(), discountPolicy());
    }

    @Bean
    public DiscountPolicy discountPolicy() {
//        return new FixDiscountPolicy();
        return new RateDiscountPolicy();
    }

}
```
- 스프링 컨테이너가 각각 `@Bean`을 호출해서 스프링 빈을 생성
- `memberRepository()`는 다음과 같이 총 3번이 호출되어야 하는 것처럼 보임
    1. 스프링 컨테이너가 스프링 빈에 등록하기 위해 @Bean이 붙어있는 memberRepository() 호출
    1. memberService() 로직에서 memberRepository() 호출
    1. orderService() 로직에서 memberRepository() 호출

결과는 모두 1번만 호출<br />
```
call AppConfig.memberService
call AppConfig.memberRepository
call AppConfig.orderService
```

### @Configuration과 바이트 코드 조작의 마법

스프링 컨테이너는 싱글톤 레지스트리 → 스프링 빈이 싱글톤이 되도록 보장<br />
스프링은 클래스의 바이트 코드를 조작하는 라이브러리를 사용
- `@Configuration`을 적용한 `AppConfig`에 비밀이 있음

```java
public class ConfigurationSingletonTest {

    @Test
    void configurationDeep() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
        AppConfig bean = ac.getBean(AppConfig.class);

        System.out.println("bean = " + bean.getClass());
    }

}
```
- `AnnotationConfigApplicationContext`에 파라미터로 넘긴 값은 스프링 빈으로 등록
- `AppConfig`도 스프링 빈이 됨

`AppConfig` 스프링 빈을 조회해서 클래스 정보를 출력<br />
```
bean = class hello.core.AppConfig$$EnhancerBySpringCGLIB$$dfa855fc
```

순수한 클래스라면 `class hello.core.AppConfig`으로 출력되어야 함

내가 만든 클래스가 아니라, 스프링이 CGLIB라는 바이트코드 조작 라이브러리를 사용해서 `AppConfig` 클래스를 상속받은 임의의 다른 클래스를 만들고, 그 다른 클래스를 스프링 빈으로 등록한 것

![SPRING#0030](/assets/images/spring-core/0030-cglib.png)
- 그 임의의 다른 클래스가 바로 싱글톤이 보장
- 아마도 다음과 같이 바이트 코드를 조작해서 작성되어 있을 것
    - 실제 CGLIB의 내부 기술은 매우 복잡하게 구성되어 있음

**정리**<br />
- `@Bean`만 사용해도 스프링 빈으로 등록되지만, 싱글톤을 보장하지 않음
    - `memberRepository()`처럼 의존관계 주입이 필요해 메서드를 직접 호출할 때, 싱글톤을 보장하지는 않음
- 스프링 설정 정보는 항상 @Configuration 을 사용할 것!!

## 6. 컴포넌트 스캔

### 컴포넌트 스캔과 의존 관계 자동 주입 시작하기

- 등록해야 할 스프링 빈이 수십, 수백 개가 되면 일일이 등록하기에 힘들어지며, 설정 정보도 커지게 되어 누락하는 문제가 발생할 수 있음
- 그래서 스프링은 설정 정보가 없어도 자동으로 스프링 빈을 등록하는 컴포넌트 스캔이라는 기능을 제공
- 또한 의존관계도 자동으로 주입하는 `@Autowired`라는 기능도 제공

```java
@Configuration
@ComponentScan(
        // 예제를 안전하기 유지하기 위해 Configuration을 제외
        excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Configuration.class)
)
public class AutoAppConfig {
}
```
- 컴포넌트 스캔을 사용하려면 먼저 `@ComponentScan`을 설정 정보에 붙여줘야 함
    - 컴포넌트 스캔을 사용하면 `@Configuration`이 붙은 설정 정보도 자동으로 등록되기 때문에, `AppConfig`, `TestConfig` 등 앞서 만들어두었던 설정 정보도 함께 등록, 실행됨
    - `excludeFilters 를 이용해서 설정정보는 컴포넌트 스캔 대상에서 제외함
- 기존의 AppConfig와 달리 `@Bean`으로 등록한 클래스가 없음

컴포넌트 스캔의 대상이 되도록 `@Component` 애노테이션 추가

```java
@Component
public class MemoryMemberRepository implements MemberRepository{}
```

```java
@Component
public class RateDiscountPolicy implements DiscountPolicy{}
```

```java
@Component
public class MemberServiceImpl implements MemberService{

    private final MemberRepository memberRepository;

    @Autowired  // ac.getBean(MemberRepository.class);
    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    ......

}
```

```java
@Component
public class OrderServiceImpl implements OrderService{

    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    ......
}
```
- 의존관계 주입도 이 클래스 안에서 해결

```java
public class AutoAppConfigTest {

    @Test
    void basicScan() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class);

        MemberService memberService = ac.getBean(MemberService.class);
        assertThat(memberService).isInstanceOf(MemberService.class);
    }
}
```

**컴포넌트 스캔과 자동 의존관계 주입의 동작 과정**

![SPRING#0031](/assets/images/spring-core/0031-component-scan.png)
- `@ComponentScan`은 `@Component`가 붙은 모든 클래스를 스프링빈으로 등록
- 스프링 빈의 기본 이름은 클래스명을 사용하되 맨 앞 글자만 소문자를 사용
    - 빈 이름 기본 전략: MemberServiceImpl 클래스 memberServiceImpl
    - 빈 이름 직접 지정: 만약 스프링 빈의 이름을 직접 지정하고 싶으면 `@Component("memberService2")` 이런식으로 이름을 부여하면 된다

![SPRING#0032](/assets/images/spring-core/0032-autowired-1.png)<br />
![SPRING#0032](/assets/images/spring-core/0033-autowired-2.png)
- 생성자에 @Autowired 를 지정하면, 스프링 컨테이너가 자동으로 해당 스프링 빈을 찾아서 주입

### 탐색 위치와 기본 스캔 대상

모든 자바 클래스를 다 컴포넌트 스캔하면 시간이 오래 걸림 → 꼭 필요한 위치부터 탐색하도록 시작 위치를 지정할 수 있음

```java
@Configuration
@ComponentScan(
        basePackages = "hello.core"
        // 예제를 안전하기 유지하기 위해 Configuration을 제외
        excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Configuration.class)
)
public class AutoAppConfig {
}
```
- `basePackages`: 탐색할 패키지의 시작 위치를 지정
    - 이 패키지를 포함한 하위 패키지를 모두 탐색
    - `basePackages = {"hello.core", "hello.service"}` 이렇게 여러 시작 위치를 지정할 수도 있음
- `basePackageClasses`: 지정한 클래스의 패키지를 탐색 시작 위치로 지정
- 지정하지 않으면 `@ComponentScan`이 붙은 설정 정보 클래스의 패키지가 시작 위치가 됨

**권장하는 방법**<br />
강사가 개인적으로 즐겨 사용하는 방법은 패키지 위치를 지정하지 않고, 설정 정보 클래스의 위치를 프로젝트 최상단에 둠<br />
최근 스프링 부트도 이 방법을 기본으로 제공함

- `com.hello`
- `com.hello.serivce`
- `com.hello.repository`

`com.hello` → 프로젝트 시작 루트, 여기에 AppConfig 같은 메인 설정 정보를 두고, `@ComponentScan` 애노테이션을 붙이고, `basePackages` 지정은 생략<br />
이렇게 하면 `com.hello`를 포함한 하위는 모두 자동으로 컴포넌트 스캔의 대상이 됨<br />
그리고 프로젝트 메인 설정 정보는 프로젝트를 대표하는 정보이기 때문에 프로젝트 시작 루트 위치에 두는 것이 좋음<br />
참고로 스프링 부트를 사용하면 스프링 부트의 대표 시작 정보인 @SpringBootApplication 를 이 프로젝트 시작 루트 위치에 두는 것이 관례<br />
그리고 이 설정안에 바로 @ComponentScan 이 들어있음

**컴포넌트 스캔 기본 대상**<br />
컴포넌트 스캔은 `@Component` 뿐만 아니라 다음과 내용도 추가로 대상에 포함

- `@Component`: 컴포넌트 스캔에서 사용
- `@Controlller`: 스프링 MVC 컨트롤러에서 사용
- `@Service`: 스프링 비즈니스 로직에서 사용
- `@Repository`: 스프링 데이터 접근 계층에서 사용
- `@Configuration`: 스프링 설정 정보에서 사용

> **참고**<br />
사실 애노테이션에는 상속관계라는 것이 없음<br />
이렇게 애노테이션이 특정 애노테이션을 들고 있는 것을 인식하는 것은 자바가 아닌, 스프링이 지원하는 기능임

다음 애노테이션이 있으면 스프링은 부가 기능을 수행함
- `@Controller`: 스프링 MVC 컨트롤러로 인식
- `@Repository`: 스프링 데이터 접근 계층으로 인식하고, 데이터 계층의 예외를 스프링 예외로 변환함
- `@Configuration`: 앞서 보았듯이 스프링 설정 정보로 인식하고, 스프링 빈이 싱글톤을 유지하도록 추가 처리
- `@Service`: 사실 `@Service` 는 특별한 처리를 하지 않음
    - 대신 개발자들이 "핵심 비즈니스 로직이 여기에 있겠구나" 라고 비즈니스 계층을 인식하는데 도움이 됨

> **참고**<br />
`useDefaultFilters` 옵션은 기본으로 켜져있는데, 이 옵션을 끄면 기본 스캔 대상들이 제외됨<br />
그냥 이런 옵션이 있구나 정도 알고 넘어가도 됨

### 필터

- `includeFilters`: 컴포넌트 스캔 대상을 추가로 지정
- `excludeFilters`: 컴포넌트 스캔에서 제외할 대상을 지정

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MyIncludeComponent {
}
```

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MyExcludeComponent {
}
```

```java
@MyIncludeComponent
public class BeanA {
}
```

```java
@MyExcludeComponent 
public class BeanB {
}
```

```java
public class ComponentFilterAppConfigTest {
    @Test
    void filterScan() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(ComponentFilterAppConfig.class);
        BeanA beanA = ac.getBean("beanA", BeanA.class);
        assertThat(beanA).isNotNull();

        assertThrows(
                NoSuchBeanDefinitionException.class,
                () -> ac.getBean("beanB", BeanB.class)
        );
    }

    @Configuration
    @ComponentScan(
            includeFilters = @Filter(type = FilterType.ANNOTATION, classes = MyIncludeComponent.class),
            excludeFilters = @Filter(type = FilterType.ANNOTATION, classes = MyExcludeComponent.class)
    )
    static class ComponentFilterAppConfig {
    }
}
```
- `includeFilters`에 `MyIncludeComponent` 애노테이션을 추가해서 `BeanA`가 스프링 빈에 등록됨
- `excludeFilters`에 `MyExcludeComponent` 애노테이션을 추가해서 `BeanB`는 스프링 빈에 등록되지 않음

**FilterType 옵션**<br />
- `ANNOTATION`: 기본값, 애노테이션을 인식해서 동작한다.
    - ex) `org.example.SomeAnnotation`
- `ASSIGNABLE_TYPE`: 지정한 타입과 자식 타입을 인식해서 동작한다.
    - ex) `org.example.SomeClass`
- `ASPECTJ`: AspectJ 패턴 사용
    - ex) `org.example..*Service+`
- `REGEX`: 정규 표현식
    - ex) `org\.example\.Default.*`
- `CUSTOM`: TypeFilter이라는 인터페이스를 구현해서 처리
    - ex) `org.example.MyTypeFilter`

상기 코드에서 BeanA도 빼고 싶으면 다음과 같이 작성

```java
@ComponentScan(
    includeFilters = {
        @Filter(type = FilterType.ANNOTATION, classes = MyIncludeComponent.class),
    },
    excludeFilters = {
        @Filter(type = FilterType.ANNOTATION, classes = MyExcludeComponent.class),
        @Filter(type = FilterType.ASSIGNABLE_TYPE, classes = BeanA.class)
    }
)
```

> **참고**<br />
`@Component`면 충분하기 때문에, `includeFilters`를 사용할 일은 거의 없음<br />
`excludeFilters`는 여러가지 이유로 간혹 사용할 때가 있지만 많지는 않음<br />
최신 스프링 부트는 컴포넌트 스캔을 기본으로 제공하는데, 개인적으로는 옵션을 변경하면서 사용하기보다는 스프링의 기본 설정에 최대한 맞추어 사용하는 것을 권장

### 중복 등록과 충돌

**자동 빈 등록 vs 자동 빈 등록**
- 컴포넌트 스캔에 의해 자동으로 스프링 빈이 등록되는데, 그 이름이 같은 경우 스프링은 오류를 발생
    - `ConflictingBeanDefinitionException` 예외 발생

**수동 빈 등록 vs 자동 빈 등록**
- 이 경우 수동 빈 등록이 우선권을 가짐
    - 수동 빈이 자동 빈을 오버라이딩 함

수동 빈 등록시 남는 로그

```bash
Overriding bean definition for bean 'memoryMemberRepository' with a different
definition: replacing
```

최근 스프링 부트에서는 수동 빈 등록과 자동 빈 등록이 충돌하면 오류를 발생하도록 수정
- 대부분의 경우 설정이 꼬여서 발생하기 때문

수동 빈 등록, 자동 빈 등록 오류시 스프링 부트 에러

```bash
Consider renaming one of the beans or enabling overriding by setting
spring.main.allow-bean-definition-overriding=true
```

## 7. 의존관계 자동 주입

### 다양한 의존관계 주입 방법

**의존관계 주입 방법**<br />
- 생성자 주입
- 수정자 주입(setter 주입)
- 필드 주입
- 일반 메서드 주입

**생성자 주입**<br />
- 생성자를 통해서 의존관계를 주입
    - 생성자 호출 시점에 딱 한 번만 호출되는 것이 보장
    - **불변**, **필수** 의존관계에 사용

```java
@Component
public class OrderServiceImpl implements OrderService{

    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

}
```
- 생성자가 딱 한 개만 있으면 `@Autowired`를 생략해도 자동 주입 (**스프링 빈**만)

**수정자 주입(setter 주입)**<br />
- setter라 불리는 필드의 값을 변경하는 수정자 메서드를 통해서 의존관계를 주입하는 방법
    - **선택**, **변경** 가능성이 있는 의존관계에 사용
    - 자바 빈 프로퍼티 규약의 수정자 메서드 방식을 사용하는 방법

```java
@Component
public class OrderServiceImpl implements OrderService {

    private MemberRepository memberRepository;
    private DiscountPolicy discountPolicy;

    @Autowired
    public void setMemberRepository(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Autowired
    public void setDiscountPolicy(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }
}
```
- `@Autowired`의 기본 동작은 주입할 대상이 없으면 오류 발생
    - 주입할 대상이 없어도 동작하게 하려면 `@Autowired(required = false)`로 지정
- 자바 빈 프로퍼티 규약: 필드의 값을 직접 변경하지 않고 setter, getter 메서드를 통해서 값을 읽거나 수정하는 규칙

**필드 주입**<br />
- 코드가 간결하지만 외부에서 변경이 불가능해 테스트하기 힘듬
- DI 프레임워크가 없으면 아무것도 할 수 없음
- 테스트 코드, 스프링 설정을 목적으로 하는 @Configuration 같은 곳에서만 특별한 용도로 사용
    - 일반적인 경우에는 사용하지 말것

```java
@Component
public class OrderServiceImpl implements OrderService {
    @Autowired
    private MemberRepository memberRepository;

    @Autowired
    private DiscountPolicy discountPolicy;
}
```
- 순수한 자바 테스트 코드에서는 `@Autowired`가 동작하지 않음
    - `@SpringBootTest`처럼 스프링 컨테이너를 테스트에 통합한 경우에만 가능
- `@Bean`에서 파라미터의 의존관계는 자동으로 주입됨

```java
@Bean
OrderService orderService(MemberRepository memberRepoisitory, DiscountPolicy discountPolicy) {
    new OrderServiceImpl(memberRepository, discountPolicy)
}
```

**일반 메서드 주입**<br />
- 한 번에 여러 필드를 주입받을 수 있음
- 일반적으로 잘 사용하지 않음

```java
@Component
public class OrderServiceImpl implements OrderService {

    private MemberRepository memberRepository;
    private DiscountPolicy discountPolicy;

    @Autowired
    public void init(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

}
```
- 의존관계 자동 주입은 스프링 컨테이너가 관리하는 스프링 빈이어야 동작
    - 스프링 빈이 아닌 `Member`같은 클래스에서는 `@Autowired` 코드를 적용해도 아무 기능도 동작하지 않음

### 옵션 처리

- 주입할 스프링 빈이 없어도 동작해야 할 때도 있음
- `@Autowired`만 사용하면 required 옵션의 기본값이 true로 설정되어 있어, 자동 주입 대상이 없으면 오류가 발생
- 자동 주입 대상을 옵션으로 처리하는 방법
    - `@Autowired(required=false)`: 자동 주입할 대상이 없으면 수정자 메서드 자체가 호출되지 않음
    - `@Nullable`: 자동 주입할 대상이 없으면 `null`이 입력됨
    - `Optional<>`: 자동 주입할 대상이 없으면 `Optional.empty`가 입력됨

```java
public class AutowiredTest {

    @Test
    void AutowiredOption() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(TestBean.class);
    }

    static class TestBean {

        @Autowired(required = false)
        public void setNoBean1(Member noBean1) {
            System.out.println("noBean1 = " + noBean1);
        }

        @Autowired
        public void setNoBean2(@Nullable Member noBean2) {
            System.out.println("noBean2 = " + noBean2);
        }

        @Autowired
        public void setNoBean3(Optional<Member> noBean3) {
            System.out.println("noBean3 = " + noBean3);
        }

    }

}
```
- `Member`는 스프링 빈이 아님

출력 결과<br />
```bash
noBean2 = null
noBean3 = Optional.empty
```
- `setNoBean1()`은 `@Autowired(required=false)`이므로 호출되지 않음
- `@Nullable`, `Optional<>`은 스프링 전반에 걸쳐 지원됨
    - 생성자 자동 주입에서 특정 필드에만 사용해도 됨

### 생성자 주입을 선택해라!

과거에는 수정자 주입과 필드 주입을 많이 사용했지만, 최근에는 스프링을 포함한 DI 프레임워크 대부분이 생성자 주입을 권장함

**불변**<br />
- 대부분의 의존관계 주입은 한 번 일어나면 애플리케이션 종료 시점까지 의존관계를 변경할 일이 없음
    - 오히려 대부분의 의존관계는 애플리케이션 종료 전까지 변하면 안됨
- 수정자 주입을 사용하면 setter 메서드를 public으로 열어두어야 함
- 누군가의 실수로 변경될 수 있는 설계는 좋은 설계가 아님
- 생성자 주입은 객체를 생성할 때 단 한 번만 호출되므로 불변하게 설계할 수 있음

**누락**<br />
- 생성자 주입을 사용하면 주입 데이터를 누락했을 때 컴파일 오류가 발생
    - 수정자 의존관계의 경우 테스트가 실행된 후 exception 오류가 발생할 수 있음
    - 생성자 주입을 사용하면 IDE에서 바로 어떤 값을 주입해야 하는지 알 수 있음

**final 키워드**<br />
- 생성자 주입을 사용하면 `final` 키워드를 사용할 수 있음
- 생성자에서 혹시라도 값이 설정되지 않는 오류를 컴파일 시점에서 막아줌
    - 수정자 주입을 포함한 나머지 주입 방식은 모두 생성자 이후에 호출되므로 필드에 final 키워드를 사용할 수 없음
    - `final` 키워드는 사전에 변수에 값을 기입하거나 생성자를 사용하는 경우에만 사용할 수 있음

> 항상 생성자 주입을 선택해라<br />
가끔 옵션이 필요하면 수정자 주입을 선택해라

### 롬복과 최신 트랜드

막상 개발을 하면 대부분의 변수가 변하지 않기 때문에 생성자 주입에 final 키워드를 사용한다.<br />
패턴화된 필드 주입을 간소화 -> 롬복 Lombok

**Lombok 라이브러리 적용**<br />

```gradle
//lombok 설정 추가
......

configurations {
    compileOnly {
        extendsFrom annotationProcessor
    }
}

dependencies {
    ......

    //lombok 라이브러리 추가
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
    testCompileOnly 'org.projectlombok:lombok'
    testAnnotationProcessor 'org.projectlombok:lombok'

    ......
}

......
```
- Preference -> Plugin -> lombok 설치 및 실행
- Preference -> Annotation Processors -> Enable annotation processing 체크

**기본 코드**<br />
```java
@Component
public class OrderServiceImpl implements OrderService {

    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

}
```

**롬복을 적용한 코드**<br />
```java
@Component
@RequiredArgsConstructor
public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;
}
```
- `@RequioredArgsConstructor` 기능을 사용하면 `final`이 붙은 필드를 모아서 생성자를 자동으로 만들어 줌

### 조회 빈이 2개 이상 - 문제

- `@Autowired`는 타입(type)으로 조회함
- 따라서 선택된 빈이 2개 이상일 때 문제가 발생함
    - 의존관계 자동 주입을 실행하면 `NoUniqueBeanDefinitionException` 에러 발생
    - 이 때 하위 타입으로 지정할 수도 있지만 하위 타입으로 지정하는 것은 DIP를 위반하고 유연성이 떨어짐

### @Autowired 필드 명, @Qualifier, @Primary

조회 대상 빈이 2개 이상일 때 해결방법<br />
- `@Autowired` 필드명 매칭
- `@Qualifier` -> `@Qualifier` 끼리 매칭 -> 빈 이름 매칭
- `@Primary` 사용

**@Autowired 필드명 매칭**<br />
`@Autowired`는 타입 매칭을 시도한 다음, 빈이 여러 개 있으면 필드 이름, 파라미터 이름으로 빈 이름을 매칭을 시도

```java
@Autowired
private DiscountPolicy discountPolicy
```

```java
@Autowired
private DiscountPolicy rateDiscountPolicy
```
- 필드명을 빈 이름으로 변경
- 필드명 매칭은 먼저 타입 매칭을 시도하고, 그 결과에 빈이 여러 개 있을 때 추가로 동작하는 기능

**@Qualifier 사용**<br />
빈 등록시 `@Qualifier` 추가 구분자를 붙임

```java
@Component
@Qualifier("mainDiscountPolicy")
public class RateDiscountPolicy implements DiscountPolicy {}
```

```java
@Component
@Qualifier("fixDiscountPolicy")
public class FixDiscountPolicy implements DiscountPolicy {}
```

의존관계 주입시 `@Qualifier`를 붙여주고 등록한 이름을 적어줌

```java
@Autowired
public OrderServiceImpl(MemberRepository memberRepository, @Qualifier("mainDiscountPolicy") DiscountPolicy discountPolicy) {
    this.memberRepository = memberRepository;
    this.discountPolicy = discountPolicy;
}
```

```java
@Autowired
public DiscountPolicy setDiscountPolicy(@Qualifier("mainDiscountPolicy") DiscountPolicy discountPolicy) {
    return discountPolicy;
}
```
- `@Qualifier`로 주입할 때 해당 이름을 갖는 Qualifier를 찾지 못한다면, 해당 이름을 갖는 스프링 빈을 추가로 탐색
    - `@Qualifier`는 `@Qualifier`를 찾는 용도로만 사용하는 것이 좋음

**@Primary 사용**<br />
`@Primary`는 우선순위를 정하는 방법<br />

```java
@Component
@Primary
public class RateDiscountPolicy implements DiscountPolicy {}

@Component
public class FixDiscountPolicy implements DiscountPolicy {}
```

```java
@Autowired
public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
    this.memberRepository = memberRepository;
    this.discountPolicy = discountPolicy;
}

@Autowired
public DiscountPolicy setDiscountPolicy(DiscountPolicy discountPolicy) {
    return discountPolicy;
}
```

**@Primary, @Qualifier 활용**<br />
- 메인 데이터베이스의 커넥션을 획득하는 스프링 빈은 `@Primary`를 적용해서 조회하는 곳에서 `@Qualifier` 지정 없이 편리하게 조회 가능
- 서브 데이터베이스 커넥션 빈을 획득할 때는 `@Qualifier`를 지정해서 명시적으로 획득 하는 방식으로 사용하면 코드를 깔끔하게 유지할 수 있음

우선순위<br />
- `@Qualifier`가 `@Primary`보다 우선순위가 높음
    - 스프링은 자동보다는 수동, 넓은 범위의 선택권보다는 좁은 범위의 선택권이 우선 순위가 높음

### 애노테이션 직접 만들기

`@Qualifier("mainDiscountPolicy")` 처럼 문자를 적으면 컴파일시 타입 체크가 안됨<br />
다음과 같이 애노테이션을 만들어서 문제를 해결할 수 있다.

```java
@Target({ElementType.FIELD, ElementType.METHOD, ElementType.PARAMETER, ElementType.TYPE, ElementType.ANNOTATION_TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Inherited
@Documented
@Qualifier("mainDiscountPolicy")
public @interface MainDiscountPolicy {
}
```

```java
@Component
@MainDiscountPolicy
public class RateDiscountPolicy implements DiscountPolicy{
    ......
}
```

```java
@Component
public class OrderServiceImpl implements OrderService{

    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    public OrderServiceImpl(MemberRepository memberRepository, @MainDiscountPolicy DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    ......

}
```
- 애노테이션에는 상속이라는 개념이 없음
    - 여러 애노테이션을 모아서 사용하는 기능은 스프링이 지원해주는 기능
- @Qualifier 뿐만 아니라 다른 애노테이션들도 함께 조합해서 사용할 수 있음
    - @Autowired도 재정의해서 사용할 수 있음
- 무분별한 재정의는 유지보수에 혼란을 주게 되니 유의

### 조회한 빈이 모두 필요할 때, List, Map

- 의도적으로 해당 타입의 스프링 빈이 모두 다 필요할 수 있음
    - 할인 서비스를 제공할 때, 클라이언트가 할인 방법을 선택할 수 있는 경우!!!

```java
public class AllBeanTest {

    @Test
    void findAllBean() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class, DiscountService.class);

        DiscountService discountService = ac.getBean(DiscountService.class);
        Member member = new Member(1L, "userA", Grade.VIP);
        int discountPrice = discountService.discount(member, 20000, "rateDiscountPolicy");

        assertThat(discountService).isInstanceOf(DiscountService.class);
        assertThat(discountPrice).isEqualTo(2000);
    }

    static class DiscountService {
        private final Map<String, DiscountPolicy> policyMap;
        private final List<DiscountPolicy> policies;

        @Autowired
        public DiscountService(Map<String, DiscountPolicy> policyMap, List<DiscountPolicy> policies) {
            this.policyMap = policyMap;
            this.policies = policies;
            System.out.println("policyMap = " + policyMap);
            System.out.println("polices = " + policies);
        }

        public int discount(Member member, int price, String discountCode) {
            DiscountPolicy discountPolicy = policyMap.get(discountCode);
            return discountPolicy.discount(member, price);
        }

    }

}
```

**로직 분석**<br />
- `DiscountService`는 `Map`으로 모든 `DiscountPolicy`를 주입받음
    - `Map`으로 `fixDiscountPolicy`, `rateDiscountPolicy`가 모두 주입됨
- `discount()` 메서드는 `discountCode`을 통해 스프링 빈을 찾아서 실행
    - "fixDiscountPolicy"가 넘어오면 `fixDiscountPolicy` 스프링 빈을 찾아서 실행
    - "rateDiscountPolicy"가 넘어오면 `rateDiscountPolicy` 스프링 빈을 찾아서 실행

**주입 분석**<br />
- `Map<String, DiscountPolicy>`: `Map`의 키에 스프링 빈의 이름을 넣어주고, 그 값으로 `DiscountPolicy` 타입으로 조회한 모든 스프링 빈을 담음
- `List<DiscountPolicy>`: `DiscountPolicy` 타입으로 조회한 모든 스프링 빈을 담음
- 만약 해당하는 타입의 스프링 빈이 없으면, 빈 컬렉션이나 `Map`을 주입함

### 자동, 수동의 올바른 실무 운영 기준

**자동 완성 기능을 기본으로 사용하자**<br />
- 스프링 출시 이후 점점 자동을 선호하는 추세
- 스프링은 `@Component`, `@Controller`, `@Service`, `@Repository`처럼 계층에 맞춰 애플리케이션 로직을 자동으로 스캔할 수 있도록 지원함
- 최근 스프링 부트는 컴포넌트 스캔을 기본으로 사용하고, 다양한 스프링 빈들도 조건이 맞으면 자동으로 등록되도록 설계
- 설정 정보를 기반으로 애플리케이션을 구성하는 부분과 실제 동작하는 부분을 명확하게 나누는 것이 이상적
- 그러나 `@Component`만으로 끝나는 스프링 빈 등록을 `@Configuration` 설정 정보에 가서 각각 `@Bean`을 적고, 객체를 생성하고 주입할 대상을 일일히 적어줄 필요는 없음
    - 관리할 빈이 많아지면 설정 정보를 관리하는 것 또한 부담이 됨
- 자동 빈 등록을 사용해도 OCP, DIP를 지킬 수 있음

**수동 빈 등록은 언제 사용하면 좋을까?**<br />
- 애플리케이션은 크게 업무 로직과 기술 지원 로직으로 나눌 수 있음
- 업무 로직 빈
    - 웹을 지원하는 컨트롤러, 핵심 비즈니스 로직이 있는 서비스, 데이터 계층의 로직을 처리하는 리포지토리 등
    - 보통 비즈니스 요구 사항을 개발할 때 추가되거나 변경됨
- 기술 지원 빈
    - 기술적인 문제나 공통 관심사(AOP)를 처리할 때 주로 사용
    - 데이터베이스 연결이나, 공통 로그 처리처럼 업무 로직을 지원하기 위한 하부 기술이나 공통 기술

- 업무 로직은 숫자도 많고, 컨트롤러, 서비스, 리포지토리처럼 어느정도 유사한 패턴이 있음
    - 자동 빈 등록 사용이 용이함
    - 문제가 발생해도 보통 어느 곳에서 문제가 발생했는지 명확하게 파악하기 쉬움
- 기술 지원 로직은 업무 로직과 비교해서 그 수가 적고, 애플리케이션 전반에 걸쳐 영향을 미치는 특징이 있음
    - 업무 로직과 달리 로직이 잘 적용되고 있는지 아닌지 파악하기 힘든 경우도 많음
    - 수동 빈 등록을 사용해 명확하게 하는 것이 좋음

애플리케이션 전반에 걸쳐 영향을 미치는 기술 지원 객체는 수동 빈으로 등록해서 설정 정보에 바로 나타나게 하는 것이 유지보수에 좋음

**비즈니스 로직 중에서 다형성을 적극 활용하는 경우**<br />
- 수동 빈 등록을 사용하거나, 자동으로 하는 경우특정 패키지에 같이 사용하는 것이 좋음
- 무엇을 사용하든 구조가 명확하게 이해되도록 설계해야 함

## 8. 빈 생명주기 콜백

### 빈 생명주기 콜백 시작

간단하게 외부 네트워크에 미리 연결하는 객체를 하나 생성한다고 가정해보자<br />

```java
public class NetworkClient {

    private String url;

    public NetworkClient() {
        System.out.println("생성자 호출, url = " + url);
        connect();
        call("초기화 연결 메시지");
    }

    public void setUrl(String url) {
        this.url = url;
    }

    // 서비스 시작시 호출
    public void connect() {
        System.out.println("connect: " + url);
    }

    public void call(String message) {
        System.out.println("call: " + url + " message = " + message);
    }

    // 서비스 종료시 호출
    public void disconnect() {
        System.out.println("close: " + url);
    }

}
```

```java
public class BeanLifeCycleTest {

    @Test
    public void lifeCycleTest() {
        ConfigurableApplicationContext ac = new AnnotationConfigApplicationContext(LifeCycleConfig.class);
        NetworkClient client = ac.getBean(NetworkClient.class);
        ac.close();
        /**
         * close는 ApplicationContext에서 지원하지 않음
         * AnnotationConfigApplicationContext 이나 ConfigurableApplicationContext 을 사용해야 함
         */
    }

    @Configuration
    static class LifeCycleConfig {

        @Bean
        public NetworkClient networkClient() {
            NetworkClient networkClient = new NetworkClient();
            networkClient.setUrl("http://hello-spring.dev");
            return networkClient;
        }

    }

}
```

실행해보면 다음과 같은 결과가 나온다

```bash
생성자 호출, url = null
connect: null
call: null message = 초기화 연결 메시지
```
- 생성자 부분을 보면 url 정보 없이 connect가 호출되고 있음
    - 객체를 생성하는 단계에는 url이 없고, 객체 생성 후 외부에서 수정자 주입을 통해 `setUrl()`이 호출되어야 url이 존재함

스프링 빈은 다음과 같은 라이프 사이클을 가짐<br />
> 객체 생성 → 의존관계 주입
- 스프링 빈은 객체를 생성하고, 의존관계 주입이 다 끝난 다음에야 필요한 데이터를 사용할 수 있는 준비가 완료됨
- 초기화 작업은 의존관계 주입이 모두 완료된 후 호출해야 함
- 스프링은 의존관계 주입이 완료되면 스프링 빈에게 콜백 메서드를 통해서 초기화 시점을 알려주는 다양한 기능을 제공
- 스프링은 스프링 컨테이너가 종료되기 직전에 소멸 콜백을 줌
    - 안전하게 종료 작업을 진행할 수 있음

**스프링 빈의 이벤트 라이프사이클**<br />
> 스프링 컨테이너 생성 → 스프링 빈 생성 → 의존관계 주입 → 초기화 콜백 → 사용 → 소멸 전 콜백 → 스프링 종료
- 초기화 콜백: 빈이 생성되고 빈의 의존 관계 주입이 완료된 후 호출
- 소멸 전 콜백: 빈이 소멸되기 직전에 호출

스프링은 다양한 방식으로 생명주기 콜백을 지원

> **객체의 생성과 초기화를 분리하라**<br />
생성자는 필수 정보(파라미터)를 받고 메모리를 할당해서 객체를 생성하는 책임을 가짐<br />
반면 초기화는 이렇게 생성된 값을 활용해서 외부 커넥션을 연결하는 등 무거운 동작을 수행<br />
따라서 생성자 안에서 무거운 초기화 작업을 함께 하는 것보다는 객체를 생성하는 부분과 초기화하는 부분을 명확하게 나누는 것이 유지보수 관점에서 좋음

> 싱글콘 빈들은 스프링 컨테이너가 종료될 때 싱글톤 빈들도 함께 종료되기 때문에 스프링 컨테이너가 종료되기 직전에 소멸 전 콜백이 일어남<br />
싱글톤처럼 컨테이너의 시작과 종료까지 생존하는 빈도 있지만 생명주기가 짧은 빈들도 있는데, 이 빈들은 컨테이너와 무관하게 해당 빈이 종료되기 직전에 소멸 전 콜백이 일어남

**스프링은 크게 3가지 방법으로 빈 생명주기 콜백을 지원함**<br />
- 인터페이스(`InitializingBean`, `DisposableBean`)
- 설정 정보에 초기화 메서드, 종료 메서드 지정
- `@PostConstruct`, `@PreDestroy` 애노테이션 지원

### 인터페이스 InitializingBean, DisposableBean

```java
public class NetworkClient implements InitializingBean, DisposableBean {

    private String url;

    public NetworkClient() {
        System.out.println("생성자 호출, url = " + url);
    }

    public void setUrl(String url) {
        this.url = url;
    }

    // 서비스 시작시 호출
    public void connect() {
        System.out.println("connect: " + url);
    }

    public void call(String message) {
        System.out.println("call: " + url + " message = " + message);
    }

    // 서비스 종료시 호출
    public void disconnect() {
        System.out.println("close: " + url);
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        System.out.println("NetworkClient.afterPropertiesSet");
        connect();
        call("초기화 연결 메시지");
    }

    @Override
    public void destroy() throws Exception {
        System.out.println("NetworkClient.destroy");
        disconnect();
    }
}
```
- `IntializingBean`은 `afterPropertiesSet()` 메서드로 초기화를 지원
- `DisposableBean`은 `distroy()` 메서드로 소멸을 지원

```bash
생성자 호출, url = null
NetworkClient.afterPropertiesSet
connect: http://hello-spring.dev
call: http://hello-spring.dev message = 초기화 연결 메시지
23:41:33.953 [main] DEBUG org.springframework.context.annotation.AnnotationConfigApplicationContext - Closing org.springframework.context.annotation.AnnotationConfigApplicationContext@14555e0a, started on Sun Feb 21 23:41:33 KST 2021
NetworkClient.destroy
close: http://hello-spring.dev
```
- 초기화 메서드가 주입 완료 후에 적절하게 호출됨
- 스프링 컨테이너의 종료가 호출되자 소멸 메서드 호출

**초기화, 소멸 인터페이스의 단점**<br />
- 코드가 스프링 전용 인터페이스에 의존
- 초기화, 소멸 메서드의 이름 변경이 불가능
- 코드를 고칠 수 없는 외부 라이브러리에는 적용 불가

> 인터페이스를 사용하는 초기화, 종료 방법은 스프링 초창기에 나온 방법<br />
현재는 거의 사용되지 않음

### 빈 등록 초기화, 소멸 메서드

설정 정보에 `@Bean(initMethod = "init", destroyMethod = "close")`처럼 초기화, 소멸 메서드를 지정할 수 있음

```java
public class NetworkClient {

    private String url;

    public NetworkClient() {
        System.out.println("생성자 호출, url = " + url);
    }

    public void setUrl(String url) {
        this.url = url;
    }

    // 서비스 시작시 호출
    public void connect() {
        System.out.println("connect: " + url);
    }

    public void call(String message) {
        System.out.println("call: " + url + " message = " + message);
    }

    // 서비스 종료시 호출
    public void disconnect() {
        System.out.println("close: " + url);
    }

    public void init() {
        System.out.println("NetworkClient.init");
        connect();
        call("초기화 연결 메시지");
    }

    public void close() {
        System.out.println("NetworkClient.close");
        disconnect();
    }
    
}
```

```java
ublic class BeanLifeCycleTest {

    @Test
    public void lifeCycleTest() {
        ConfigurableApplicationContext ac = new AnnotationConfigApplicationContext(LifeCycleConfig.class);
        NetworkClient client = ac.getBean(NetworkClient.class);
        ac.close();
        /**
         * close는 ApplicationContext에서 지원하지 않음
         * AnnotationConfigApplicationContext 이나 ConfigurableApplicationContext 을 사용해야 함
         */
    }

    @Configuration
    static class LifeCycleConfig {

        @Bean(initMethod = "init", destroyMethod = "close")
        public NetworkClient networkClient() {
            NetworkClient networkClient = new NetworkClient();
            networkClient.setUrl("http://hello-spring.dev");
            return networkClient;
        }

    }

}
```

**설정 정보 사용 특징**<br />
- 메서드 이름을 자유롭게 줄 수 있음
- 스프링 비닝 스프링 코드에 의존하지 않음
- 설정 정보를 사용하기 때문에 코드를 고칠 수 없는 외부 라이브러리에도 초기화, 종료 메서드를 적용할 수 있음

**종료 메서드 추론**<br />
- 라이브러리는 대부분 `close`, `shutdown`이라는 이름의 종료 메서드를 사용
- 따라서 `@Bean`의 `destroyMethod`는 기본값이 `(inferred)`으로 등록되어 있음
    - 추론 기능은 `close`, `shutdown`이라는 이름의 메서드를 자동으로 호출
    - 이름 그대로 종료 메서드를 추론해서 호출
- 따라서 직접 스프링 빈으로 등록하면 종료 메서드는 따로 적어주지 않아도 잘 동작함
- 추론 기능을 사용하지 않는다면 `distroyMethod=""`처럼 빈 공백으로 지정

### 애노테이션 @PostConstruct, @PreDestroy

```java
public class NetworkClient {

    private String url;

    public NetworkClient() {
        System.out.println("생성자 호출, url = " + url);
    }

    public void setUrl(String url) {
        this.url = url;
    }

    // 서비스 시작시 호출
    public void connect() {
        System.out.println("connect: " + url);
    }

    public void call(String message) {
        System.out.println("call: " + url + " message = " + message);
    }

    // 서비스 종료시 호출
    public void disconnect() {
        System.out.println("close: " + url);
    }

    @PostConstruct
    public void init() {
        System.out.println("NetworkClient.init");
        connect();
        call("초기화 연결 메시지");
    }

    @PreDestroy
    public void close() {
        System.out.println("NetworkClient.close");
        disconnect();
    }

}
```

```java
public class BeanLifeCycleTest {

    @Test
    public void lifeCycleTest() {
        ConfigurableApplicationContext ac = new AnnotationConfigApplicationContext(LifeCycleConfig.class);
        NetworkClient client = ac.getBean(NetworkClient.class);
        ac.close();
        /**
         * close는 ApplicationContext에서 지원하지 않음
         * AnnotationConfigApplicationContext 이나 ConfigurableApplicationContext 을 사용해야 함
         */
    }

    @Configuration
    static class LifeCycleConfig {

        @Bean
        public NetworkClient networkClient() {
            NetworkClient networkClient = new NetworkClient();
            networkClient.setUrl("http://hello-spring.dev");
            return networkClient;
        }

    }

}
```
- `@PostConstruct`, `@PreDestroy` 이 두 애노테이션을 사용하면 가장 편리하게 초기화와 종료를 실행할 수 있음

**`@PostConstruct`, `@PreDestory` 애노테이션 특징**<br />
- 최신 스프링에서 가장 권장하는 방법
    - 애노테이션 하나만 붙이면 되므로 매우 편리함
- 스프링에 종속적인 기술이 아님
    - `javax.annotation.PostConstruct` 패키지
    - JSR-250 이라는 자바 표준
    - 스프링이 아닌 다른 컨테이너에서도 동작
- 컴포넌트 스캔과 잘 어울림
- 코드를 고칠 수 없는 외부 라이브러리에는 적용할 수 없음
    - 이 경우 `@Bean`의 `initMethod`와 `destroyMethod` 사용 권장

## 9. 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 문제점

### 빈 스코프란?

- 스프링 빈은 기본적으로 스프링 컨테이너의 시작화 함께 생성되어 스프링 컨테이너가 종료될 때까지 유지됨
    - 스프링 빈이 기본적으로 **싱글톤 스코프**로 생성되기 때문

**스프링은 다음과 같은 다양한 스코프를 지원함**<br />
- 싱글톤: 기본 스코프. 스프링 컨테이너의 시작부터 종료까지 유지되는 가장 넓은 범위의 스코프
- 프로토타입: 스프링 컨테이너는 프로토타입 빈의 생성과 의존관계 주입까지만 관여하고, 더는 관리하지 않는 매우 짧은 범위의 스코프
- 웹 관련 스코프
    - request: 웹 요청이 들어오고 나갈 때까지 유지되는 스코프
    - session: 웹 세션이 생성되고 종료될 때까지 유지되는 스코프
    - application: 웹의 서븛릿 컨텍스와 같은 범위로 유지되는 스코프

**컴포넌트 스캔 자동 등록**<br />
```java
@Scope("prototype")
@Component
public class HelloBean {}
```

**컴포넌트 스캔 수동 등록**<br />
```java
@Scope("prototype")
@Bean
PrototypeBean HelloBean() {
    return new HelloBean();
}
```

### 프로토타입 스코프

- 싱글톤 스코프의 빈을 조회하면 스프링 컨테이너는 항상 같은 인스턴스의 스프링 빈을 반환
- 프로토타입 스코프를 스프링 컨테이너에 조회하면 스프링 컨테이너는 항상 새로운 인스턴스를 생성해서 반환

**싱글톤 빈 요청**<br />
![SPRING#0034](/assets/images/spring-core/0034-request-singleton-bean.png)
- 싱글톤 스코프의 빈을 스프링 컨테이너에 요청
- 스프링 컨테이너는 본인이 관리하는 스프링 빈을 반환
- 이후 스프링 컨테이너에 같은 요청이 와도 같은 객체 인스턴스의 스프링 빈을 반환

**프로토타입 빈 요청**<br />
![SPRING#0035](/assets/images/spring-core/0035-request-prototype-bean-1.png)
- 프로토타입 스코프의 빈을 스프링 컨테이너에 요청
- 스프링 컨테이너는 이 시점에 프로토 타입 빈을 생성하고 필요한 의존관계를 주입

![SPRING#0036](/assets/images/spring-core/0036-request-prototype-bean-2.png)
- 스프링 컨테이너는 생성한 프로토타입 빈을 클라이언트에 반환
- 이후 스프링 컨테이너에 같은 요청이 오면 항상 새로운 프로토타립 빈을 생성해서 반환

**정리**<br />
> 스프링 컨테이너는 프로토타입 빈을 생성하고 의존관꼐 주입, 초기화까지만 처리함<br />
클라이언트에 빈을 반환한 후 스프링 컨테이너는 생성된 프로토타입 빈을 관리하지 않음<br />
프로토타입 빈을 관리할 책임은 프로토타입 빈을 받은 클라이언트에 있음<br />
따라서 `@PreDestroy`와 같은 종료 메서드가 호출되지 않음

**싱글톤 스코프 빈 테스트**

```java
public class SingletonTest {

    @Test
    void singletonBeanFind() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(SingletonBean.class);

        SingletonBean singletonBean1 = ac.getBean(SingletonBean.class);
        SingletonBean singletonBean2 = ac.getBean(SingletonBean.class);
        System.out.println("singletonBean1 = " + singletonBean1);
        System.out.println("singletonBean2 = " + singletonBean2);
        assertThat(singletonBean1).isSameAs(singletonBean2);

        ac.close();
    }

    @Scope("singleton")
    static class SingletonBean {

        @PostConstruct
        public void init() {
            System.out.println("SingletonBean.init");
        }

        @PreDestroy
        public void destroy() {
            System.out.println("SingletonBean.destroy");
        }

    }

}
```

```bash
SingletonBean.init
singletonBean1 = hello.core.scope.SingletonTest$SingletonBean@479ceda0
singletonBean2 = hello.core.scope.SingletonTest$SingletonBean@479ceda0
11:11:37.258 [main] DEBUG org.springframework.context.annotation.AnnotationConfigApplicationContext - Closing org.springframework.context.annotation.AnnotationConfigApplicationContext@7a419da4, started on Mon Feb 22 11:11:37 KST 2021
SingletonBean.destroy
```
- 빈 초기화 메서드를 실행하고
- 같은 인스턴스의 빈을 조회하고
- 종료 메서드까지 정상 호출된 것을 확인

**프로토타입 스코프 빈 테스트**

```java
public class PrototypeTest {

    @Test
    void prototypeBeanFind() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(PrototypeBean.class);
        System.out.println("find prototypeBean1");
        PrototypeBean prototypeBean1 = ac.getBean(PrototypeBean.class);
        System.out.println("find prototypeBean2");
        PrototypeBean prototypeBean2 = ac.getBean(PrototypeBean.class);
        System.out.println("prototypeBean1 = " + prototypeBean1);
        System.out.println("prototypeBean2 = " + prototypeBean2);
        assertThat(prototypeBean1).isNotSameAs(prototypeBean2);

        ac.close();
    }

    @Scope("prototype")
    static class PrototypeBean {

        @PostConstruct
        public void init() {
            System.out.println("PrototypeBean.init");
        }

        @PreDestroy
        public void destroy() {
            System.out.println("PrototypeBean.destroy");
        }

    }

}
```

```bash
find prototypeBean1
PrototypeBean.init
find prototypeBean2
PrototypeBean.init
prototypeBean1 = hello.core.scope.PrototypeTest$PrototypeBean@479ceda0
prototypeBean2 = hello.core.scope.PrototypeTest$PrototypeBean@6d07a63d
11:12:31.734 [main] DEBUG org.springframework.context.annotation.AnnotationConfigApplicationContext - Closing org.springframework.context.annotation.AnnotationConfigApplicationContext@7a419da4, started on Mon Feb 22 11:12:31 KST 2021
```
- 싱글톤 빈은 스프링 컨테이너 생성 시점에 초기화 메서드가 실행되지만, 프로토타입 스코프의 빈은 스프링 컨테이너에서 빈을 조회할 때 생성되고, 초기화 메서드도 실행됨
    - 싱글톤 빈은 스프링 컨테이너가 관리하기 때문에 스프링 컨테이너가 종료될 때 빈의 종료 메서드가 실행됨
- 프로토타입 빈을 두 번 조회했으므로 완전히 다른 스프링 빈이 생성되고, 초기화도 두 번 실행됨
    - 프로토타입 빈은 스프링 컨테이너가 생성과 의존관계 주입, 초기화까지만 관여하고 더는 관리하지 않음
    - 프로토타입 빈은 스프링 컨테이너가 종료될 때 `@PreDestory` 같은 종료 메서드가 전혀 실행되지 않음
        - 종료 메서드 호출도 클라이언트가 직접 해야함

### 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 문제점

프로토타입 스코프의 빈을 요청하면 항상 새로운 객체 인스턴스를 생성해서 반환하지만, 싱글톤 빈과 함께 사용할 때는 의도한대로 잘 동작하지 않음

**프로토타입 빈 직접 요청**

![SPRING#0037](/assets/images/spring-core/0037-request-prototype-direct-1.png)
- 클라이언트 A는 스프링 컨테이너에 프로토타입 빈을 요청
- 스프링 컨테이너는 프로토타입 빈을 새로 생성해서 반환
    - count = 0
- 클라이언트는 조회한 프로토타입 빈에 `addCount()`를 호출하면서 count 필드에 1을 더함
    - count = 1

![SPRING#0038](/assets/images/spring-core/0038-request-prototype-direct-2.png)
- 클라이언트 B는 스프링 컨테이너에 프로토타입 빈을 요청
- 스프링 컨테이너는 프로토타입 빈을 새로 생성해서 반환
    - count = 0
- 클라이언트는 조회한 프로토타입 빈에 `addCount()`를 호출하면서 count 필드에 1을 더함
    - count = 1

```java
public class SingletonWithPrototypeTest {

    @Test
    void prototypeFind() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(PrototypeBean.class);
        PrototypeBean prototypeBean1 = ac.getBean(PrototypeBean.class);
        prototypeBean1.addCount();
        assertThat(prototypeBean1.getCount()).isEqualTo(1);

        PrototypeBean prototypeBean2 = ac.getBean(PrototypeBean.class);
        prototypeBean2.addCount();
        assertThat(prototypeBean2.getCount()).isEqualTo(1);
    }

    @Scope("prototype")
    static class PrototypeBean {

        private int count = 0;

        public void addCount() {
            count++;
        }

        public int getCount() {
            return count;
        }

        @PostConstruct
        public void init() {
            System.out.println("PrototypeBean.init " + this);
        }

        @PreDestroy
        public void destroy() {
            System.out.println("PrototypeBean.destroy");
        }

    }

}
```

```bash
PrototypeBean.init hello.core.scope.SingletonWithPrototypeTest$PrototypeBean@6d07a63d
PrototypeBean.init hello.core.scope.SingletonWithPrototypeTest$PrototypeBean@602e0143
```

**싱글톤 빈에서 프로토타입 빈 사용**

![SPRING#0039](/assets/images/spring-core/0039-singleton-prototype-1.png)
- `ClientBean`은 싱글톤이므로 스프링 컨테이너 생성 시점에 함께 생성되고 의존관계 주입도 발생
- `ClientBean`은 의존관계 자동 주입을 사용
    - 주입 시점에 스프링 컨테이너에 프로토타입 빈을 요청
    - 스프링 컨테이너는 프로토타입 빈을 생성해서 `ClientBean`에 반환
        - count = 0
- `ClientBean`은 프로토타입 빈을 내부 필드에 보관
    - 정확하게는 참조값을 보관

![SPRING#0040](/assets/images/spring-core/0040-singleton-prototype-2.png)
- 클라이언트 A는 `ClientBean`을 스프링 컨테이너에 요청해서 받음
    - 싱글톤이므로 항상 같은 `ClientBean`이 반환
- 클라이언트 A는 `clientBean.logic()`을 호출
- `clientBean`은 `prototypeBean`의 `addCount()`를 호출해서 프로토타입 빈의 count를 증가
    - count = 1

![SPRING#0041](/assets/images/spring-core/0041-singleton-prototype-3.png)
- 클라이언트 B는 `ClientBean`을 스프링 컨테이너에 요청해서 받음
    - 싱글톤이므로 항상 같은 `ClientBean`이 반환
    - clientBean이 내부에 가지고 있는 프로토타입 빈은 이미 과거에 주입이 끝난 빈임
        -  주입 시점에 스프링 컨테이너에 요청해서 프로토타입 빈이 새로 생성이 된 것이지, 사용 할 때마다 새로 생성되는 것이 !!
- 클라이언트 B는 `clientBean.logic()`을 호출
- `clientBean`은 `prototypeBean`의 `addCount()`를 호출해서 프로토타입 빈의 count를 증가
    - count = 2

```java
public class SingletonWithPrototypeTest {

    @Test
    void singletonClientUsePrototype() {
        AnnotationConfigApplicationContext ac =
                new AnnotationConfigApplicationContext(ClientBean.class, PrototypeBean.class);
        ClientBean clientBean1 = ac.getBean(ClientBean.class);
        int count1 = clientBean1.logic();
        assertThat(count1).isEqualTo(1);

        ClientBean clientBean2 = ac.getBean(ClientBean.class);
        int count2 = clientBean1.logic();
        assertThat(count2).isEqualTo(2);
    }

    @Scope("singleton")
    static class ClientBean{

        private final PrototypeBean prototypeBean; // 생성 시점에 주입

        @Autowired
        public ClientBean(PrototypeBean prototypeBean) {
            this.prototypeBean = prototypeBean;
        }

        public int logic() {
            prototypeBean.addCount();
            int count = prototypeBean.getCount();
            return count;
        }

    }

    @Scope("prototype")
    static class PrototypeBean {

        private int count = 0;

        public void addCount() {
            count++;
        }

        public int getCount() {
            return count;
        }

        @PostConstruct
        public void init() {
            System.out.println("PrototypeBean.init " + this);
        }

        @PreDestroy
        public void destroy() {
            System.out.println("PrototypeBean.destroy");
        }

    }

}
```

```bash
PrototypeBean.init hello.core.scope.SingletonWithPrototypeTest$PrototypeBean@22356acd
11:31:56.881 [main] DEBUG org.springframework.beans.factory.support.DefaultListableBeanFactory - Autowiring by type from bean name 'singletonWithPrototypeTest.ClientBean' via constructor to bean named 'singletonWithPrototypeTest.PrototypeBean'
```
- 싱글톤 빈은 생성 시점에만 의존관계 주입을 받기 때문에, 프로토타입 빈이 새로 생성되기는 하지만 싱글톤 빈과 함께 계속 유지됨
    - 프로토타입 빈을 사용하는 이유는 사용할 때마다 새로 생성해서 사용하기 위함이기 때문에, 이는 사용자가 원하는 것이 아님

> : 여러 빈에서 같은 프로토타입 빈을 주입 받으면, 주입 받는 시점에 각각 새로운 프로토타입 빈이 생성<br />
예를 들어서 clientA, clientB가 각각 의존관계 주입을 받으면 각각 다른 인스턴스의 프로토타입 빈을 주입 받음<br />
clientA → prototypeBean@x01<br />
clientB → prototypeBean@x02<br />
물론 사용할 때 마다 새로 생성되는 것은 아님

### 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 Provider로 문제 해결

**스프링 컨테이너에 요청**<br />
가장 간단한 방법은 싱글톤 빈이 프로토타입을 사용할 때마다 스프링 컨테이너에 새로 요청하는 방법

```java
public class SingletonWithPrototypeTest {

    ......

    @Scope("singleton")
    static class ClientBean{

        @Autowired
        private ApplicationContext ac;

        public int logic() {
            PrototypeBean prototypeBean = ac.getBean(PrototypeBean.class);
            prototypeBean.addCount();
            int count = prototypeBean.getCount();
            return count;
        }

    }

    ......

}
```
- `ac.getBean()`을 통해서 항상 새로운 프로토타입 빈이 생성
- 의존관계를 외부에서 주입(DI) 받는게 아니라 이렇게 직접 필요한 의존관계를 찾는 것을 Dependency Lookup(DL), 의존관계 조회(탐색)이라 함
- 이렇게 스프링의 애플리케이션 컨텍스트 전체를 주입받으면, 스프링 컨테이너에 종속적인 코드가 되고 단위 테스트도 어려워짐

필요한 기능은 지정한 프로토타입 빈을 컨테이너에서 대신 찾아주는 DL 정도의 기능

**ObjectFactory, ObjectProvider**<br />
지정한 빈을 컨테이너에서 대신 찾아주는 DL 서비스를 제공하는 것이 `ObjectProvider`<br />
과거 `ObjectFactory`에서 편의 기능을 추가한 것이 `ObjectProvider`

```java
public class SingletonWithPrototypeTest {

    ......

    @Scope("singleton")
    static class ClientBean{

        @Autowired
        private ObjectProvider<PrototypeBean> prototypeBeanProvider;

        public int logic() {
            PrototypeBean prototypeBean = prototypeBeanProvider.getObject();
            prototypeBean.addCount();
            int count = prototypeBean.getCount();
            return count;
        }

    }

    ......

}
```
- `prototypeBeanProvider.getObject()`을 통해 항상 새로운 프로토타입 빈이 생성
- `ObjectProvider`의 `getObject()`를 호출하면 내부에서는 스프링 컨테이너를 통해 해당 빈을 찾아서 반환 (DL)
- 스프링의 기능을 사용하지만, 기능이 단순하므로 단위테스트를 만들거나 mock 코드를 만들기는 훨씬 쉬움

- ObjectFactory: 기능 단순. 별도의 라이브러리 필요 없음. 스프링에 의존
- ObjectProvider: ObjectFactory 상속. 옵션, 스트림 처리 등 편의 기능이 많고, 별도의 라이브러리 필요 없음. 스프링에 의존

**JSR-330 Provider**<br />
`javax.inject.Provider`라는 JSR-330 자바 표준을 사용<br />
사용에 앞서 `javax.inject:javax.inject:1` 라이브러리를 gradle에 추가해야 함

```gradle
......

dependencies {
    ......	

	implementation 'javax.inject:javax.inject:1'

    ......

	}
}

......
```

```java
public class SingletonWithPrototypeTest {
    ......

    @Scope("singleton")
    static class ClientBean{

        @Autowired
        private Provider<PrototypeBean> prototypeBeanProvider;

        public int logic() {
            PrototypeBean prototypeBean = prototypeBeanProvider.get();
            prototypeBean.addCount();
            int count = prototypeBean.getCount();
            return count;
        }

    }

    ......
}
```
- `provider.get()` 을 통해서 항상 새로운 프로토타입 빈이 생성
- `provider`의 `get()` 을 호출하면 내부에서는 스프링 컨테이너를 통해 해당 빈을 찾아서 반환 (DL)
- 자바 표준이고, 기능이 단순하므로 단위테스트를 만들거나 mock 코드를 만들기는 훨씬 쉬움

- `get()` 메서드 하나로 기능이 매우 단순함
- 별도의 라이브러리가 필요
- 자바 표준이므로 스프링이 아닌 다른 컨테이너에서도 사용할 수 있음

**정리**<br />
- 프로토타입 빈은 매번 사용할 때 마다 의존관계 주입이 완료된 새로운 객체가 필요할 경우 사용
    - 실무에서 웹 애플리케이션을 개발해보면 싱글톤 빈으로 대부분의 문제를 해결할 수 있기 때문에, 프로토타입 빈을 직접적으로 사용하는 일은 매우 드뭄
- ObjectProvider , JSR330 Provider 등은 프로토타입 뿐만 아니라 DL이 필요한 경우는 언제든지 사용할 수 있음

>`@Lookup` 애노테이션을 사용하는 방법은 생략

> JSR-330 Provider을 사용해야 하는가, 아니면 스프링이 제공하는 ObjectProvider를 사용해야 하는가?<br />
ObjectProvider는 DL을 위한 편의 기능을 많이 제공해주고 스프링 외에 별도의 의존관계 추가가 필요없기 때문에 편리함<br />
만약 코드를 스프링이 아닌 다른 컨테이너에서도 사용할 수 있어야 한다면, JSR-330 Provider를 사용해야 함

> 스프링과 자바 표준이 제공하는 기능이 겹칠 경우, 스프링이 대개 더 다양하고 편리한 기능을 제공해주므로 다른 컨테이너를 사용할 일이 없다면 스프링이 제공하는 기능을 사용

### 웹 스코프

**웹 스코프의 특징**<br />
- 웹 스코프는 웹 환경에서만 동작
- 웹 스코프는 프로토타입과 다르게 스프링이 해당 스코프의 종료 시점까지 관리
    - 따라서 종료 메서드가 호출됨

**웹 스코프의 종류**<br />
- request
    - HTTP 요청 하나가 들어오고 나갈 때까지 유지되는 스코프.
    - 각각의 HTTP 요청마다 별도의 빈 인스턴스가 생성되고 관리됨
- session: HTTP Session과 동일한 생명주기를 갖는 스코프
- application: 서블릿 컨텍스트(`ServletContext`)와 동일한 생명주기를 갖는 스코프
- websocket: 웹 소켓과 동일한 생명주기를 갖는 스코프

HTTP request 요청 당 각각 할당되는 request 스코프<br />
![SPRING#0042](/assets/images/spring-core/0042-web-scope.png)

### request 스코프 예제 만들기

웹 스코프는 웹 환경에서만 동작하므로 웹 환경이 동작하도록 라이브러리 추가

```gradle
dependencies {
	......

	// Web 라이브러리 추기
	implementation 'org.springframework.boot:spring-boot-starter-web'

    ......
}
```
- `hello.core.CoreApplication`의 main 메서드를 실행하면 웹 애플리케이션이 실행됨
    - `spring-boot-starter-web` 라이브러리를 추가하면 스프링 부트는 내장 톰켓 서버를 활용해서 웹 서버와 스프링을 함께 실행
- 스프링 부트는 웹 라이브러리가 없으면 `AnnotationConfigApplicationContext`을 기반으로 애플리케이션을 구동
- 웹 라이브러리가 추가되면 웹과 관련된 추가 설정과 환경이 필요하므로 `AnnotationConfigServletWebServerApplicationContext`을 기반으로 애플리케이션 구동
- 만약 기본 포트인 8080 포트가 다른 곳에서 사용중이라면 "main/resources/application.properties" 파일을 수정

```properties
server.port=9090
```

**request 스코프 예제**<br />
다음과 같이 로그가 남도록 request 스코프를 활용해서 추가 기능을 개발

```bash
[d06b992f...] request scope bean create
[d06b992f...][http://localhost:8080/log-demo] controller test
[d06b992f...][http://localhost:8080/log-demo] service id = testId
[d06b992f...] request scope bean close
```
- [UUID][requestURL] {message}
    - UUID를 사용해서 HTTP 요청을 구분
    - requestURL 정보를 추가해 어떤 URL을 요청해서 남은 로그인지 확인

```java
@Component
@Scope(value = "request")
public class MyLogger {

    private String uuid;
    private String requestURL;

    public void setRequestURL(String requestURL) {
        this.requestURL = requestURL;
    }

    public void log(String message) {
        System.out.println("[" + uuid + "][" + requestURL + "] " + message);
    }

    @PostConstruct
    public void init() {
        uuid = UUID.randomUUID().toString();
        System.out.println("[" + uuid + "] request scope bean create: " + this);
    }

    @PreDestroy
    public void close() {
        System.out.println("[" + uuid + "] request scope bean close: " + this);
    }

}
```
- 로그 출력을 위한 MyLogger 클래스
- `@Scope(value = "request")`를 사용해서 request 스코프로 지정
    - 해당 빈은 HTTP 요청 당 하나씩 생성되고, HTTP 요청이 끝나는 시점에 소멸됨
- 빈이 생성되는 시점에 자동으로 `@PostConstruct` 초기화 메서드를 사용해서 uuid를 생성해서 저장
- 빈은 HTTP 요청 당 하나씩 생성되므로, uuid를 저장해두면 다른 HTTP 요청과 구분할 수 있음
- 빈이 소멸되는 시점에 `@PreDestroy`를 사용해서 종료 메시지를 남김
- `requestURL`은 이 빈이 생성되는 시점에는 알 수 없으므로, 외부에서 setter로 입력 받음

```java
@Controller
@RequiredArgsConstructor
public class LogDemoController {

    private final LogDemoService logDemoService;
    private final MyLogger myLogger;

    @RequestMapping("log-demo")
    @ResponseBody
    public String logDemo(HttpServletRequest request) {
        String requestURL = request.getRequestURL().toString();
        myLogger.setRequestURL(requestURL);

        myLogger.log("controller test");
        logDemoService.logic("testID");
        return "OK";
    }

}
```
- 로거가 잘 작동하는지 확인하는 테스트용 컨트롤러
- `HttpServletRequest`를 통해서 요청 URL을 받음
    - requestURL: `http://localhost:8080/log-demo`
- 수신한 requestURL 값을 myLogger에 저장
    - myLogger는 HTTP 요청 당 각각 구분되므로 다른 HTTP 요청 때문에 값이 섞이지 않음
- 컨트롤러에서 controller test라는 로그를 남김

> requestURL을 MyLogger에 저장하는 부분은 컨트롤러 보다는 공통 처리가 가능한 스프링 인터셉터나 서블릿 필터 같은 곳을 활용하는 것이 좋음<br />
여기서는 단순한 예제를 통해 아직 스프링 인터셉터를 학습하지 않은 분들을 위해서 컨트롤러를 사용<br />
스프링 웹에 익숙하다면 인터셉터를 사용해서 구현해보자

```java
@Service
@RequiredArgsConstructor
public class LogDemoService {

    private final MyLogger myLogger;

    public void logic(String id) {
        myLogger.log("service id = " + id);
    }
}
```
- 비즈니스 로직이 있는 서비스 계층에서도 로그를 출력
    - request scope를 사용하지 않고 파라미터로 이 모든 정보를 서비스 계층에 넘긴다면, 파라미터가 많아서 지저분해짐
    - requestURL 같은 웹과 관련된 정보가 웹과 관련없는 서비스 계층으로 넘어감
    - 웹과 관련된 부분은 컨트롤러까지만 사용해야 함
    - 서비스 계층은 웹 기술에 종속되지 않고, 가급적 순수하게 유지하는 것이 유지보수 관점에서 좋음
- request scope의 MyLogger 덕분에 웹과 관련젱 정보를 파라미터로 넘기지 않고, MyLogger의 멤버변수에 저장해서 코드와 계층을 깔끔하게 유지할 수 있음

request 스코프 빈은 실제 요청이 들어와야 빈을 생성할 수 있으므로, 현재 애플리케이션은 실행시 오류 발생

### 스코프와 Provider

Provider를 사용해 오류를 간단히 해결할 수 있음

```java
@Controller
@RequiredArgsConstructor
public class LogDemoController {

    private final LogDemoService logDemoService;
    private final ObjectProvider<MyLogger> myLoggerProvider;

    @RequestMapping("log-demo")
    @ResponseBody
    public String logDemo(HttpServletRequest request) {
        String requestURL = request.getRequestURL().toString();
        MyLogger myLogger = myLoggerProvider.getObject();
        myLogger.setRequestURL(requestURL);

        myLogger.log("controller test");
        logDemoService.logic("testID");
        return "OK";
    }

}
```

```java
@Service
@RequiredArgsConstructor
public class LogDemoService {

    private final ObjectProvider<MyLogger> myLoggerProvider;

    public void logic(String id) {
        MyLogger myLogger = myLoggerProvider.getObject();
        myLogger.log("service id = " + id);
    }
}
```

main() 메서드로 스프링을 실행하고, 웹 브라우저에 http://localhost:8080/log-demo 를 입력하면 정상적으로 동작함

```bash
[23890fe7-b44a-4e63-aa29-6f6d0a158dc9] request scope bean create: hello.core.common.MyLogger@c4b5173
[23890fe7-b44a-4e63-aa29-6f6d0a158dc9][http://localhost:8080/log-demo] controller test
[23890fe7-b44a-4e63-aa29-6f6d0a158dc9][http://localhost:8080/log-demo] service id = testID
[23890fe7-b44a-4e63-aa29-6f6d0a158dc9] request scope bean close: hello.core.common.MyLogger@c4b5173
```

- `ObjectProvider` 덕분에 `ObjectProvider.getObject()`를 호출하는 시점까지 request scope 빈의 생성을 지연할 수 있음
- `ObjectProvider.getObject()`를 호출하시는 시점에는 HTTP 요청이 진행중이므로 request scope 빈의 생성이 정상 처리됨
- `ObjectProvider.getObject()`를 `LogDemoController`, `LogDemoService`에서 각각 한 번씩 따로 호출해도 같은 HTTP 요청이면 같은 스프링 빈이 반환됨

### 스코프와 프록시

```java
@Component
@Scope(value = "request", proxyMode = ScopedProxyMode.TARGET_CLASS)
public class MyLogger {

    private String uuid;
    private String requestURL;

    public void setRequestURL(String requestURL) {
        this.requestURL = requestURL;
    }

    public void log(String message) {
        System.out.println("[" + uuid + "][" + requestURL + "] " + message);
    }

    @PostConstruct
    public void init() {
        uuid = UUID.randomUUID().toString();
        System.out.println("[" + uuid + "] request scope bean create: " + this);
    }

    @PreDestroy
    public void close() {
        System.out.println("[" + uuid + "] request scope bean close: " + this);
    }

}
```
- Scope에 `proxyMode = ScopedProxyMode.TARGET_CLASS`를 추가
    - 적용 대상이 클래스면 `TARGET_CLASS`를 선택
    - 적용 대상이 인터페이스면 `INTERFACES`를 선택
- MyLogger의 가짜 프록시 클래스를 만들어두고 HTTP request와 상관 없이 가짜 프록시 클래스를 다른 빈에 미리 주입해 둘 수 있음

```java
@Controller
@RequiredArgsConstructor
public class LogDemoController {

    private final LogDemoService logDemoService;
    private final MyLogger myLogger;

    @RequestMapping("log-demo")
    @ResponseBody
    public String logDemo(HttpServletRequest request) {
        String requestURL = request.getRequestURL().toString();

        System.out.println("myLogger = " + myLogger.getClass());
        myLogger.setRequestURL(requestURL);

        myLogger.log("controller test");
        logDemoService.logic("testID");
        return "OK";
    }

}
```

```java
@Service
@RequiredArgsConstructor
public class LogDemoService {

    private final MyLogger myLogger;

    public void logic(String id) {
        myLogger.log("service id = " + id);
    }
}
```
- `LogDemoController`, `LogDemoService`는 `Provider` 사용 전과 완전히 동일함

**웹 스코프와 프록시 동작 원리**<br />
주입된 myLogger를 확인하자

```java
System.out.println("myLogger = " + myLogger.getClass());
```

```bash
myLogger = class hello.core.common.MyLogger$$EnhancerBySpringCGLIB$$e126e0cb
```

**CBLIB 라이브러리를 사용해 MyLogger 클래스에 가짜 프록시 객체를 만들어 주입함**<br />
- `@Scope`에 `proxyMode = ScopedProxyMode.TARGET_CLASS`를 설정하면 스프링 컨테이너는 CGLIB라는 바이트코드를 조작하는 라이브러리를 사용해서, MyLogger를 상속받은 가짜 프록시 객체를 생성함
- 따라서 우리가 등록한 순수한 MyLogger 클래스가 아니라 `MyLogger$$EnhancerBySpringCGLIB`이라는 클래스로 만들어진 객체가 대신 등록됨
    - 스프링 컨테이너에 "myLogger"라는 이름으로 이 가짜 프록시 객체를 등록
- `ac.getBean("myLogger", MyLogger.class)`로 조회해도 프록시 객체가 조회되는 것을 확인 가능
    - 의존관계 주입도 이 가짜 프록시 객체가 주입

![SPRING#0043](/assets/images/spring-core/0043-proxy.png)

**가짜 프록시 객체는 요청이 오면 그때 내부에서 진짜 빈을 요청하는 위임 로직이 들어있음**<br />
- 가짜 프록시 객체는 내부에 진짜 myLogger를 찾는 방법을 알고 있음
- 클라이언트가 `myLogger.logic()`을 호출하면 사실은 가짜 프록시 객체의 메서드를 호출한 것
- 가짜 프록시 객체는 request 스코프의 진짜 `myLogger.logic()`를 호출
- 가짜 프록시 객체는 원본 클래스를 상속 받아서 만들어졌기 때문에, 이 객체를 사용하는 클라이언트 입장에서는 사실 원본인지 아닌지 알 필요 없이 동일하게 사용할 수 있음 (다형성)

**동작 정리**<br />
- CGLIB라는 라이브러리로 내 클래스를 상속 받은 가짜 프록시 객체를 만들어서 주입
    - 이 가짜 프록시 객체는 실제 요청이 오면 그때 내부에서 실제 빈을 요청하는 위임 로직이 들어있음
- 가짜 프록시 객체는 실제 request scope와는 관계 없음
    - 그냥 가짜이고, 내부에 단순한 위임 로직만 있으며 싱글톤처럼 동작함

**특징 정리**<br />
- 프록시 객체 덕분에 클라이언트는 마치 싱글톤 빈을 사용하듯이 편리하게 request scope를 사용할 수 있음
- Provider를 사용하든, 프록시를 사용하든 핵심 아이디어는 **진짜 객체 조회를 꼭 필요한 시점까지 지연처리 하는 것**
- 단지 애노테이션 설정 변경만으로 원본 객체를 프록시 객체로 대체할 수 있음
    - 이것이 바로 다형성과 DI 컨테이너가 가진 큰 강점
- 웹 스코프가 아니어도 프록시를 사용할 수 있음

**주의점**<br />
- 싱글톤을 사용하는 것 같지만 다르게 동작하기 때문에 주의해서 사용해야 함
    - 이런 특별한 scope는 꼭 필요한 곳에만 최소화해서 사용하자
    - 무분별하게 사용하면 유지보수가 어려워진다

## 10. 다음으로