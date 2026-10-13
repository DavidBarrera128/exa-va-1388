# David Barrera NC = 1388

import cv2
from pathlib import Path

# 1. Localizar la carpeta raíz del proyecto
script_dir = Path(__file__).resolve().parent
carpeta_proyecto = script_dir.parent

# 2. Buscar automáticamente la carpeta de imágenes originales en el proyecto
carpetas_candidatas = list(carpeta_proyecto.rglob("img-original*"))

if not carpetas_candidatas:
    carpeta_imagenes = carpeta_proyecto
else:
    carpeta_imagenes = carpetas_candidatas[0]

# Definir/crear carpeta de resultados
carpeta_resultados = carpeta_proyecto / "resultados-img-1388"
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 3. Buscar la imagen "Chevrolet"
archivos_encontrados = list(carpeta_proyecto.rglob("*Chevrolet*"))
archivos_validos = [f for f in archivos_encontrados if f.suffix.lower() in ['.jpg', '.jpeg', '.png']]

if not archivos_validos:
    print(f"\n❌ No se encontró ningún archivo con el nombre 'Chevrolet' dentro de: {carpeta_proyecto}")
    print("\nArchivos de imagen encontrados en todo el proyecto:")
    todas_las_imgs = [f for f in carpeta_proyecto.rglob("*") if f.suffix.lower() in ['.jpg', '.jpeg', '.png']]
    for img in todas_las_imgs:
        print(f" - {img.relative_to(carpeta_proyecto)}")
    raise FileNotFoundError("Asegúrate de haber guardado la imagen 'Chevrolet.jpg' en el proyecto.")

ruta_original = archivos_validos[0]
print(f"✅ Imagen encontrada en: {ruta_original}")

# 4. Leer la imagen original
img1388 = cv2.imread(str(ruta_original))

if img1388 is None:
    raise FileNotFoundError(f"OpenCV no pudo leer el archivo: {ruta_original}")

# 5. Rotar la imagen 90 grados en sentido horario
img90_1388 = cv2.rotate(img1388, cv2.ROTATE_90_CLOCKWISE)

# 6. Rotar la imagen 45 grados
alto, ancho = img1388.shape[:2]
centro = (ancho // 2, alto // 2)
matriz_rotacion = cv2.getRotationMatrix2D(centro, 45, 1.0)
img45_1388 = cv2.warpAffine(img1388, matriz_rotacion, (ancho, alto))

# 7. Redimensionar a 600x500 píxeles
img600x500_1388 = cv2.resize(img1388, (600, 500))

# 8. Dibujar rectángulo rojo
img_rojo_1388 = img1388.copy()
x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200
cv2.rectangle(img_rojo_1388, (x1, y1), (x2, y2), (0, 0, 255), 3)

# 9. Mostrar las imágenes con los títulos actualizados a 1388
cv2.imshow("Chevrolet original 1388", img1388)
cv2.imshow("Chevrolet 90 1388", img90_1388)
cv2.imshow("Chevrolet 45 1388", img45_1388)
cv2.imshow("Chevrolet 600x500 1388", img600x500_1388)
cv2.imshow("Chevrolet rojo 1388", img_rojo_1388)

# 10. Guardar las imágenes procesadas
cv2.imwrite(str(carpeta_resultados / "img-chevrolet1-1388.jpg"), img90_1388)
cv2.imwrite(str(carpeta_resultados / "img-chevrolet2-1388.jpg"), img45_1388)
cv2.imwrite(str(carpeta_resultados / "img-chevrolet3-1388.jpg"), img600x500_1388)
cv2.imwrite(str(carpeta_resultados / "img-chevrolet4-1388.jpg"), img_rojo_1388)

# 11. Finalizar
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("David Barrera NC = 1388")