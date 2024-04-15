def verificar_rango_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        print("La vlan", vlan_id, "es de rango normal")
    elif 1006 <= vlan_id <= 4095:
        print("La VLAN", vlan_id, "es de rango extendido")
    else:
        print("El numero de vlan ingresado es desconocido")
vlan_id = int(input("Ingrese el id de la vlan: "))

verificar_rango_vlan(vlan_id)