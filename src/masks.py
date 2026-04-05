import logging
import os

# Путь к файлу лога (поднимаемся на уровень выше из src в корень)
log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'masks.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# mode='w' чтобы файл очищался при каждом запуске
file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
