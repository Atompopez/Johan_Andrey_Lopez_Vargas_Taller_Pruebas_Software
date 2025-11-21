#!/bin/bash

# Script para ejecutar todos los tests y mostrar un resumen

echo "🧪 Ejecutando todos los tests..."
echo ""

cd "$(dirname "$0")"
./venv/bin/pytest test/ -v --tb=short

echo ""
echo "✅ Resumen: Revisa el resultado arriba para ver cuántos tests pasaron"

