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
    main_dir = os.path.join(script_dir, 'main')
    
    print("🧪 Ejecutando todos los tests...\n")
    
    # Buscar todos los archivos de test en main/
    test_files = []
    for root, dirs, files in os.walk(main_dir):
        for file in files:
            if file.endswith('Test.py') or file.endswith('test.py'):
                test_files.append(os.path.join(root, file))
    
    if not test_files:
        print("❌ No se encontraron archivos de test")
        return 1
    
    print(f"📁 Encontrados {len(test_files)} archivos de test\n")
    
    # Ejecutar pytest con formato detallado
    # Usar python3 -m pytest en lugar de buscar el ejecutable
    # --continue-on-collection-errors permite ejecutar tests aunque algunos fallen al importar
    cmd = [sys.executable, '-m', 'pytest'] + sorted(test_files) + ['-v', '--tb=short', '--continue-on-collection-errors']
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=script_dir
    )
    
    # Mostrar la salida
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    # Contar tests - buscar en la salida completa
    full_output = result.stdout + result.stderr
    passed = full_output.count(' PASSED')
    failed = full_output.count(' FAILED')
    # Contar errores de importación/colección
    error_count = full_output.count('ERROR collecting')
    
    # Buscar el resumen de pytest
    summary_line = None
    for line in result.stdout.split('\n'):
        if 'passed' in line.lower() and ('failed' in line.lower() or 'error' in line.lower() or '=' in line):
            if 'test session' not in line.lower() and 'collected' not in line.lower() and 'short test' not in line.lower():
                summary_line = line.strip()
                break
    
    print(f"\n{'='*60}")
    print("📊 RESUMEN FINAL")
    print(f"{'='*60}")
    if passed > 0:
        print(f"✅ Tests exitosos: {passed}")
    if failed > 0:
        print(f"❌ Tests fallidos: {failed}")
    if error_count > 0:
        print(f"⚠️  Errores de importación/colección: {error_count}")
    
    total = passed + failed
    if total > 0:
        print(f"\n📈 Total de tests ejecutados: {total}")
        if passed > 0:
            porcentaje = (passed / total) * 100
            print(f"📊 Tasa de éxito: {porcentaje:.1f}%")
    elif error_count > 0 and passed == 0:
        print(f"\n⚠️  No se pudieron ejecutar tests debido a errores de importación")
    print(f"{'='*60}\n")
    
    return result.returncode

if __name__ == '__main__':
    sys.exit(run_tests())

