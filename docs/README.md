# Geometric Lib
## Описание
### Geometric Lib - библиотека для работы с площадью и периметром круга и квадрата

## Usage
### Клонируйте репозиторий
```bash
git clone https://github.com/rabtra1/geometric_lib.git
```

### Импортируйте библиотеку в python файле,где нужны вычисления
```py
import geometric_lib.circle as circle
import geometric_lib.square as square

print(circle.perimeter(5)) #31.41592653589793
print(square.area(2)) # 4
```

## Доступные функции и примеры вызова
```py
circle.area(r) # Площадь круга с радиусом r
print(circle.area(5)) # 78.53981633974483

circle.perimeter(r) # Периметр(длина окружности) круга с радиусом r
print(circle.perimeter(1)) # 6.283185307179586

square.area(a) # Площадь квадрата со стороной a
print(square.area(8)) # 64

square.perimeter(a) # Периметр квадрата со стороной a
print(square.perimeter(10)) # 40
```
### История коммитов
```

commit d2b6c0fde7cd94ae23dfd5a82a641091ccfa4096
Date: Mon Sep 29 18:20:46 2025 +0300
message: Added files circle.py and square.py that do math for circle and square. also wrote documentation for all functions and added README.md file

```