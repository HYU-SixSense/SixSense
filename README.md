# BlindHelper

MadCamp Week4 1분반 

- 시각 장애인들이 현재 사용하고 있는 프로그램은 이미지를 설명할 때 이미지의 대체 텍스트(alt)를 설명한다. 심지어 일반인들이 구매하기에 꽤 비싼 가격이다.
- 이 대체 텍스트는 제대로 되어 있지 않은 웹페이지가 많고, 웹이 아닌 곳에서는 이미지를 읽어올 수 없다는 단점이 있다.
- 이 단점을 보완하기 위해 구글 클라우드의 이미지 분석 api를 사용하여 이미지 자체를 분석하여 설명해주는 프로그램을 기획하였다.
- 시각 장애인의 90%는 색깔을 구분할 수 있고 노란색을 가장 잘 보기 때문에 웹과 실행파일 gui를 만들 때 노란색을 주로 사용하였다.
- 이 프로그램은 시각 장애 중 시력 및 시야 장애를 가진 분들을 타겟으로 하였고, 인터넷을 사용할 때 특정 부분에 대한 설명을 해줄 수 있도록 구성하였다.

## 1. 개발 팀원

- 김수환 - KAIST 전산학부(수리과학과) 22학번
- 이형진 - KAIST 전산학부 22학번

## 2. 개발환경

- Language: Python
- Server: Flask
- DataBase: MongoDB
- IDE: Visual Studio code 

기 위한 사이트이다.
- 화면 중앙의 버튼 3개는 차례대로 로그인, 회원가입, 디테일 보기 버튼이다.
- 페이지를 이동할 때마다 소리로 알려준다.



***Major features***

- 최대한 마우스를 사용하지 않도록 탭을 사용하여 입력할 수 있는 곳을 지정할 수 있게 하였고, 음성(구글 클라우드 TTS api)으로 설명을 해주도록 설계했다. 
- tkinter 파이썬 라이브러리로 gui를 구성하였다.
- pyinstaller로 실행파일을 만들었다.
-
  ```
  #실행파일을 만드는 코드(cmd)
  pyinstaller --noconsole --onefile -n="BlindHelperLicense" --add-data "service_secret_key.json;." --add-data "error.mp3;." --add-data "get.mp3;." --add-data "getfinish.mp3;." check.py

  #exe가 제대로 실행되기 위한 상대 주소 사용 함수(py)
  def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
  ```

### b - BlindHelper Program

<img width="961" alt="chrome_cSLdJfE6SP" src="https://github.com/Madweek4/madcamp_week4/assets/155048947/cdff5684-3b6d-4518-adec-23ff7caa8489">
<br/>실행 화면
<br/><br/><br/>
<img width="961" alt="chrome_cSLdJfE6SP" src="https://github.com/Madweek4/madcamp_week4/assets/155048947/cd9d5f29-ee29-49a1-8cc3-a38bd6123d6b">
<br/>글자 추출 과정 시각화
<br/><br/><br/>
<img width="961" alt="chrome_cSLdJfE6SP" src="https://github.com/Madweek4/madcamp_week4/assets/155048947/17f19dab-7cd8-4864-a566-3a021535b43e">
<br/>글자 추출 과정 시각화(잘리는 부분 제거)
<br/><br/><br/>


***Major features***

- BlindHelper 프로그램은 실행한 후에 따로 ui가 존재하지 않고 음성으로만 설명이 되도록 만들었다.
- 단축키들로 기능을 구현할 수 있다. "ctrl+alt"로 모든 단축키가 시작된다.
-
  ```
  ctrl+alt+q: 캡처 시작
  ctrl+alt+w: 음성 설명 취소
  ctrl+alt+e: 음성 설명 중지
  ctrl+alt+r: 음성 설명 다시재생(중지된 부분부터)
  ctrl+alt+d: 프로그램 종료
  ctrl+alt+f: 요약 시작
  ```
