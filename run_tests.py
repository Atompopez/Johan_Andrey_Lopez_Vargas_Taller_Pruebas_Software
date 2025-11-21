#!/usr/bin/env python3
"""
Script para ejecutar todos los tests y mostrar un resumen detallado
"""
import subprocess
import sys
import os

def run_tests():
    """Ejecuta todos los tests y muestra un resumen"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    venv_pytest = os.path.join(script_dir, 'venv', 'bin', 'pytest')
    test_dir = os.path.join(script_dir, 'test')
    
    print("🧪 Ejecutando todos los tests...\n")
    
    # Ejecutar pytest con formato detallado
    result = subprocess.run(
        [venv_pytest, test_dir, '-v', '--tb=short'],
        capture_output=True,
        text=True
    )
    
    # Mostrar la salida
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    # Extraer y mostrar resumen final
    output_lines = result.stdout.split('\n')
    summary_line = None
    for line in output_lines:
        if 'passed' in line.lower() and ('failed' in line.lower() or 'error' in line.lower() or '=' in line):
            summary_line = line.strip()
            break
        elif 'passed' in line.lower() and '=' in line and 'test session' not in line.lower():
            summary_line = line.strip()
    
    if summary_line:
        print(f"\n{'='*60}")
        print(f"📊 RESUMEN: {summary_line}")
        print(f"{'='*60}\n")
    
    # Contar tests
    passed = result.stdout.count(' PASSED')
    failed = result.stdout.count(' FAILED')
    errors = result.stdout.count(' ERROR')
    
    if passed > 0:
        print(f"✅ Tests exitosos: {passed}")
    if failed > 0:
        print(f"❌ Tests fallidos: {failed}")
    if errors > 0:
        print(f"⚠️  Errores: {errors}")
    
    return result.returncode

if __name__ == '__main__':
    sys.exit(run_tests())

