# 거상 AGF Codex 작업 지침

- 기존 AGF 파일과 이미지 원본은 절대 덮어쓰지 않는다.
- AGF 바이너리 포맷을 검증하기 전에는 직접 AGF를 생성하거나 수정했다고 주장하지 않는다.
- PNG/GIF 프레임 처리와 AGF Studio 편집은 별개의 단계로 취급한다.
- 프레임 순서, 크기, 기준점, 알파 채널, 애니메이션 재생 속도를 확인한다.
- 결과물은 data/output/에, 원본은 data/original/에 둔다. 두 경로 모두 Git 추적에서 제외한다.
- Windows 로컬의 AGF Studio는 사용자가 별도로 설치해야 한다.
- Linux 클라우드에서는 Windows 전용 AGF Studio가 동작한다고 가정하지 않는다.
- 스프라이트 축소에는 기본적으로 nearest-neighbor 보간을 사용하고, 잘림/흐릿함/흔들림을 확인한다.
