from connection_mysql import cursor, db
import time


class Menu:
    def mostrar_menu(self):
        print("===========================================")
        print("     Bienvenido a Bike - Sports    ")
        print("===========================================")
        print("      ¡Pedalea hacia el éxito!     ")
        time.sleep(2)  # Esperar 2 segundos

        while True:
            print(
                """
        ¿Qué deseas realizar?

        [1] Gestión de Almacenes.
        [2] Gestión de Cargos.
        [3] Gestión de Empleados.
        [4] Gestión de Proveedores.
        [5] Gestión de Repuestos.
        [6] Gestión de Ventas.
        [7] Gestión de Inventarios.
        [8] Salir.

        

        || Desarrollador: Kevin Chacón ||
                """
            )

            opcion = input("Elige una opción: ")

            if opcion == "1":
                gestion_almacenes = Almacen()
                gestion_almacenes.mostrar_submenu()
            elif opcion == "2":
                gestion_cargos = Cargo()
                gestion_cargos.mostrar_submenu()
            elif opcion == "3":
                gestion_empleados = Empleado()
                gestion_empleados.mostrar_submenu()
            elif opcion == "4":
                gestion_proveedores = Proveedor()
                gestion_proveedores.mostrar_submenu()
            elif opcion == "5":
                gestion_repuestos = Repuestos()
                gestion_repuestos.mostrar_submenu()
            elif opcion == "6":
                gestion_ventas = Ventas()
                gestion_ventas.mostrar_submenu()
            elif opcion == "7":
                gestion_inventario = Inventario()
                gestion_inventario.submenu_inventario()
            elif opcion == "8":
                print("¡Hasta luego!")
                break
            else:
                print("Opción incorrecta")


