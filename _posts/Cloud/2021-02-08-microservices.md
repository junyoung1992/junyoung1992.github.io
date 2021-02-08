---
title: "What is Microservices?"
tags: Microservices MSA
---

## 1. Microservices 소개

### What is Microservices?

하나의 어플리케이션을 다수의 독립적인 서비스들의 집합으로 구성하는 것<br>
- 각자 별도의 프로세스에서 실행되며
- HTTP API 같은 가벼운 매커니즘으로 통신하는 작은 애플리케이션
- 작은 서비스들은 각자의 비즈니스 기능을 담당하고
- 완전 자동화 된 절차에 따라 독립적으로 배포됨
- 각 서비스는 서로 다른 프로그래밍 언어나 서로 다른 데이터 저장 기술을 사용할 수 있음

**Microservices**라는 용어가 주로 사용됨
- Monolith to Microservices, Building Microservices, Microservices Pattern

### Microservices 출현

- 2005년 클라우드 컴퓨팅 컨퍼런스에서 Peter Rogers가 Micro Web Service 개념 발표
- 2011년 SW 아키텍처 워크샵에서 Microservice라는 용어 탄생
    - 본인들의 아키텍처 스타일을 표현하기 위한 단어로 사용
- 2012년 Microservices라는 용어로 변경
- 2014년 James Lewis와 Martin Fowler가 Microservices 정리
    - Microservices의 정의, 특징을 정리
    - 현재까지도 다양한 문서에서 거의 표준적인 정의처럼 사용
    - <https://martinfowler.com/articles/microservices.html>
- Microservices의 진정한 태동은 산업계에서 시작
    - Amazon, Netflix

### Microservices in Amazon

- 2001년까지 Amazon.comn은 Monolithic
- 빠르게 개발되는 코드가 운영에 배포되는데 오랜 시간이 걸림
- 시스템을 Decomposition하여 독립적인 서비스들의 집합으로 재설계
- Ref: AWS re:Invent 2015: DevOps at Amazon: A Look at Our Tools and Processes(DVO202)

Jeff Bazos's Mandate
- 모든 팀은 해당 팀의 기능 및 데이터를 Service Interface를 통해서만 노출해야 한다.
- 다른 팀의 기능/데이터를 사용하려면 Network를 통한 Service Interface를 호출해야 한다.
- Service Interface 기술을 상관하지 않겠다. (HTTP, Corba, etc.)
- 누구든 이것을 지키지 않으면 해고하겠다.

Deployments at Amazon.com
- 11.6: 평균적인 서비스 배포 간격(초)
- 1,079: 1시간에 최대 배포 수
- 10,000: 단일 배포를 받는 평균 호스트 개수
- 30,000: 단일 배포를 받는 최대 호스트 개수

고객들에게 개발, 신규 기능이 빠르게 전달됨
- 배포의 회수는 고객에게 주는 가치의 전달 속도

### Microservices in Netflix

- Netflix 초기에는 Monolithic 시스템으로 개발
- 2008년 데이터베이스 장애 -> 3일 간 모든 비즈니스가 정지
- Netflix는 모든 시스템을 AWS Cloud로 마이그레이션 하기로 결정
    - Big Bang이 아닌 단계적 마이그레이션 진행
    - 자연스럽게 시스템이 분할되고, Microservices 설계/구현
- 2009년에 시작한 시스템 재설계/구현이 2011년 완료
- Cloud로의 마이그레이션은 7년간 진행
- 2015년 기준 500개 이상의 Microservices로 구성

Netflix OSS
- Cloud 횐경 및 Microservices 전환 중 다양한 문제에 봉착
- 여러 문제들을 해결하기 위한 아키텍처 패턴 및 OSS 개발

### 국내 Microservices 사례

- PAYCO, 11번가, 삼성전자, 삼성SDS, GSSHOP, Coupang 등

## 2. Monolithic Architecture

### 전통적 개발 방법

- 전체 기능을 단일 코드베이스로 개발
- 대규모 단일 코드 베이스를 빌드/배포
- 단일 통합 데이터베이스 사용
- Monolithic System
    - Monolithic Architecture
    - Monolith
- Monolithic System Type이 존재

### Monolithic System 단점

- 스케일 아웃 시 전체 시스템을 확장해야 하는 비효율
- 빌드/배포 시간 오래 걸림
- 작은 수정에도 전체 시스템을 빌드/배포해야 함
- 하나의 버그에 전체 시스템이 실패할 수 있음
- 기능 간의 결합도가 일반적으로 높음
    - 다른 기능의 테이블에 직접 접근하기도 함
- 기능 변경 시 영향도 파악이 어려움
    - 코드 의존 관계
    - 데이터 의존 관계
- 결과적으로 운영 환경에 민첩하게 배포되기 어려움

