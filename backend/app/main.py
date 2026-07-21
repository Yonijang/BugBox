from fastapi import FastAPI #FastAPI를 가져온다

app = FastAPI( #우리 백엔드 어플리케이션을 만든다
    title = "BugBox API",
    description = "Backend API for BugBox",
    version = "0.1.0",
)

@app.get("/") #/주소로 GET 요청이 들어오면 아래 함수를 실행한다
def root():
    return {
        "message": "BugBox API is running" #JSON 데이터를 돌려준다
    }