---
title: "스프링 핵심 원리 - 기본편"
tags: Java Spring Inflearn
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
- 레고 블럭을 조립하듯, 컴포넌트를 쉽고 유연하게 변경하면서 개발할 수 있는 방법 -> 다형성(Polymorphism)
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
- 클라이언트: 요청 -> 서버: 응답
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
    - 객체를 생성하고 연관 관계를 맺어주는 별도의 조립, 설정자가 필요 -> Spring 배우면서!!

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
    - 애플리케이션 로직으로 테스트를 하는 것은 좋은 방법이 아님 -> JUnit 테스트 활용
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

**주문 도메인 협력, 역할 책임**
![SPRING#0005](/assets/images/spring-core/0005-order-domain.png)
1. 주문 생성: 클라이언트는 주문 서비스에 주문 생성을 요청
1. 회원 조회: 할인을 위해 주문 서비스는 회원 저장소에서 회원을 조회
1. 할인 적용: 주문 서비스는 회원 등급에 따른 할인 여부를 할인 정책에 위임
1. 주문 결과 반환: 주문 서비스는 할인 결과를 포함한 주문 결과를 반환
    - DB에 저장하면 예제가 복잡해지므로 그냥 반환

**주문 도메인 전체**
![SPRING#0006](/assets/images/spring-core/0006-order-domain-all.png)
- 역할과 구현을 분리해서 자유롭게 객체를 조힙할 수 있도록 설계

**주문 도메인 클래스 다이어그램**
![SPRING#0007](/assets/images/spring-core/0007-order-class.png)

**주문 도메인 객체 다이어그램**
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

**RateDiscountPolicy**
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

**RateDiscountPolicy 테스트**
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

### AppConfig 리팩터링

### 새로운 구조와 할인 정책 적용

### 전체 흐름 정리

### 좋은 객체 지향 설계의 5가지 원칙의 적용

### IoC, DI, 그리고 컨테이너

### 스프링으로 전환하기

## 4. 스프링 컨테이너와 스프링 빈

### 스프링 컨테이너 생성

### 컨테이너에 등록된 모든 빈 조화

### 스프링 빈 조회 - 기본

### 스프링 빈 조회 - 동인한 타입이 둘 이상

### 스프링 빈 조회 - 상속 관계

### BeanFactory와 ApplicationContext

### 다양한 설정 형식 지원 - 자바 코드, XML

### 스프링 빈 설정 메타 정보 - BeanDefinition

## 5. 싱글톤 컨테이너

### 웹 애플리케이션과 싱글톤

### 싱글톤 패턴

### 싱글톤 컨테이너

### 싱글톤 방식의 주의점

### @Configuration과 싱글톤

### @Configuration과 바이트 코드 조작의 마법

## 6. 컴포넌트 스캔

### 컴포넌트 스캔과 의존 관계 자동 주입 시작하기

### 탐색 위치와 기본 스캔 대상

### 필터

### 중복 등록과 충돌

## 7. 의존관계 자동 주입

### 다양한 의존관계 주입 방법

### 옵션 처리

### 생성자 주입을 선택해라!

### 롬복과 최신 트랜드

### 조회 빈이 2개 이상 - 문제

### @Autowired 필드 명, @Qualifier, @Primary

### 애노테이션 직접 만들기

### 조회한 빈이 모두 필요할 때, List, Map

## 8. 빈 생명주기 콜백

### 빈 생명주기 콜백 시작

### 인터페이스 InitializingBean, DisposableBean

### 빈 등록 초기화, 소멸 메서드

### 애노테이션 @PostConstruct, @PreDestroy

## 9. 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 문제점

### 빈 스코프란?

### 프로토타입 스코프

### 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 문제점

### 프로토타입 스코프 - 싱글톤 빈과 함께 사용시 Provider로 문제 해결

### 웹 스코프

### request 스코프 예제 만들기

### 스코프와 Provider

### 스코프와 프록시

## 10. 다음으로