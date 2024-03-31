from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='M2MwNWY1ODYtNTg3YS00OTM4LWJhZTAtYTAwYTI3MzY0YjhhOmY2Y2E4OTNlLTNhOGItNGU5Mi1hMzZjLWE3ZWI5OTZjNjE3ZA==', verify_ssl_certs=False)

messages = [
    {
        "model": "GigaChat",
        "messages": [
            {
                "role": "system",
                "content": "Ты — профессиональный маркетолог с опытом написания высококонверсионной рекламы. Для генерации описания товара ты изучаешь потенциальную целевую аудиторию и оптимизируешь рекламный текст так, чтобы он обращался именно к этой целевой аудитории. Создай текст объявления с привлекающим внимание заголовком и убедительным призывом к действию, который побуждает пользователей к целевому действию."
            },
            {
                "role": "user",
                "content": "Название товара: SberBoom. Категория: умные колонки. Ключевые слова: умная колонка, салют, умный дом."
            }
        ]
    }
]

def chatbot(user_input):
    messages.append(HumanMessage(content=user_input))
    res = chat(messages)
    messages.append(res)
    return res.content


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtCore import Qt


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание главного виджета и макета
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Создание QLineEdit для ввода сообщения
        self.line_edit = QLineEdit()
        main_layout.addWidget(self.line_edit)

        # Создание кнопки для отправки сообщения
        self.send_button = QPushButton('Отправить')
        self.send_button.clicked.connect(self.send_message)
        main_layout.addWidget(self.send_button)

        # Создание QLabel для отображения ответа от чат-бота
        self.response_label = QLabel()
        self.response_label.setWordWrap(True) # Делаем QLabel мультистрочным
        main_layout.addWidget(self.response_label)

        # Создание второй кнопки и QLabel
        self.second_button = QPushButton('Какая страна')
        self.second_button.clicked.connect(self.second_button_clicked)
        main_layout.addWidget(self.second_button)

        self.second_label = QLabel()
        main_layout.addWidget(self.second_label)
        self.second_label.setWordWrap(True) # Делаем QLabel мультистрочным

        self.third_button = QPushButton('Какой тип путешествий')
        self.third_button.clicked.connect(self.third_button_clicked)
        main_layout.addWidget(self.third_button)

        self.third_label = QLabel()
        main_layout.addWidget(self.third_label)
        self.third_label.setWordWrap(True) # Делаем QLabel мультистрочным



        # Применение стилей CSS
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLineEdit {
                border: 1px solid #ccc;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QLabel {
                font-size: 14px;
                color: #333;
                margin-top: 10px;
            }
        """)

    def send_message(self):
        user_input = self.line_edit.text()
        # Здесь вызывается ваша функция chatbot
        # res = chatbot(user_input)
        # Для демонстрации используем простой ответ
        res = chatbot(user_input)
        self.response_label.setText(res)
        self.line_edit.clear()

    def second_button_clicked(self):
        input = "Пиши только список стран, которые ты рекомендуешь, никаких обьяснений, не более 3 стран"
        res = chatbot(input)
        self.second_label.setText(res)

    def third_button_clicked(self):
        input = "анализируй мой ответ и пиши тип путешествия, который мне подходит"
        res = chatbot(input)
        self.third_label.setText(res)



# Запуск приложения
app = QApplication(sys.argv)
window = ChatBotWindow()
window.show()
sys.exit(app.exec_())
