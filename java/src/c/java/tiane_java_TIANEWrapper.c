#include <JIANE.h>

#include "tiane_java_TIANEWrapper.h"

#include <dlfcn.h>

JNIEXPORT void JNICALL Java_tiane_java_TIANEWrapper_startTiane(JNIEnv *env, jclass clazz, jstring runPy, jstring runDir, jobjectArray dlopens) {

  if ((*env)->GetJavaVM(env, &JIANE_jvm) == 0) {
    JIANE_jni_version = (*env)->GetVersion(env);
  } else {
    jclass exClass = (*env)->FindClass(env, "java/lang/InternalError");
    (*env)->ThrowNew(env, exClass, "Could not fetch JVM reference");
    return;
  }

  FILE *script = fopen((*env)->GetStringUTFChars(env, runPy, NULL), "r");

  chdir((*env)->GetStringUTFChars(env, runDir, NULL));

  int dlopens_length = (*env)->GetArrayLength(env, dlopens);
  for (int dlopens_index = 0;dlopens_index < dlopens_length;dlopens_index++) {
    dlopen((*env)->GetStringUTFChars(env, (*env)->GetObjectArrayElement(env, dlopens, dlopens_index), NULL), RTLD_LAZY | RTLD_GLOBAL);
  }

  Py_SetProgramName(Py_DecodeLocale("TIANE_server", NULL));
  Py_Initialize();

  wchar_t *runPyW[] = {Py_DecodeLocale((*env)->GetStringUTFChars(env, runPy, NULL), NULL), Py_DecodeLocale("jni", NULL)};
  PySys_SetArgv(2, runPyW);

  if (PyRun_SimpleFile(script, (*env)->GetStringUTFChars(env, runPy, NULL)) < 0) {
    jclass exClass = (*env)->FindClass(env, "tiane/java/TianeException");
    (*env)->ThrowNew(env, exClass, "TIANE raised an error.");
  }
}