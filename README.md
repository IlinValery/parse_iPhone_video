# Разделение видеопотока для подготовки обучающей выборки искусственной нейронной сети

## Информация по проекту
### Входные параметры

* Имя файла
* Частота кадров

### Выходные параметры
* Кадр

### Настройка окружения
```bash
git clone https://github.com/IlinValery/parse_iPhone_video.git
cd parse_iPhone_video
python3 -m venv venv
source venv/bin/activate
pip install -r req.txt
```
### Запуск скрипта 

```bash
python3 save_frames.py --inf file.mp4 --fr 240
```

* --inf file.mp4 - входной файл
* --fr 240 - частота использования кадров

На выходе получаем набор кадров с названием file%d.jpg

