from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt


class BalanceTab(QWidget):
    def __init__(self, kiwoom):
        super().__init__()
        self.kiwoom = kiwoom
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 요약 정보 레이블
        self.total_purchase_label = QLabel("전체 매입 금액: ")
        self.total_evaluation_label = QLabel("평가 금액: ")
        self.total_profit_loss_label = QLabel("평가 손익: ")
        layout.addWidget(self.total_purchase_label)
        layout.addWidget(self.total_evaluation_label)
        layout.addWidget(self.total_profit_loss_label)

        # 새로고침 버튼
        self.refresh_button = QPushButton("새로고침")
        self.refresh_button.clicked.connect(self.update_data)
        layout.addWidget(self.refresh_button)

        # 보유 종목 테이블
        self.stock_table = QTableWidget()
        self.stock_table.setColumnCount(8)
        self.stock_table.setHorizontalHeaderLabels(["종목명", "보유 수량", "보유 가격", "평가 손익", "현재가", "평균단가", "전일대비", "보유비중"])
        layout.addWidget(self.stock_table)

        self.setLayout(layout)
        self.update_data()

    def update_data(self):
        # API를 통해 데이터를 조회하고 업데이트합니다.
        self.kiwoom.get_account_info()  # 예: 계좌 정보 조회
        self.kiwoom.get_stock_positions()  # 예: 보유 종목 조회

        # 데이터를 레이블과 테이블에 업데이트
        self.total_purchase_label.setText(f"전체 매입 금액: {self.kiwoom.total_purchase}")
        self.total_evaluation_label.setText(f"평가 금액: {self.kiwoom.total_evaluation}")
        self.total_profit_loss_label.setText(f"평가 손익: {self.kiwoom.total_profit_loss}")

        # 테이블에 데이터 채우기
        self.stock_table.setRowCount(len(self.kiwoom.positions))
        for i, stock in enumerate(self.kiwoom.positions):
            self.stock_table.setItem(i, 0, QTableWidgetItem(stock['name']))
            self.stock_table.setItem(i, 1, QTableWidgetItem(str(stock['quantity'])))
            self.stock_table.setItem(i, 2, QTableWidgetItem(str(stock['purchase_price'])))
            self.stock_table.setItem(i, 3,
                                     QTableWidgetItem(f"{stock['profit_loss']} ({stock['profit_loss_percent']}%)"))
            self.stock_table.setItem(i, 4, QTableWidgetItem(str(stock['current_price'])))
            self.stock_table.setItem(i, 5, QTableWidgetItem(str(stock['average_price'])))
            self.stock_table.setItem(i, 6, QTableWidgetItem(str(stock['day_change'])))
            self.stock_table.setItem(i, 7, QTableWidgetItem(f"{stock['holding_percent']}%"))

