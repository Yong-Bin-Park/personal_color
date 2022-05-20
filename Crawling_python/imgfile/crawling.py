#importing the library
#기존 google_images_download 라이브러리 사용 시 오류가 발생해 수정버전을 설치해야함
#수정버전 : pip install git+https://github.com/Joeclinton1/google-images-download.git
from google_images_download import google_images_download   

#class instantiation
response = google_images_download.googleimagesdownload()   

# keywords : 원하는 검색 키워드
# limit : 원하는 다운로드 사진 개수 (수정 버전에서는 최대 100개까지 가능)
# format : 다운로드 확장자 지정
arguments = {"keywords":"소녀시대 윤아,송혜교,이다인,오마이걸 효정,여자아이들 우기,아이유,수지,레드벨벳 조이,원더걸스 유빈,소녀시대 제시카,손예진,김연아,아이브 장원영,트와이스 다현,레드벨벳 아이린,소녀시대 티파니,우주소녀 설아,이영애,트와이스 채영,트와이스 나연,김고은,김태리,전지현,손예진,태연,이성경,블랙핑크 제니,신세경,스테파니 리,캣 데닝스,한예슬,아이즈원 김민주,레드벨벳 예리,엔시티 해찬,bts 뷔,김유정,현아,김효진,이효리,이민정,선미,청하,여자친구 은하,트와이스 미나,김옥빈,김혜수,문근영,선우선,앤 헤서웨이,강동원",
                        "limit":100,
                        "print_urls":True,
                        "format":"jpg"
                            }

#passing the arguments to the function
paths = response.download(arguments)   

#printing absolute paths of the downloaded images
print(paths)   