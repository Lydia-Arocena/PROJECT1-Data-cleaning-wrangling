# PROYECTO-1-IRONHACK

![Aquí había una foto de un tiburón](https://github.com/Lydia-Arocena/PROYECTO-1-IRONHACK/blob/main/foto_tiburon.jpg)


## 1. OBJETIVO DEL PROYECTO:
Este proyecto pretende verificar o refutar las tres hipótesis planteadas sobre los datos contenidos en el dataframe "attacks.csv". Éstas son:
- En 2018 hubo más ataques de tiburones tigre en el hemisferio sur que en 1990.
- En México hay más ataques de tiburones blancos que en USA.
- La mayoría de las víctimas que bucean son mujeres.

Para ello, primero, he procedido a la limpieza de los datos del mismo a través de diferentes técnicas que expondré más adelante y, después, he visualizado los datos limpios a través de gráficos que me han servido para finalmente verificar/refutar cada una de las 3 hipótesis planteadas al inicio del proyecto.


## 2. ESTRUCTURA DEL REPO:
He trabajado utilizando dos archivos de Jupyter Notebook:

A. "Limpieza": Este archivo lo he utilizado para limpiar el dataframe objeto de estudio donde se recogía información sobre los ataques de tiburones clasificados en función de diversas variables (año, país, sexo de la víctima, actividad que estaba practicando cuando sucedió el ataque, si fue mortal o no, etc.).

Para ello, he utilizado 5 técnicas diferentes:
1. En primer lugar, he borrado las filas que eran enteras NaN.

2. En segundo lugar, he borrado las filas duplicadas.

3. En tercer lugar,he cambiado el nombre de dos columnas (Sex y Especies) porque me he dado cuenta de que contenían un espacio de la manera en la que estaban nombradas.

4. En cuarto lugar,al ser todas variables categóricas, he reemplazado los Nan por "Unkown" pues se trata de datos de los cuales no disponemos pero que se encuentran en filas donde sí hay otros datos valiosos que quiero conservar.

5. Por último, he tratado de armonizar los valores únicos de cada columna para disminuir su número a través de diferentes formas:

    a) Usando método de Pandas ".replace" para aquellas columnas que no tuvieran muchos valores únicos pero tuvieran algunos que claramente eran imputaciones de datos erróneas ("Sex", "Type" & "Fatal (Y/N)").

    b) Usando Regex para aquellas columnas cuyos datos hacían referencia a lo mismo pero habían sido imputados de múltiples formas (Species, Activitiy, Injury).

    c) También he construído algunas funciones contenidas en otro archivo llamado "cleaning_functions" del cual las he exportado que me han servido para armonizar la columa "Year" así como para usar Regex en las tres columnas mencionadas anteriormente. Además, construí otra función llamada "hemisferio" para crear una columna nueva en el df a partir de la columna "Country".
        
        
B. "Visualización": En este Jupyter Notebook he ido verificando/refutando cada una de mis tres hipótesis a través de diferentes gráficos de la Libería Seaborn: gráficos de barras e histogramas.


## 3. LIBRERÍAS USADAS:
- Pandas.
- Numpy.
- Seaborn
- Regex.
- Sys.
- src.cleaning_functions: Librería creada por mí para la limpieza de los datos.



## 4. CONCLUSIÓN:
Una vez analizado los datos sobre los ataques de los tiburones, podemos concluir lo siguiente:
- Se verifica la Hipótesis 1 puesto que efectivamente hubo más ataques de tiburones Tigre en el Hemiferio Sur en el año 2018 que en el año 1990: 2 vs 1.
- La hipótesis 2 se refuta porque se demuestra que en USA se produce un mayor número de ataques de tiburones blancos que en México.
- Se refuta la Hipótesis 3 pues la mayoría de las víctimas que practican buceo no son mujeres sino hombres.

