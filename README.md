# 🚀 FastAPI CI/CD with GitHub Actions + ArgoCD

이 프로젝트는 다음을 포함합니다:
- FastAPI 웹 서버 (image.png 표시)
- GitHub Actions 기반 CI
- ArgoCD 기반 GitOps 자동 배포
- 코드 푸시 → 이미지 변경 자동 반영

## 사용 방법
1. `image.png`를 변경하고 `git push`
2. GitHub Actions → Docker 이미지 빌드 및 push
3. K8s deployment.yaml 수정 → push
4. ArgoCD가 자동으로 배포
