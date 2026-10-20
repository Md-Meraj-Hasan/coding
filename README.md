# AndroWish Android Build Probe v0.1

## Why this is separate
This is an isolated experiment. **Do not upload this over your Jupyter app repository or replace its build workflow.**
The existing app uses Chaquopy Python 3.10.22; its diagnostic confirmed that both `tkinter` and `_tkinter` are missing.

## What this experiment does
- Downloads the official AndroWish source archive pinned to release `8e9d986cd1`.
- Attempts to build the standalone Android Tcl/Tk application with its own Gradle wrapper.
- Uploads the resulting APK if the build succeeds, and uploads logs/source summary even if it fails.
- This validates the Android Tcl/Tk/SDL build path separately. It does **not** add Python Tkinter to Jupyter and does not claim to.

## How to run it
1. Create a **new, separate GitHub repository** named `androwish-android-build-probe`.
2. Extract this ZIP.
3. Upload the contents inside `AndroWish-Android-Build-Probe-v0.1` to that new repository's root, including the `.github` folder.
4. Open **Actions** → **AndroWish Native Build Probe** → **Run workflow**.
5. Wait for completion and download the artifact `androwish-build-diagnostics`.
6. If build succeeds, download `androwish-native-apk`; install it only if you want to test the standalone Tcl/Tk app.

## What success/failure tells us
- If the standalone APK builds and opens, Android's Tcl/Tk native GUI route is viable as a separate app.
- If it fails, send `build.log` and `environment.txt`; these show the exact toolchain or source incompatibility.
- Even a successful standalone AndroWish build is only Stage 1. It does not provide a CPython `_tkinter` extension compatible with Chaquopy. That remains a separate native integration task.

## Safety
This repository is isolated and does not touch your existing Jupyter project, APK, dependencies, or workflow.