### Monolithic System 장점

- 상대적으로 운영하기 용이
    - 코드 관리, 장애 관리, 로그 관리, 모니터링
- 내부 메소드를 호출하기 때문에 성능 문제 없음
    - MSA는 Network를 통한 Interface 호출
- 트랜잭션 관리 용이

### Monolithic System의 종류

**Single Monolithic System**
- 가장 일반적인 형태

**Modular Monolith System**
- 각 기능별로 모듈화 되어 있는 형태
    - Package, Multi-module project
- MSA의 좋은 대안이 될 수 있음
- Monolith의 가장 큰 문제는 기능 간 결합도, 코드 수정시 영향도
    - 결합도를 잘 다루면 유지보수성 높은 SW 가능 -> Modular Monolith
- 배포와 확장에 대한 이슈는 여전히 존재
- 데이터에 대한 이슈도 존재
    - 타 기능 데이터 직접 접근에 의한 결합도
- Modular Monolith의 장점을 취하기 위해서는 모듈 간의 결합도를 자주 관리해야 함

**Distributed Monolithic System**
- 분산된 Monolith
- 쪼갰다고 MSA가 아니다
- 쪼개진 서비스 간에 매우 강결합 된 형태
- 항상 같이 배포되는 형태
- Monolith와 분산 시스템의 단점이 모두 존재
    - Monolith의 단점
        - 영향도
        - 결합도
    - 분산 시스템의 단점
        - 네트워크를 통한 협력에 의한 성능 저하
        - 관리 어려움
- Microservices를 도입할 때 가장 경계해야 할 형태

**Monolith에 대한 오해**
- Monolith는 Legacy이다?
- Monolith는 피해야할 안티 패턴이다?
- Monolith는 모든 상황에서 Microservice로 분할되어야 한다?
- Monolith는 하나의 아키텍처 패턴일 뿐
- 많은 상황에서 충분히 좋은 역할을 함
- 관리 용이성, 트랜잭션, 성능 등 많은 장점이 있음

Monolith와 MSA는 Trade-off가 존재하니 적절한 선택이 필요

## 3. Microservices 장단점

### 왜 지금 MSA인가? - 비즈니스

- 비즈니스 환경이 점점 빠르게 급변
- 비즈니스가 IT 기술에 의존하는 케이스가 많음
- 민첩한 IT 기술 없이 비즈니스의 빠른 변화가 어려움

### 왜 지금 MSA인가? - 기술

- Cloud
- NoSQL
- Docker, Kubernetes & Ecosystem
- Netflix OSS
- 쌓여가는 사례 및 Best Practice

### MSA의 장점

- 빠른 Delivery
    - 각 서비스는 독립적으로 개발되고 느슨하게 결합
    - 서비스는 작기 때문에 코드 수정에 대한 영향 범위가 상대적으로 작음
        - 빠른 영향도 파악, 빠른 빌드, 빠른 테스트
    - 각 서비스들은 네트워크를 통한 Interface로 느슨히 결합됨
        - 서비스 간 자율적인 배포 가능 
- Polyglot Architecture 지원
    - 전통적인 개발 환경은 표준 기술을 만들고 모든 조직에 강제
    - 특정 Task에 가장 적절한 기술을 적용 가능
    - 각 서비스는 자신만의 고유한 언어/Framework 선택 가능
- 실험과 혁신 가능
    - 최근 비즈니스 상황에서는 기술의 혁신이 필수적
    - Monolith 환경에서는 단순한 기술 실험도 어려움
        - DB/Framework 변경은 물론 언어의 버전 업도 어려운 작업
        - 영향도와 비용의 문제
    - 마이크로서비스는 새로운 기술들을 쉽게 실험해볼 수 있음
        - 작은 코드 베이스
        - 서비스 간 느슨한 결합
- 탄력적이고 선택적인 확장
    - 작은 서비스 단위로 확장 가능
    - Monolith는 전체 Scale Out 필요 -> 비효율
    - 각 서비스는 코드 베이스가 작아 확장 비용이 상대적으로 저렴
- 대체 가능성
    - 언어/프레임워크를 완전히 새롭게 개발 가능
        - 또는 오픈소스/커머셜 솔루션으로 대체
    - 각 서비스는 작고 느슨하게 연결되어 있기 때문
    - 적절한 서비스의 크기
        - 완전히 새로 개발되는데 2주
        - 정답은 없음......
- 기술 부채의 경감
    - SW는 나이를 먹고 관리하지 않으면 기술 부채가 쌓임
    - Monolith는 강한 결합도 때문에 코드 수정이 어려움
    - Microservices는 서비스 크기가 작아 품질 관리에 용이
    - 품질 향상을 위한 코드 개선 시 영향도 작음
        - 지속적인 개선 작업 가능 -> 조직의 문화로 자리 잡을 수 있음

