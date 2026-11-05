# Limitaciones de ChuspaCalc - Versión Inicial (v1)

#

##### A continuación, se detallan las limitaciones conocidas y esperadas de ChuspaCalc en su versión inicial, así como algunas funcionalidades previstas para futuras versiones.

#

# 1\. Falta de integración con herramientas de diseño gráfico

#

##### Descripción: En esta versión no se incluye soporte para importar ni exportar archivos de herramientas como Adobe Illustrator, Figma o Inkscape. No es posible trabajar directamente con estos formatos.

#

##### ¿Solución temporal? Sí. Los archivos deben exportarse o convertirse a formatos compatibles (PNG, JPG o SVG simple) antes de utilizarlos en ChuspaCalc.

#####

##### ¿Planeado para futuras versiones? Sí. Se tiene previsto integrar soporte para estos formatos en la versión v1.2.

#

# 2\. No soporta sistemas operativos móviles

#

##### Descripción: La herramienta solo funciona en sistemas operativos de escritorio como Windows, Linux y macOS. No es posible utilizarla en Android ni iOS.

#####

##### ¿Solución temporal? No. Actualmente no existe una forma oficial de ejecutarla en dispositivos móviles.

#####

##### ¿Planeado para futuras versiones? No. Esta funcionalidad no se encuentra dentro de los planes a corto o mediano plazo, ya que se priorizarán otras características.

#

# 3\. No gestiona proyectos colaborativos simultáneos

#

##### Descripción: La herramienta solo permite trabajar con un usuario a la vez en un mismo proyecto. No cuenta con edición en tiempo real ni control de versiones compartido.

#####

##### ¿Solución temporal? Sí. Los usuarios pueden compartir archivos manualmente y fusionar los cambios mediante herramientas externas.

#####

##### ¿Planeado para futuras versiones? Sí. Esta funcionalidad está prevista para la versión v2.0.



# 4\. Sin soporte para bases de datos externas



##### Descripción: Actualmente no es posible conectar, leer ni escribir información en bases de datos externas como MySQL, PostgreSQL o MongoDB. La herramienta únicamente trabaja con archivos locales.

#####

##### ¿Solución temporal? No. Por el momento no existe una forma de conectarse a fuentes de datos externas.

#####

##### ¿Planeado para futuras versiones? Sí. Se agregará conectividad básica con bases de datos en la versión v1.5.

#####

# 5\. Limitaciones por módulo

#

# 5.1 Módulo Civil

#####

##### Descripción: El módulo Civil implementa un conjunto limitado de funcionalidades para el análisis estructural.

#####

##### Limitaciones conocidas

#####

##### \- Solo soporta vigas simplemente apoyadas.

##### \- No soporta vigas continuas.

##### \- No soporta marcos estructurales complejos.

##### \- No realiza análisis sísmico.

##### \- No contempla cargas dinámicas avanzadas.

##### \- Los resultados deben considerarse aproximaciones para escenarios básicos.

#####

# 5.2 Módulo Eléctrica

#####

##### Descripción: El módulo Eléctrica está orientado a circuitos básicos de corriente continua.

#####

##### Limitaciones conocidas

#####

##### \- Solo trabaja con corriente continua (DC).

##### \- No soporta corriente alterna (AC).

##### \- Solo considera resistencias puras.

##### \- No soporta capacitores ni inductores.

##### \- No realiza análisis fasorial.

##### \- No contempla fenómenos avanzados de potencia eléctrica.



# 5.3 Módulo Matemáticas

#####

##### Descripción: El módulo Matemáticas utiliza la precisión numérica estándar del lenguaje.

#####

##### Limitaciones conocidas

#####

##### \- No utiliza bibliotecas de alta precisión numérica.

##### \- Pueden existir errores de redondeo.

##### \- Pueden existir errores de punto flotante.

##### \- Las operaciones repetidas pueden acumular pequeñas diferencias numéricas.

##### \- Algunos resultados pueden variar ligeramente dependiendo de la plataforma utilizada.

#####

# 5.4 Módulo Geometría

#####

##### Descripción: El módulo Geometría se enfoca en operaciones geométricas básicas.

#####

##### Limitaciones conocidas

#####

##### \- Solo soporta figuras regulares.

##### \- No soporta figuras irregulares complejas.

##### \- No incluye modelado tridimensional avanzado.

##### \- Algunas fórmulas asumen condiciones ideales.

##### \- No contempla geometría computacional avanzada.



# 5.5 Módulo Sistemas

#####

##### Descripción: El módulo Sistemas implementa soporte limitado para el manejo de caracteres.

#####

##### Limitaciones conocidas

#####

##### \- Solo soporta caracteres ASCII en el rango de 0 a 127.

##### \- No soporta completamente Unicode.

##### \- Los caracteres especiales pueden producir resultados inesperados.

##### \- No existe soporte completo para alfabetos internacionales.

##### \- El procesamiento avanzado de texto no está implementado.


# 5.6 Alcance educativo de fórmulas y procedimientos simplificados

##### Descripción: Algunas herramientas implementadas en ChuspaCalc tienen un propósito principalmente educativo y utilizan modelos simplificados. Los resultados obtenidos deben interpretarse como aproximaciones para aprendizaje, práctica académica o validaciones preliminares, y no sustituyen procedimientos profesionales, software especializado ni normativa técnica vigente.

##### Simplificación de mapas de Karnaugh

##### Limitaciones conocidas

##### - La simplificación se realiza mediante agrupaciones típicas de mapas de Karnaugh.

##### - No implementa necesariamente algoritmos completos de minimización como Quine-McCluskey ni métodos avanzados de optimización lógica.

##### - Puede no ser adecuada para funciones de gran tamaño o para procesos de síntesis lógica industrial.

##### Simplificaciones LRFD

##### Limitaciones conocidas

##### - Las combinaciones de carga utilizan expresiones simplificadas con fines educativos.

##### - No reemplazan la aplicación directa de normas de diseño estructural vigentes.

##### - No contemplan todas las combinaciones especiales, factores de ajuste o requisitos normativos específicos de cada jurisdicción.

##### - Los resultados deben utilizarse únicamente como referencia conceptual o académica.

##### Pandeo de Euler

##### Limitaciones conocidas

##### - El cálculo se basa en las hipótesis clásicas del modelo de Euler.

##### - Es válido principalmente para columnas esbeltas sometidas a compresión axial.

##### - Supone comportamiento elástico lineal del material.

##### - No considera imperfecciones geométricas, excentricidades de carga, efectos inelásticos ni condiciones reales complejas de apoyo.

##### - Su aplicación fuera de los rangos de validez física del modelo puede producir resultados no representativos.

##### Uso académico de los resultados

##### - Las herramientas que indiquen explícitamente el uso de aproximaciones o modelos idealizados deben considerarse de carácter educativo.

##### - Los resultados no deben utilizarse como único criterio para decisiones de diseño, construcción, seguridad o certificación profesional.
