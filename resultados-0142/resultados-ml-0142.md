# Reporte de Análisis de Datos - Pandas

`yahir sifuentes Machine Learning pandas, NC 0142`

## 1. DataFrame Convertido
```text
      Farmacia  Productos  Clientes_dia
0    San Pablo       8000          1500
1    Similares       5000          2000
2   Del Ahorro       6500          1800
3  Guadalajara       7500          1200
4    Benavides       6000          1000
5  Del Savings       5500           900
```

## 2.1 Primeras Filas (head)
```text
    Farmacia  Productos  Clientes_dia
0  San Pablo       8000          1500
1  Similares       5000          2000
```

## 2.2 Últimas Filas (tail)
```text
      Farmacia  Productos  Clientes_dia
4    Benavides       6000          1000
5  Del Savings       5500           900
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Farmacia          str
Productos       int64
Clientes_dia    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   Farmacia      6 non-null      str  
 1   Productos     6 non-null      int64
 2   Clientes_dia  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Productos'
```text
count       6.000000
mean     6416.666667
std      1158.303357
min      5000.000000
25%      5625.000000
50%      6250.000000
75%      7250.000000
max      8000.000000
Name: Productos, dtype: float64
```

## 4. Ordenar Ascendente por Productos
```text
      Farmacia  Productos  Clientes_dia
1    Similares       5000          2000
5  Del Savings       5500           900
4    Benavides       6000          1000
2   Del Ahorro       6500          1800
3  Guadalajara       7500          1200
0    San Pablo       8000          1500
```

## 5. Ordenar Descendente por Clientes_dia
```text
      Farmacia  Productos  Clientes_dia
1    Similares       5000          2000
2   Del Ahorro       6500          1800
0    San Pablo       8000          1500
3  Guadalajara       7500          1200
4    Benavides       6000          1000
5  Del Savings       5500           900
```

`yahir sifuentes Machine Learning pandas, NC 0142`