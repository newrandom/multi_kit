from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_main import Ui_MainWindow
# from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
# from PySide6.QtCore import QUrl
import PySide6.QtAsyncio as QtAsyncio, asyncio, requests, time, random



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.SIGNAL = None      # api 호출 시그널

        # self.ui.btnRun.clicked.connect(lambda: asyncio.create_task(self.to_thread_get_number()))
        self.ui.btnRun.clicked.connect(lambda:asyncio.create_task(self.btnRunClick()))

    # api 호출하기
    async def to_thread_get_number(self):
        # signal 이 None 이면 api 호출, 아니면 호출 하지 않음
        if self.SIGNAL is None:
            await asyncio.to_thread(self.get_number)

    def get_number(self):
        self.SIGNAL = "fetching"
        try:
            print(self.SIGNAL)
            url = "http://127.0.0.1:8000/get_number"
            response = requests.get(url)

            # to_thread 테스트
            for _ in range(random.randint(3,6)):
                print("Fetching number...")
                time.sleep(1)

            print("Fetch complete.")
            if response.status_code == 200:
                data = response.json()
                number = data.get("number", "N/A")
                self.ui.lbStatus.setText(f"Number : {number}")

                # api 호출이 끝나면 set_number 에 0 을 던지기 (초기화)
                reset_url = "http://127.0.0.1:8000/set_number/"
                request = requests.post(reset_url, json={"number": random.randint(1,101)})
                if request.status_code == 200:
                    print("Number reset to 0 successfully.")
            else:
                self.ui.lbStatus.setText("Failed to fetch number")
        except Exception as e:
            self.ui.lbStatus.setText(f"Error: {str(e)}")
        finally:
            self.SIGNAL = None

    # 체크가 되어있으면 정기적 loop 호출, 안되어있으면 일반 호출
    async def btnRunClick(self):
        if self.SIGNAL is None:
            # chkCondition이 체크되어 있으면 정기적 루프 진행,
            # 체크되어 있지 않으면 일반 호출
            if self.ui.chkCondition.isChecked():
                while True:
                    print("Checked: Starting periodic loop")
                    await self.to_thread_get_number()
                    await asyncio.sleep(5)
                    if not self.ui.chkCondition.isChecked():
                        break
            else:
                print("Not Checked: Performing single API call")
                await self.to_thread_get_number()
        else:
            print("API call already in progress, skipping...")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    # app.exec()

    QtAsyncio.run(handle_sigint=True)