# k8s-ops-platform
Kubernetes 기반 장애 감지 및 자동 복구 플랫폼 구축 프로젝트


# Kubernetes Operations Platform

## 프로젝트 개요

Flask 기반 웹 애플리케이션을 Docker로 컨테이너화하고 Kubernetes 환경에서 운영하기 위한 프로젝트입니다.

## 기술 스택

- Python (Flask)
- Docker
- Kubernetes
- GitHub
- Amazon ECR

## 현재 구현 완료

- Flask 웹 애플리케이션 개발
- Docker 이미지 생성
- Amazon ECR 업로드
- Kubernetes Deployment
- Kubernetes Service
- ReplicaSet 기반 Self-Healing 확인

## 향후 계획

- GitHub Actions 기반 CI/CD
- Amazon EKS 배포
- HPA(Auto Scaling)
- Prometheus + Grafana
- Alertmanager