# pknu_raspberrypi_2023
라즈베리파이 학습 리포지토리

## Day 01/02
- 라즈베리파이 학습
	- 라즈베리파이 개요
	- 라즈비안 설치
		- Bullseye
	- 라즈비안 설정
		- 기본 업데이트 및 업그레이드
		- 한글 폰트 및 입력기
		- 스크린세이버, 와이파이 연결 끊김 해제
	- pi-apps 설치
		- Visual Studio Code 설치
		- Github Desktop 설치 및 설정
	- Visual Studio Code
		- Python 플러그인
	- 리눅스 기본
		- 리눅스 명령어 (대표 20여가지)

## Day 03
- 라즈베리파이 학습
	- 통신 설정
		- AnyDesk 실패
	- 리눅스 일반
		- 서비스 실행, 확인, 종료하는 명령어
			- systemctl [start|stop|status] 서비스명
		- MySQL DB
		- WebServer
	- Flask 기본

## Day 04
- 라즈베리파이 학습
	- PyQt5 설치
	- QtDesigner 설치 및 실행 확인
	- 하드웨어 제어(GPIO)
		- LED / RGB LED 출력

## Day 05
- 라즈베리파이 학습
	- pip install RPi.GPIO
	- 네트워크 셋팅 (VNC)
	- RGB LED / Button 클릭

## Day 06
- 라즈베리파이 학습
	- MQTT 통신
		- MQTT Broker IP, port 설정, 계정설정(옵션)
		- RPi <--> WPF
		- RPi 온습도 센터값 MQTT 전송
		- WPF 모터, LED 제어값 전송
		- RPi Python paho-mqtt 패키지
		- WPF C# M2Mqtt 패키지

## Day 07
- 라즈베리파이 학습
	- 파이카메라 v1.3 ov5647
	- OpenCV 4.7
	- 카메라 연동 QrCode

## Day 08
- 가상환경 만들기
	- python -m venv [가상환경 명]
	- source ./bin/activate
		- 가상환경에서 프로그램 실행하기
	- deactivate
		- 가상환경 종료하기
- 라즈베리파이 학습
	- 7-세그먼트 16진수 표현하기
 	- 버튼 클릭시 7-세그먼트 16진수 표현하기

## Day 09
- 라즈베리파이 학습
	- pwm
		- 펄스 폭 조절하여 전압을 제어하는 방법
	- Interrupt
 		- 1. 핀설정
     			- GPIO.add_event_detect(channel, GPIO.Mode)
        		- channel : Pin number
          		- GPIO.Mode : RISING or FALLING or BOTH   
     		  2. 콜백 함수 설정
         		- GPIO.add_event_callback(channel, function)
           		- channel : Pin number
             		- function : call back function 
         	  3. 하나의 인터럽트 사용시
               		- GPIO.add_event_detect(channel, GPIO.Mode, callback=my_callback)
