from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_main import Ui_MainWindow
# from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
# from PySide6.QtCore import QUrl
import PySide6.QtAsyncio as QtAsyncio, asyncio, requests, time



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.SIGNAL = None      # api 호출 시그널

        # self.ui.btnRun.clicked.connect(lambda: asyncio.to_thread(self.get_number()))
        # self.ui.btnRun.clicked.connect(lambda: self.get_number())
        self.ui.btnRun.clicked.connect(lambda: asyncio.create_task(self.to_thread_get_number()))

    # api 호출하기
    # async def get_number(self):
    #     # url = QUrl("http://127.0.0.1:8000/get_number")
    #     # request = QNetworkRequest(url)
    #     # # self.ui.lbStatus.setText(f"Number : {}")
    #     # print(request)
    #     url = "http://127.0.0.1:8000/get_number"
    #     response = await asyncio.to_thread(requests.get, url)
    #     print(response)
    #     if response.status_code == 200:
    #         data = response.json()
    #         number = data.get("number", "N/A")
    #         self.ui.lbStatus.setText(f"Number : {number}")
    #     await asyncio.sleep(1)

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
            for _ in range(5):
                print("Fetching number...")
                time.sleep(1)

            if response.status_code == 200:
                data = response.json()
                number = data.get("number", "N/A")
                self.ui.lbStatus.setText(f"Number : {number}")
            else:
                self.ui.lbStatus.setText("Failed to fetch number")
        except Exception as e:
            self.ui.lbStatus.setText(f"Error: {str(e)}")
        finally:
            self.SIGNAL = None

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    # app.exec()

    QtAsyncio.run(handle_sigint=True)