### MSA의 단점

- 컴퓨팅 자원의 사용이 Monolith보다 비효율적
    - 성능: 내부 호출보다 느림
    - 메모리: JVM 등 자원 중복 사용
- 운영 관리가 어려움
- 모니터링 대상 증가
- 배포 대상 서비스 증가 및 기술의 다변화
- 다양한 장애 상황 발생
- 단위 테스트, 컴포넌트 테스트 난이도 증가
- DB 트랜잭션 처리가 어려움
- 서비스 간 Polyglot Data Store 사용
- 분산 환경에서 트랜잭션이 어려움

## 4. Microservices 특징

**MSA의 특징**
- MSA의 일반적인 특징 by Martin Fowler
    - MSA를 채택한 조직을 관찰, 조사 후 공통적인 특징을 정리
    - 모든 MSA가 만족해야 할 필수 조건은 아님
    - <https://martinfowler.com/articles/microservices.html>
- 서비스를 통한 컴포넌트화
    - 컴포넌트를 어떻게 정의하고 어떻게 연결하느냐
    - MSA에서는 서비스 단위를 컴포넌트로 정의
        - 특정 비즈니스 기능을 담당
        - 독립적인 프로세스로 실행
        - 자율적으로 배포 가능
    - 서비스는 응집도 높게 설계되어야 함
    - 서비스 간에는 명확한 인터페이스를 제공하여 협력
- 비즈니스 역량에 따른 조직 구성
    - Conway의 법칙
        - 시스템을 설계하는 조직은 그 조직의 소통 구조를 닮은 아키텍처를 만듬
    - 조직의 구조가 시스템의 아키텍처에 영향을 줌
    - 서비스를 만들 수 있는 역량을 팀 내부에서 모두 갖추고 있음
        - 비즈스 영역별로 기획자, 디자이너, 개발잘, 테스터를 모두 갖춤
        - 팀 간 Loosely Coupled -> 전체 시스템도 Loosely Coupled: Conway의 법칙
- 프로젝트보다 제품에 집중
    - 기존에는 개발과 운영이 분리되어 있음
        - 프로잭트 개발이 끝나면, 소프트웨어는 운영 조직에 이관
    - MSA에서는 팀이 개발, 운영을 포함한 전체 라이프사이클을 책임짐
    - 팀원들이 자신들이 만드는 SW를 바라보는 시각이 전환됨
        - 고객과의 접점을 늘리고 피드백을 늘려나감
    - 단순히 기능의 집합을 개발하여 넘기는 것이 아닌
    - SW가 어떻게 고객에게 가치를 전달할 수 있을지 고민하는 계기
    - SW와 기업의 비즈니스와의 연관 관계를 인식
- 똑똑한 End Point, 단순한 Pipe
    - 도메인 로직은 각 서비스 내에 응집도 높게 유지
    - 각 서비스 간의 연결은 HTTP API, MQ 등 사용
- 분산된 거버넌스
    - 중앙에서 표준이나 절차의 준수를 강요하지 않음
    - 스스로 효율적인 방법론과 도구, 기술을 찾아 적용
        - 각 서비스에 가장 적합한 기술 적용
- 분산된 데이터 관리
    - Monolithic은 일반적으로 단일 통합 데이터베이스 사용
        - 트랜잭션 처리에 용이함
        - 서로 다른 기능이 테이블을 직접 접근하기도 함
    - MSA는 해당 서비스의 데이터를 각자 관리
        - 서비스는 서로 다른 데이터 저장 기숧을 사용 가능
            - Polyglot Persistence
        - 각 서비스는 API를 통해서만 다른 서비스의 데이터에 접근
        - 트랜잭션 처리의 어려움, 결과적 일관성 적용
- 인프라 자동화
    - 다수의 서비스와 인스턴스가 존재하는 환경에서는 자동화가 필수
    - 자동화된 테스팅
    - 자동화된 Continuous Integration
    - 자동화된 Continuous Deployment
- 장애 방지 설계
    - 특정 서비스의 장애는 항상 일어나고 다른 서비스로 전파됨
    - 일부 서비스 장애가 전체 시스템 장애로 전파되는 것을 막는 것이 핵심
    - 서비스에 이상 동작을 최대한 신속하게 알 수 있어야 함
    - 가능하면 자동으로 복구할 수 있도록 설계해야 함
    - 장애 발생이 고객에게 미치는 영향을 파악하는 것도 중요
    -  Netflix의 장애 유발 테스트
        - 카오스 멍키, 카오스 고릴라, 카오스 콩
    - Circuit Breaker 패턴
        - 일부 서비스의 장애가 전체 시스템 장애로 전파되지 않도록 막음