class Almacen:
    def mostrar_submenu(self):
        while True:
            print(
                """
            ¿Qué deseas realizar en la Gestión de Almacenes?

            [1] Agregar un Almacén.
            [2] Buscar Almacén.
            [3] Buscar Almacén por ID.
            [4] Volver al menú principal.
            """
            )

            opcion = input("Elige una opción: ")

            if opcion == "1":
                id_almacen = input("Ingrese el ID del almacén: ")
                nombre = input("Ingrese el nombre del almacén: ")
                ciudad = input("Ingrese la ciudad del almacén: ")
                responsable = input("Ingrese el responsable del almacén: ")
                capacidad = input("Ingrese la capacidad del almacén: ")
                self.agregar_almacen(id_almacen, nombre, ciudad, responsable, capacidad)
                print("¡Almacén agregado exitosamente!")
            elif opcion == "2":
                self.buscar_almacen()
            elif opcion == "3":
                id_almacen = input("Ingrese el ID del almacén: ")
                self.buscar_almacen_por_id(id_almacen)
            elif opcion == "4":
                break
            else:
                print("Opción incorrecta")

            continuar = input("¿Deseas continuar en la Gestión de Almacenes? (S/N): ")
            if continuar.lower() != "s":
                break

    def agregar_almacen(self, id_almacen, nombre, ciudad, responsable, capacidad):
        mysql = "INSERT INTO almacen (idalmacen, nombre, ciudad, responsable, capacidad) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(mysql, (id_almacen, nombre, ciudad, responsable, capacidad))
        db.commit()

    def buscar_almacen1(self):
        mysql = "SELECT * FROM almacen"
        cursor.execute(mysql)
        data = cursor.fetchall()
        for almacen in data:
            print("ID Almacen:", almacen[0])
            print("Nombre:", almacen[1])
            print("Ciudad:", almacen[2])
            print("Responsable:", almacen[3])
            print("Capacidad:", almacen[4])
            print("---")

    def buscar_almacen(self):
        mysql = "SELECT * FROM almacen"
        cursor.execute(mysql)
        data = cursor.fetchall()

        print("+" + "-" * 79 + "+")  # Línea superior del encabezado
        print(
            "| {:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^10s} |".format(
                "ID Almacen", "Nombre", "Ciudad", "Responsable", "Capacidad"
            )
        )
        print("+" + "-" * 79 + "+")  # Línea horizontal entre el encabezado y los datos

        for almacen in data:
            print(
                "| {:^10d} | {:^15s} | {:^15s} | {:^15s} | {:^10d} |".format(
                    almacen[0], almacen[1], almacen[2], almacen[3], almacen[4]
                )
            )

        print("+" + "-" * 79 + "+")  # Línea inferior

    def buscar_almacen_por_id(self, id_almacen):
        mysql = "SELECT * FROM almacen WHERE idalmacen = %s"
        cursor.execute(mysql, (id_almacen,))
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 79 + "+")  # Línea superior del encabezado
            print(
                "| {:^10s} | {:^15s} | {:^15s} | {:^15s} | {:^10s} |".format(
                    "ID Almacen", "Nombre", "Ciudad", "Responsable", "Capacidad"
                )
            )
            print(
                "+" + "-" * 79 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for almacen in data:
                print(
                    "| {:^10d} | {:^15s} | {:^15s} | {:^15s} | {:^10d} |".format(
                        almacen[0], almacen[1], almacen[2], almacen[3], almacen[4]
                    )
                )

            print("+" + "-" * 79 + "+")  # Línea inferior
        else:
            print("No se encontró ningún almacén con el ID especificado.")


class Cargo:
    def mostrar_submenu(self):
        while True:
            print(
                """
            ¿Qué deseas realizar en la Gestión de Cargos?

            [1] Agregar un Cargo.
            [2] Buscar Cargos.
            [3] Buscar Cargo por ID.
            [4] Volver al menú principal.
            """
            )

            opcion = input("Elige una opción: ")

            if opcion == "1":
                id_cargo = input("Ingrese el ID del cargo: ")
                nombre = input("Ingrese el nombre del cargo: ")
                self.agregar_cargo(id_cargo, nombre)
                print("¡Cargo agregado exitosamente!")
            elif opcion == "2":
                self.buscar_cargos()
            elif opcion == "3":
                id_cargo = input("Ingrese el ID del cargo: ")
                self.buscar_cargo_por_id(id_cargo)
            elif opcion == "4":
                break
            else:
                print("Opción incorrecta")

            continuar = input("¿Deseas continuar en la Gestión de Cargos? (S/N): ")
            if continuar.lower() != "s":
                break

    def agregar_cargo(self, id_cargo, nombre):
        mysql = "INSERT INTO cargos (idcargos, nombre) VALUES (%s,%s)"
        cursor.execute(mysql, (id_cargo, nombre))
        db.commit()

    def buscar_cargos(self):
        mysql = "SELECT * FROM cargos"
        cursor.execute(mysql)
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 28 + "+")  # Línea superior del encabezado
            print("| {:^8s} | {:^15s} |".format("ID Cargo", "Nombre"))
            print(
                "+" + "-" * 28 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for cargo in data:
                print("| {:^8d} | {:^15s} |".format(cargo[0], cargo[1]))

            print("+" + "-" * 28 + "+")  # Línea inferior
        else:
            print("No se encontraron cargos en la base de datos.")

    def buscar_cargo_por_id(self, id_cargo):
        mysql = "SELECT * FROM cargos WHERE idcargos = %s"
        cursor.execute(mysql, (id_cargo))
        cargo = cursor.fetchone()

        if cargo:
            print("+" + "-" * 28 + "+")  # Línea superior del encabezado
            print("| {:^8s} | {:^15s} |".format("ID Cargo", "Nombre"))
            print(
                "+" + "-" * 28 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            print("| {:^8d} | {:^15s} |".format(cargo[0], cargo[1]))

            print("+" + "-" * 28 + "+")  # Línea inferior
        else:
            print("No se encontró un cargo con el ID especificado.")


class Empleado:
    def mostrar_submenu(self):
        while True:
            print(
                """
            ¿Qué deseas realizar en la Gestión de Empleados?

            [1] Agregar un Empleado.
            [2] Buscar Empleados.
            [3] Buscar Empleado por ID.
            [4] Volver al menú principal.
            """
            )

            opcion = input("Elige una opción: ")

            if opcion == "1":
                id_empleado = input("Ingrese el ID del empleado: ")
                nombres = input("Ingrese los nombres del empleado: ")
                apellidos = input("Ingrese los apellidos del empleado: ")
                correo = input("Ingrese el correo del empleado: ")
                direccion = input("Ingrese la dirección del empleado: ")
                telefono = input("Ingrese el teléfono del empleado: ")
                salario = input("Ingrese el salario del empleado: ")
                id_almacen = input("Ingrese el ID del almacén asignado al empleado: ")
                id_cargo = input("Ingrese el ID del cargo del empleado: ")
                self.agregar_empleado(
                    id_empleado,
                    nombres,
                    apellidos,
                    correo,
                    direccion,
                    telefono,
                    salario,
                    id_almacen,
                    id_cargo,
                )
                print("¡Empleado agregado exitosamente!")
            elif opcion == "2":
                self.buscar_empleados()
            elif opcion == "3":
                id_empleado = input("Ingrese el ID del empleado: ")
                self.buscar_empleado_por_id(id_empleado)
            elif opcion == "4":
                break
            else:
                print("Opción incorrecta")

            continuar = input("¿Deseas continuar en la Gestión de Empleados? (S/N): ")
            if continuar.lower() != "s":
                break

    def agregar_empleado(
        self,
        id_empleado,
        nombres,
        apellidos,
        correo,
        direccion,
        telefono,
        salario,
        id_almacen,
        id_cargo,
    ):
        mysql = (
            "INSERT INTO empleado (idempleados, nombres, apellidos, correo, direccion, telefono, salario, "
            "almacen_idalmacen, cargos_idcargos) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        )
        cursor.execute(
            mysql,
            (
                id_empleado,
                nombres,
                apellidos,
                correo,
                direccion,
                telefono,
                salario,
                id_almacen,
                id_cargo,
            ),
        )
        db.commit()

    def buscar_empleados(self):
        mysql = "SELECT * FROM empleado"
        cursor.execute(mysql)
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 177 + "+")  # Línea superior del encabezado
            print(
                "| {:^12s} | {:^20s} | {:^20s} | {:^25s} | {:^30s} | {:^12s} | {:^10s} | {:^12s} | {:^10s} |".format(
                    "ID Empleado",
                    "Nombres",
                    "Apellidos",
                    "Correo",
                    "Dirección",
                    "Teléfono",
                    "Salario",
                    "ID Almacén",
                    "ID Cargo",
                )
            )
            print(
                "+" + "-" * 177 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for empleado in data:
                print(
                    "| {:^12d} | {:^20s} | {:^20s} | {:^25s} | {:^30s} | {:^12s} | {:^10.2f} | {:^12d} | {:^10d} |".format(
                        empleado[0],
                        empleado[1],
                        empleado[2],
                        empleado[3],
                        empleado[4],
                        empleado[5],
                        empleado[6],
                        empleado[7],
                        empleado[8],
                    )
                )

            print("+" + "-" * 177 + "+")  # Línea inferior
        else:
            print("No se encontraron empleados en la base de datos.")

    def buscar_empleado_por_id(self, id_empleado):
        mysql = "SELECT * FROM empleado WHERE idempleados = %s"
        cursor.execute(mysql, (id_empleado,))
        empleado = cursor.fetchone()

        if empleado is not None:
            print("+" + "-" * 177 + "+")  # Línea superior del encabezado
            print(
                "| {:^12s} | {:^20s} | {:^20s} | {:^25s} | {:^30s} | {:^12s} | {:^10s} | {:^12s} | {:^10s} |".format(
                    "ID Empleado",
                    "Nombres",
                    "Apellidos",
                    "Correo",
                    "Dirección",
                    "Teléfono",
                    "Salario",
                    "ID Almacén",
                    "ID Cargo",
                )
            )
            print(
                "+" + "-" * 177 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            print(
                "| {:^12d} | {:^20s} | {:^20s} | {:^25s} | {:^30s} | {:^12s} | {:^10.2f} | {:^12d} | {:^10d} |".format(
                    empleado[0],
                    empleado[1],
                    empleado[2],
                    empleado[3],
                    empleado[4],
                    empleado[5],
                    empleado[6],
                    empleado[7],
                    empleado[8],
                )
            )

            print("+" + "-" * 177 + "+")  # Línea inferior
        else:
            print("No se encontró un empleado con el ID especificado.")


class Proveedor:
    def mostrar_submenu(self):
        while True:
            print(
                """
            ¿Qué deseas realizar en la Gestión de Proveedores?

            [1] Agregar un Proveedor.
            [2] Buscar Proveedores.
            [3] Buscar Proveedor por ID.
            [4] Volver al menú principal.
            """
            )

            opcion = input("Elige una opción: ")

            if opcion == "1":
                id_proveedor = input("Ingrese el ID del proveedor: ")
                nombre = input("Ingrese el nombre del proveedor: ")
                ciudad = input("Ingrese la ciudad del proveedor: ")
                telefono = input("Ingrese el teléfono del proveedor: ")
                correo = input("Ingrese el correo del proveedor: ")
                productos_suministrados = input(
                    "Ingrese los productos suministrados por el proveedor: "
                )
                metodos_pago = input("Ingrese los métodos de pago del proveedor: ")
                self.agregar_proveedor(
                    id_proveedor,
                    nombre,
                    ciudad,
                    telefono,
                    correo,
                    productos_suministrados,
                    metodos_pago,
                )
                print("¡Proveedor agregado exitosamente!")
            elif opcion == "2":
                self.buscar_proveedores()
            elif opcion == "3":
                id_proveedor = input("Ingrese el ID del proveedor: ")
                self.buscar_proveedor_por_id(id_proveedor)
            elif opcion == "4":
                break
            else:
                print("Opción incorrecta")

            continuar = input("¿Deseas continuar en la Gestión de Proveedores? (S/N): ")
            if continuar.lower() != "s":
                break

    def agregar_proveedor(
        self,
        id_proveedor,
        nombre,
        ciudad,
        telefono,
        correo,
        productos_suministrados,
        metodos_pago,
    ):
        mysql = (
            "INSERT INTO proveedor (idproveedor, nombre, ciudad, telefono, correo, productos_suministrados, "
            "metodos_pago) VALUES (%s,%s,%s,%s,%s,%s,%s) "
        )
        cursor.execute(
            mysql,
            (
                id_proveedor,
                nombre,
                ciudad,
                telefono,
                correo,
                productos_suministrados,
                metodos_pago,
            ),
        )
        db.commit()

    def buscar_proveedores(self):
        mysql = "SELECT * FROM proveedor"
        cursor.execute(mysql)
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 179 + "+")  # Línea superior del encabezado
            print(
                "| {:^15s} | {:^30s} | {:^20s} | {:^15s} | {:^25s} | {:^30s} | {:^30s} |".format(
                    "ID Proveedor",
                    "Nombre",
                    "Ciudad",
                    "Teléfono",
                    "Correo",
                    "Productos Suministrados",
                    "Métodos de Pago",
                )
            )
            print(
                "+" + "-" * 179 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for proveedor in data:
                print(
                    "| {:^15d} | {:^30s} | {:^20s} | {:^15s} | {:^25s} | {:^30s} | {:^30s} |".format(
                        proveedor[0],
                        proveedor[1],
                        proveedor[2],
                        proveedor[3],
                        proveedor[4],
                        proveedor[5],
                        proveedor[6],
                    )
                )

            print("+" + "-" * 179 + "+")  # Línea inferior
        else:
            print("No se encontraron proveedores en la base de datos.")

    def buscar_proveedor_por_id(self, id_proveedor):
        mysql = "SELECT * FROM proveedor WHERE idproveedor = %s"
        cursor.execute(mysql, (id_proveedor,))
        proveedor = cursor.fetchone()

        if proveedor:
            print("+" + "-" * 179 + "+")  # Línea superior del encabezado
            print(
                "| {:^15s} | {:^30s} | {:^20s} | {:^15s} | {:^25s} | {:^30s} | {:^30s} |".format(
                    "ID Proveedor",
                    "Nombre",
                    "Ciudad",
                    "Teléfono",
                    "Correo",
                    "Productos Suministrados",
                    "Métodos de Pago",
                )
            )
            print(
                "+" + "-" * 179 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            print(
                "| {:^15d} | {:^30s} | {:^20s} | {:^15s} | {:^25s} | {:^30s} | {:^30s} |".format(
                    proveedor[0],
                    proveedor[1],
                    proveedor[2],
                    proveedor[3],
                    proveedor[4],
                    proveedor[5],
                    proveedor[6],
                )
            )

            print("+" + "-" * 179 + "+")  # Línea inferior
        else:
            print("No se encontró un proveedor con el ID especificado.")


class Repuestos:
    def mostrar_submenu(self):
        while True:
            print(
                """
            ¿Qué deseas realizar en la Gestión de Repuestos?

            [1] Agregar un Repuesto.
            [2] Mostrar Repuestos.
            [3] Buscar Repuesto por ID.
            [4] Volver al menú principal.
            """
            )

            opcion = input("Elige una opción: ")

            if opcion == "1":
                id_repuesto = input("Ingrese el ID del repuesto: ")
                nombre = input("Ingrese el nombre del repuesto: ")
                descripcion = input("Ingrese la descripción del repuesto: ")
                marca = input("Ingrese la marca del repuesto: ")
                precio = input("Ingrese el precio del repuesto: ")
                modelo = input("Ingrese el modelo del repuesto: ")
                tipo = input("Ingrese el tipo del repuesto: ")
                tamaño = input("Ingrese el tamaño del repuesto: ")
                id_proveedor = input("Ingrese el ID del proveedor del repuesto: ")
                self.agregar_repuesto(
                    id_repuesto,
                    nombre,
                    descripcion,
                    marca,
                    precio,
                    modelo,
                    tipo,
                    tamaño,
                    id_proveedor,
                )
                print("¡Repuesto agregado exitosamente!")
            elif opcion == "2":
                self.mostrar_repuestos()
            elif opcion == "3":
                id_repuesto = input("Ingrese el ID del repuesto: ")
                self.buscar_repuesto_por_id(id_repuesto)
            elif opcion == "4":
                break
            else:
                print("Opción incorrecta")

            continuar = input("¿Deseas continuar en la Gestión de Repuestos? (S/N): ")
            if continuar.lower() != "s":
                break

    def agregar_repuesto(
        self,
        id_repuesto,
        nombre,
        descripcion,
        marca,
        precio,
        modelo,
        tipo,
        tamaño,
        id_proveedor,
    ):
        mysql = (
            "INSERT INTO repuesto (idrepuesto, nombre, descripción, marca, precio, modelo, tipo, tamaño, "
            "proveedor_idproveedor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        )
        cursor.execute(
            mysql,
            (
                id_repuesto,
                nombre,
                descripcion,
                marca,
                precio,
                modelo,
                tipo,
                tamaño,
                id_proveedor,
            ),
        )
        db.commit()

    def mostrar_repuestos(self):
        mysql = "SELECT * FROM repuesto"
        cursor.execute(mysql)
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 180 + "+")  # Línea superior del encabezado
            print(
                "| {:^15s} | {:^30s} | {:^40s} | {:^20s} | {:^15s} | {:^20s} | {:^20s} | {:^20s} | {:^15s} |".format(
                    "ID Repuesto",
                    "Nombre",
                    "Descripción",
                    "Marca",
                    "Precio",
                    "Modelo",
                    "Tipo",
                    "Tamaño",
                    "ID Proveedor",
                )
            )
            print(
                "+" + "-" * 180 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for repuesto in data:
                print(
                    "| {:^15d} | {:^30s} | {:^40s} | {:^20s} | {:^15.2f} | {:^20s} | {:^20s} | {:^20s} | {:^15d} |".format(
                        repuesto[0],
                        repuesto[1],
                        repuesto[2],
                        repuesto[3],
                        repuesto[4],
                        repuesto[5],
                        repuesto[6],
                        repuesto[7],
                        repuesto[8],
                    )
                )

            print("+" + "-" * 180 + "+")  # Línea inferior
        else:
            print("No se encontraron repuestos en la base de datos.")

    def buscar_repuesto_por_id(selft, id_repuesto):
        mysql = "SELECT * FROM repuesto WHERE idrepuesto = %s"
        cursor.execute(mysql, (id_repuesto,))
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 120 + "+")  # Línea superior del encabezado
            print(
                "| {:^15s} | {:^30s} | {:^40s} | {:^20s} | {:^15s} | {:^20s} | {:^20s} | {:^20s} | {:^15s} |".format(
                    "ID Repuesto",
                    "Nombre",
                    "Descripción",
                    "Marca",
                    "Precio",
                    "Modelo",
                    "Tipo",
                    "Tamaño",
                    "ID Proveedor",
                )
            )
            print(
                "+" + "-" * 120 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for repuesto in data:
                print(
                    "| {:^15d} | {:^30s} | {:^40s} | {:^20s} | {:^15.2f} | {:^20s} | {:^20s} | {:^20s} | {:^15d} |".format(
                        repuesto[0],
                        repuesto[1],
                        repuesto[2],
                        repuesto[3],
                        repuesto[4],
                        repuesto[5],
                        repuesto[6],
                        repuesto[7],
                        repuesto[8],
                    )
                )

            print("+" + "-" * 120 + "+")  # Línea inferior
        else:
            print("No se encontró ningún repuesto con el ID especificado.")


class Ventas:
    def mostrar_submenu(self):
        while True:
            print(
                """
            ¿Qué deseas realizar en la Gestión de Ventas?

            [1] Agregar una Venta.
            [2] Mostrar Ventas.
            [3] Volver al menú principal.
            """
            )

            opcion = input("Elige una opción: ")

            if opcion == "1":
                id_venta = input("Ingrese el ID de la venta: ")
                fecha = input("Ingrese la fecha de la venta: ")
                nombre_cliente = input("Ingrese el nombre del cliente: ")
                total = input("Ingrese el total de la venta: ")
                forma_pago = input("Ingrese la forma de pago: ")
                estado_pago = input("Ingrese el estado de pago: ")
                id_almacen = input("Ingrese el ID del almacén: ")
                id_empleado = input("Ingrese el ID del empleado: ")
                id_repuesto = input("Ingrese el ID del repuesto: ")
                self.agregar_venta(
                    id_venta,
                    fecha,
                    nombre_cliente,
                    total,
                    forma_pago,
                    estado_pago,
                    id_almacen,
                    id_empleado,
                    id_repuesto,
                )
                print("¡Venta agregada exitosamente!")
            elif opcion == "2":
                self.mostrar_ventas()
            elif opcion == "3":
                break
            else:
                print("Opción incorrecta")

            continuar = input("¿Deseas continuar en la Gestión de Ventas? (S/N): ")
            if continuar.lower() != "s":
                break

    def agregar_venta(
        self,
        id_venta,
        fecha,
        nombre_cliente,
        total,
        forma_pago,
        estado_pago,
        id_almacen,
        id_empleado,
        id_repuesto,
    ):
        mysql = (
            "INSERT INTO ventas (idventas, fecha, nombre_cliente, total, forma_pago, estado_pago, "
            "almacen_idalmacen, empleado_idempleados, repuesto_idrepuesto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        )
        cursor.execute(
            mysql,
            (
                id_venta,
                fecha,
                nombre_cliente,
                total,
                forma_pago,
                estado_pago,
                id_almacen,
                id_empleado,
                id_repuesto,
            ),
        )
        db.commit()

        mysql_update = "UPDATE inventario SET stock = stock - 1 WHERE almacen_idalmacen = %s AND repuesto_idrepuesto = %s"
        cursor.execute(mysql_update, (id_almacen, id_repuesto))
        db.commit()

    def mostrar_ventas(self):
        mysql = "SELECT * FROM ventas"
        cursor.execute(mysql)
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 173 + "+")  # Línea superior del encabezado
            print(
                "| {:^15s} | {:^20s} | {:^30s} | {:^15s} | {:^20s} | {:^20s} | {:^15s} | {:^15s} |".format(
                    "ID Venta",
                    "Fecha",
                    "Nombre del Cliente",
                    "Total",
                    "Forma de Pago",
                    "Estado de Pago",
                    "ID Almacén",
                    "ID Empleado",
                )
            )
            print(
                "+" + "-" * 173 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for venta in data:
                print(
                    "| {:^15d} | {:^20s} | {:^30s} | {:^15.2f} | {:^20s} | {:^20s} | {:^15d} | {:^15d} |".format(
                        venta[0],
                        str(venta[1]),
                        venta[2],
                        venta[3],
                        venta[4],
                        venta[5],
                        venta[6],
                        venta[7],
                    )
                )

            print("+" + "-" * 173 + "+")  # Línea inferior
        else:
            print("No se encontraron ventas en la base de datos.")


class Inventario:
    def submenu_inventario(self):
        while True:
            print(
                """
            ¿Qué deseas realizar en la Gestión de inventarios?

            [1] Agregar un inventario.
            [2] Buscar inventario por almacén.
            [3] Buscar inventario por repuesto.
            [4] Mostrar inventario.
            [5] Volver al menú principal.
            """
            )
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                idinventario = input("Ingrese el ID del inventario: ")
                id_almacen = input("Ingrese el ID del almacen: ")
                id_repuesto = input("Ingrese el ID del repuesto: ")
                stock = input("Ingrese la cantidad del stock: ")

                self.agregar_inventario(idinventario, id_almacen, id_repuesto, stock)
                print("¡Inventario agregado exitosamente!")
            elif opcion == "2":
                almacen_id = input("Ingrese el ID del almacén: ")
                self.buscar_inventario_por_almacen(almacen_id)
            elif opcion == "3":
                repuesto_id = input("Ingrese el ID del repuesto: ")
                self.buscar_inventario_por_repuesto(repuesto_id)
            elif opcion == "4":
                self.mostrar_inventario()
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

            continuar = input("¿Deseas continuar en la Gestión de inventarios? (S/N): ")
            if continuar.lower() != "s":
                break

    def agregar_inventario(self, idinventario, almacen_id_almacen, repuesto_id_repuesto, stock):
        mysql = "INSERT INTO inventario (id_inventario, almacen_idalmacen, repuesto_idrepuesto, stock) VALUES (%s, %s, %s, %s)"
        cursor.execute(mysql, (idinventario, almacen_id_almacen, repuesto_id_repuesto, stock))
        db.commit()

    def mostrar_inventario(self):
        mysql = "SELECT * FROM inventario"
        cursor.execute(mysql)
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 62 + "+")  # Línea superior del encabezado
            print(
                "| {:^15s} | {:^15s} | {:^10s} | {:^10s} |".format(
                    "ID inventario", "ID Almacén", "ID Repuesto", "Stock"
                )
            )
            print(
                "+" + "-" * 62 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for inventario in data:
                print(
                    "| {:^15d} | {:^15d} | {:^10d} |  {:^10d} |".format(
                        inventario[0], inventario[1], inventario[2], inventario[3]
                    )
                )

            print("+" + "-" * 62 + "+")  # Línea inferior
        else:
            print("No se encontró inventario en la base de datos.")

    def buscar_inventario_por_almacen(self, almacen_id):
        mysql = "SELECT * FROM inventario WHERE almacen_idalmacen = %s"
        cursor.execute(mysql, (almacen_id,))
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 62 + "+")  # Línea superior del encabezado
            print(
                "| {:^15s} | {:^15s} | {:^10s} | {:^10s} |".format(
                    "ID inventario", "ID Almacén", "ID Repuesto", "Stock"
                )
            )
            print(
                "+" + "-" * 62 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for inventario in data:
                print(
                    "| {:^15d} | {:^15d} | {:^10d} | {:^10d} |".format(
                        inventario[0], inventario[1], inventario[2], inventario[3]
                    )
                )

            print("+" + "-" * 62 + "+")  # Línea inferior
        else:
            print("No se encontró inventario para el almacén especificado.")

    def buscar_inventario_por_repuesto(self, repuesto_id):
        mysql = "SELECT * FROM inventario WHERE repuesto_idrepuesto = %s"
        cursor.execute(mysql, (repuesto_id,))
        data = cursor.fetchall()

        if len(data) > 0:
            print("+" + "-" * 62 + "+")  # Línea superior del encabezado
            print(
                "| {:^15s} | {:^15s} | {:^10s} | {:^10s} |".format(
                    "ID inventario", "ID Almacén", "ID Repuesto", "Stock"
                )
            )
            print(
                "+" + "-" * 62 + "+"
            )  # Línea horizontal entre el encabezado y los datos

            for inventario in data:
                print(
                    "| {:^15d} | {:^15d} | {:^10d} | {:^10d} |".format(
                        inventario[0], inventario[1], inventario[2], inventario[3]
                    )
                )

            print("+" + "-" * 68 + "+")  # Línea inferior
        else:
            print("No se encontró inventario para el repuesto especificado.")


menu_principal = Menu()
menu_principal.mostrar_menu()