- 캡처가 시작되면 현재 화면에서 드래그하여 캡처 영역을 정할 수 있다. 드래그 영역은 노란색으로 표시하여 어느 부분을 캡처하는 지 인지할 수 있게 하였다.
- 구글 클라우드 api를 통해 글자를 인식할 때 서로 가까이 있는 글자들을 한 그룹으로 인식하여 그리드 형태의 사이트에서도 문맥에 맞게 글자를 인식할 수 있게 하였다.
- 인식된 글자는 pykospacing 라이브러리를 통해 띄어쓰기를 적용하여 TTS가 읽을 때 자연스럽게 읽도록 구성했다.
- ```
  pip install git+https://github.com/haven-jeon/PyKoSpacing.git```
- 요약 기능이 시작되면 우선 구글 클라우드 api를 통해 캡처 이미지에서 이미지 컨텐츠들의 키워드들을 추출한다.
- 이미지 키워드들을 추출할 때 confidence가 70% 이상인 키워드만 추출하여 정확도를 높였다.
- 해당 키워드와 텍스트를 이용하여 chatgpt api가 요약한 후 이를 TTS로 출력한다.
- 프롬프트를 구성할 때 텍스트만 있는 경우, 이미지만 있는 경우, 둘 다 있는 경우 세 가지로 나누어 프롬프트를 구성하여 자연스럽게 설명할 수 있도록 설계했다.
- 이 프로그램도 license 프로그램과 마찬가지로 상대 주소를 사용하고, pyinstaller로 exe 파일을 만들었다.
  <br/><br/><br/>
  
- 첫 번재 사진은 프로그램에서 캡처를 진행할 때의 화면을 나타낸 것이고, 두, 세 번째 사진은 기술적으로 어떻게 인식된 글자를 가져오는 지 나타낸 사진이다.
- 캡처를 시작할 때 화면에서 움직이는 부분들이 있기에 우선 전체 화면을 캡처한다.
- 그 후에 구글 api를 통해 전체 화면에서 글자들을 인식하고 인식된 글자들의 좌표를 추출한다. 이를 보여준 것이 2,3번째 사진이다.
- 상단바나 하단바에 의해 잘린 글자들은 confidence로 판단하여 추출하지 않는다. 이는 3번째 사진에서 잘린 글자들에 초록색 박스가 없는 이유이다.
- 드래그 했을 때 글자 박스의 좌표와 드래그 영역이 겹치는 모든 글자를 추출하도록 설계했다.
- 이런 식으로 설계하여 글자가 잘렸을 때에도 제대로 글자를 추출할 수 있도록 만들었다. 


## 5. DIRECTORY STRUCTURE

```
#BlindHelper 프로그램
📦BlindHelper
 ┣ 📂__pycache__
 ┃ ┣ 📜ImageLabeler.cpython-310.pyc
 ┃ ┣ 📜ImageLabeler.cpython-38.pyc
 ┃ ┣ 📜NaverOCR.cpython-310.pyc
 ┃ ┣ 📜NaverOCR.cpython-38.pyc
 ┃ ┣ 📜OpenAIChat.cpython-310.pyc
 ┃ ┣ 📜OpenAIChat.cpython-38.pyc
 ┃ ┣ 📜screenshot.cpython-310.pyc
 ┃ ┣ 📜screenshot.cpython-38.pyc
 ┃ ┣ 📜TTS.cpython-310.pyc
 ┃ ┗ 📜TTS.cpython-38.pyc
 ┣ 📜BlindHelper.spec
 ┣ 📜cancel.mp3
 ┣ 📜capturecancel.mp3
 ┣ 📜capturestart.mp3
 ┣ 📜dragtest.py
 ┣ 📜exefolder.ico
 ┣ 📜fullscreenshot.png
 ┣ 📜hash.mp3
 ┣ 📜hash.txt
 ┣ 📜ImageLabeler.py
 ┣ 📜main.py
 ┣ 📜NaverOCR.py
 ┣ 📜notext.mp3
 ┣ 📜OpenAIChat.py
 ┣ 📜output.jpg
 ┣ 📜programexit.mp3
 ┣ 📜programstart.mp3
 ┣ 📜screenshot.png
 ┣ 📜screenshot.py
 ┣ 📜service_secret_key.json
 ┣ 📜summary.mp3
 ┣ 📜sumstart.mp3
 ┣ 📜test.mp3
 ┣ 📜test.py
 ┣ 📜text.mp3
 ┣ 📜TTS.py
 ┣ 📜ttt.py
 ┗ 📜wait.mp3
```
