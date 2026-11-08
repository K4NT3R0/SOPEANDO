# Sopeando

Sopa de letras en español con anuncios AdMob. GitHub compila la app por ti, sin ordenador.

1. Crea un repositorio PRIVADO (la clave de firma se guarda en él).
2. Sube a la raíz: index.html, package.json, capacitor.config.json, patch_android.py y README.md.
3. Add file > Create new file, nombre `.github/workflows/android.yml`, pega el contenido de android.yml y confirma.
4. Settings > Secrets and variables > Actions > New repository secret: `KEYSTORE_PASSWORD` con una contraseña tuya (mínimo 6 caracteres). Guárdala.
5. Actions > Compilar Android > Run workflow. La primera vez déjalo SIN anuncios reales. Tarda unos 10-15 min.
6. Descarga el artefacto "sopeando": trae un APK de prueba para tu móvil y el archivo .aab para Play Console.
7. Para producción: Run workflow con "Anuncios reales" activado y sube ese .aab.

El ID de paquete es com.sopeando.juego y no se puede cambiar una vez publicada la app.
