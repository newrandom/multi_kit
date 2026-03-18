from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_main import Ui_MainWindow
import PySide6.QtAsyncio as QtAsyncio, asyncio
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.async_condition = None

        self.ui.btnRun.clicked.connect(lambda: asyncio.create_task(self.manual_run()))   
        self.ui.chkCondition.stateChanged.connect(lambda: asyncio.create_task(self.auto_run()))     

    async def manual_run(self):
        if self.ui.btnRun.text() == "Start":
            await self.cancel_async()

            self.ui.btnRun.setText("Stop")
            self.async_condition = asyncio.create_task(self.run())
        else:
            self.ui.btnRun.setText("Start")
            await self.cancel_async()

    async def auto_run(self):
        while True:
            await asyncio.sleep(5)
            if self.ui.chkCondition.checkState() == Qt.CheckState.Checked:
                if self.async_condition == None:
                    print('Checked!')
                    self.async_condition = asyncio.create_task(self.run())
            else:
                if self.async_condition and not self.async_condition.done():
                    print('Unchecked!')
                    await self.cancel_async()

    async def run(self):
        count = 0
        self.ui.lbStatus.setText("Running...")
        for _ in range(5):
            count += 1
            await asyncio.sleep(1)
            self.ui.lbStatus.setText(f"Running...{count}")

        self.ui.lbStatus.setText(f"Finished...{count}")
        self.ui.btnRun.setText("Start")

    async def cancel_async(self):
        if self.async_condition and not self.async_condition.done():
            self.async_condition.cancel()
            try:
                await self.async_condition
            except asyncio.CancelledError:
                pass
            finally:
                self.async_condition = None
    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    # app.exec()

    QtAsyncio.run(handle_sigint=True)