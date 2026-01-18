# Cómo Activar GitHub Pages para TrackG

## Pasos para Habilitar GitHub Pages

Una vez que esta Pull Request sea fusionada a la rama `main` o `master`, sigue estos pasos:

### 1. Ve a la Configuración del Repositorio
- Abre tu repositorio en GitHub: https://github.com/diegoturijancontacto-sudo/TrackG
- Haz clic en **Settings** (Configuración) en la parte superior

### 2. Configura GitHub Pages
- En el menú lateral izquierdo, busca y haz clic en **Pages**
- En la sección **Source** (Fuente):
  - Selecciona **GitHub Actions** del menú desplegable
  - ¡No necesitas seleccionar ninguna rama!

### 3. Espera el Despliegue
- Ve a la pestaña **Actions** de tu repositorio
- Verás el workflow "Deploy to GitHub Pages" ejecutándose
- Espera a que termine (icono verde ✅)

### 4. Accede a tu Sitio
Tu aplicación estará disponible en:
```
https://diegoturijancontacto-sudo.github.io/TrackG/
```

## Actualizaciones Automáticas

Cada vez que hagas push a la rama `main` o `master`:
1. El workflow de GitHub Actions se ejecutará automáticamente
2. Tu sitio se actualizará con los últimos cambios
3. No necesitas hacer nada manual

## Verificación

Para verificar que todo funciona:
1. Abre el enlace de tu sitio
2. Permite el acceso a la cámara cuando te lo pida el navegador
3. Selecciona un ejercicio
4. La aplicación debe comenzar a rastrear tus movimientos

## Solución de Problemas

### El sitio no se despliega
- Verifica que GitHub Pages esté configurado en **GitHub Actions**
- Revisa la pestaña **Actions** para ver si hay errores
- Asegúrate de que el workflow haya terminado correctamente

### El sitio muestra un 404
- Espera unos minutos después del primer despliegue
- Verifica que la URL sea correcta: `https://tu-usuario.github.io/nombre-repo/`
- Limpia la caché de tu navegador

### La cámara no funciona
- Asegúrate de que tu navegador tenga permisos de cámara
- Usa HTTPS (GitHub Pages usa HTTPS automáticamente)
- Prueba en un navegador diferente (Chrome, Firefox, Edge, Safari)

## Recursos Adicionales

- [Documentación oficial de GitHub Pages](https://docs.github.com/pages)
- [Documentación de GitHub Actions](https://docs.github.com/actions)
- [Troubleshooting GitHub Pages](https://docs.github.com/pages/getting-started-with-github-pages/troubleshooting-jekyll-build-errors-for-github-pages-sites)
