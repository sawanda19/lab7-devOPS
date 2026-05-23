# Модель: Автоматизоване складання розкладу занять — Генетичний алгоритм (5 семестр)
# Автор: Акімов Андрій, група АІ-231

# ЛР7: Хмарне розгортання — Render

## Сервіс
**URL:** `https://devops-231-akimov.onrender.com`

## Endpoints
| Метод | URL | Опис |
|-------|-----|------|
| GET  | `/` | Інформація про сервіс |
| GET  | `/health` | Стан сервера |
| POST | `/calculate` | Запуск оптимізації |

## Тестовий запит (після деплою)
```bash
curl -X POST https://devops-231-akimov.onrender.com/calculate \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Environment Variables (Render)
| Змінна | Значення | Опис |
|--------|----------|------|
| `PORT` | `5000` | Порт сервера |
| `DEBUG` | `false` | Debug вимкнено |
| `SECRET_KEY` | `***` | Секретний ключ (в Render secrets) |

## Безпека (підготовка до ЛР8)
- ✅ Debug mode вимкнено (`DEBUG=false`)
- ✅ Секрети через environment variables
- ✅ Паролі не збережені у коді
- ✅ Docker image готовий до security scan

## Структура
```
├── api.py
├── test_api.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/workflows/ci.yml
```
