from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_main import Ui_MainWindow
import PySide6.QtAsyncio as QtAsyncio, asyncio, datetime, time, random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Variable
        self.async_task_condition = None
        self.sync_task_condition = False

        # Event Connections
        self.ui.btnRun.clicked.connect(lambda:asyncio.create_task(self.btnRun_Clicked()))
        

    # timer test
    async def run_timer(self):
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            self.ui.lbStatus.setText(f"Current Time: {now}")
            await asyncio.sleep(1)

    # action function
    async def call_api_manually(self):
        print('Option loaded')
        loaded_condition = random.randint(1,3)
        print(f'Loaded condition: {loaded_condition}')

        self.sync_task_condition = True

        # TEST - Manual function
        if loaded_condition == 1:
            await asyncio.to_thread(lambda: self.func_1())
            print('call func_1 done')
        elif loaded_condition == 2:
            await asyncio.to_thread(lambda: self.func_2())
            print('call func_2 done')
        elif loaded_condition == 3:
            await asyncio.to_thread(lambda: self.func_3())
            print('call func_3 done')
        
        self.sync_task_condition = False

        print('call option api (Manual) done')
        self.ui.btnRun.setText("Start")

    async def call_api_auto(self):
        while True:
            await asyncio.sleep(5)
            print('Option loaded')

            loaded_condition = random.randint(1,3)
            print(f'Loaded condition: {loaded_condition}')

            # Test - Manual function
            if loaded_condition == 1:
                await asyncio.to_thread(lambda: self.func_1())
                print('call func_1 done')
            elif loaded_condition == 2:
                await asyncio.to_thread(lambda: self.func_2())
                print('call func_2 done')
            elif loaded_condition == 3:
                await asyncio.to_thread(lambda: self.func_3())
                print('call func_3 done')

            print('call option api (Auto) done')


    # normal function    
    def func_1(self):
        for _ in range(10):
            time.sleep(1)
            print(f'func_1 is running{_+1}')
        self.ui.lbStatus.setText("Func 1 done")

    def func_2 (self):
        time.sleep(3)
        self.ui.lbStatus.setText("Func 2 done")

    def func_3(self):
        time.sleep(1)
        self.ui.lbStatus.setText("Func 3 done")

    # control function    
    async def btnRun_Clicked(self):
        if self.ui.btnRun.text() == "Start":
            self.ui.btnRun.setText("Stop")
            await self.cancel_task()

            # self.async_task_condition = asyncio.create_task(self.run_timer())
            if self.ui.chkCondition.isChecked() == False:
                self.async_task_condition = asyncio.create_task(self.call_api_manually())
            else:
                self.async_task_condition = asyncio.create_task(self.call_api_auto())
        else:
            self.ui.btnRun.setText("Start")
            await self.cancel_task()

            self.ui.lbStatus.setText("Click The Button")

    # Cancel Task Function
    async def cancel_task(self):
        if self.async_task_condition and not self.async_task_condition.done():
            self.async_task_condition.cancel()
            try:
                await self.async_task_condition
            except asyncio.CancelledError:
                pass
            finally:
                self.async_task_condition = None




if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()

    QtAsyncio.run()