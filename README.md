# PROYECTO-1-IRONHACK

![Aquí había una foto de un tiburón](Images/foto_tiburon.jpg)


## 1. OBJETIVO DEL PROYECTO:
Este proyecto pretende verificar o refutar las tres hipótesis planteadas sobre los datos contenidos en el [dataset](https://www.kaggle.com/teajay/global-shark-attacks). Éstas son:
- En 2018 hubo más ataques de tiburones tigre en el hemisferio sur que en 1990.
- En México hay más ataques de tiburones blancos que en USA.
- La mayoría de las víctimas que bucean son mujeres.

Para ello, primero, he procedido a la limpieza de los datos del mismo a través de diferentes técnicas que expondré más adelante y, después, he visualizado los datos limpios a través de gráficos que me han servido para finalmente verificar/refutar cada una de las 3 hipótesis planteadas al inicio del proyecto.


## 2. ESTRUCTURA DEL REPO:
He trabajado utilizando dos archivos de Jupyter Notebook:

A. "Limpieza": Este archivo lo he utilizado para limpiar el dataframe objeto de estudio donde se recogía información sobre los ataques de tiburones clasificados en función de diversas variables (año, país, sexo de la víctima, actividad que estaba practicando cuando sucedió el ataque, si fue mortal o no, etc.).

Para ello, he utilizado 5 técnicas diferentes:
1. Eliminación de las filas que eran enteras NaN.

2. Eliminación de filas duplicadas.

3. Cambio de nombre de dos columnas (Sex y Especies).

4. Gestión de los Nan, en este caso, sustitución por "Unkown".

5. Armonización de los valores únicos de cada columna para disminuir su número a través de diferentes formas:

    a) Usando método de Pandas ".replace" para aquellas columnas que no tuvieran muchos valores únicos pero tuvieran algunos que claramente eran imputaciones de datos erróneas.

    b) Usando Regex para aquellas columnas cuyos datos hacían referencia a lo mismo pero habían sido imputados de múltiples formas.

    c) Usando funciones contenidas en otro archivo llamado "cleaning_functions".
        
        
B. "Visualización": En este Jupyter Notebook he ido verificando/refutando cada una de mis tres hipótesis a través de diferentes gráficos de la Libería Seaborn: gráficos de barras e histogramas.


## 3. LIBRERÍAS USADAS:
- [Pandas](https://pandas.pydata.org/docs/)
- [Numpy](https://numpy.org/doc/)
- [Seaborn](https://seaborn.pydata.org/)
- [Regex](https://docs.python.org/3/library/re.html)
- [Sys](https://docs.python.org/3/library/sys.html)



## 4. CONCLUSIÓN:
Una vez analizado los datos sobre los ataques de los tiburones, podemos concluir lo siguiente:
- Se verifica la Hipótesis 1 puesto que efectivamente hubo más ataques de tiburones Tigre en el Hemiferio Sur en el año 2018 que en el año 1990: 2 vs 1.
- La hipótesis 2 se refuta porque se demuestra que en USA se produce un mayor número de ataques de tiburones blancos que en México.
- Se refuta la Hipótesis 3 pues la mayoría de las víctimas que practican buceo no son mujeres sino hombres.

