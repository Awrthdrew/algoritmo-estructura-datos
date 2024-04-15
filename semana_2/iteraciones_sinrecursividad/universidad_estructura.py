calificacion = float(input("¿Cuánto te sacaste pibe?: "))

descuento = 0

if calificacion >= 9.5:
    descuento = 0.75
elif calificacion >= 9:
    descuento = 0.40
elif calificacion >= 8:
    descuento = 0.25
elif calificacion >= 7:
    descuento = 0.10
elif calificacion >= 4:
    descuento = 0.02

print(f"Su descuento es de {descuento:.0%}")
