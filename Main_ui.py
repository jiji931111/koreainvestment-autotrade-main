import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from balance_tab import BalanceTab  # BalanceTab 클래스를 가져옵니다.
from api_handler import KoreaInvestmentAPIHandler  # api_handler 클래스를 가져옵니다.

sys.path.append('path_to_directory')
class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('주식 자동매매 시스템')
        self.setGeometry(100, 100, 1000, 600)

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # 한국투자증권 API 핸들러 인스턴스 생성
        self.korea_investment = KoreaInvestmentAPIHandler()

        # 잔고 탭 추가
        self.balance_tab = BalanceTab(self.korea_investment)
        self.tabs.addTab(self.balance_tab, "잔고")

        # 추가 탭 구성 (전략 설정, 매매 일지 등)



def main():
    app = QApplication(sys.argv)
    ex = MainUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
